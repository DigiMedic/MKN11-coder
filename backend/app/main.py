from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from .mkn11_processor import MKN11Processor
from .openai_client import OpenAIClient

load_dotenv()

app = FastAPI(
    title="MKN-11 Asistované Kódování",
    description="API pro asistované kódování diagnóz podle standardu MKN-11",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializace procesoru MKN-11 a OpenAI klienta
mkn11_processor = MKN11Processor("/app/data/mkn-11-terminologie-202403.xlsx")
openai_client = OpenAIClient()

class DiagnosisRequest(BaseModel):
    text: str

class DiagnosisCode(BaseModel):
    diagnosis: str
    description: Optional[str]
    icd_code: str
    confidence: str
    is_preliminary: bool
    score: Optional[float]

class DiagnosisResponse(BaseModel):
    codes: List[DiagnosisCode]

@app.post("/api/code", response_model=DiagnosisResponse)
async def code_diagnosis(request: DiagnosisRequest):
    try:
        # Extrakce diagnóz pomocí OpenAI
        extracted_diagnoses = await openai_client.extract_diagnoses(request.text)
        
        # Validace a obohacení výsledků pomocí MKN-11 dat
        validated_codes = []
        for diagnosis in extracted_diagnoses:
            try:
                # Vyhledání v MKN-11 datech
                mkn11_matches = mkn11_processor.find_matching_codes(diagnosis["text"])
                
                if mkn11_matches:
                    # Použijeme nejlepší shodu z MKN-11
                    best_match = mkn11_matches[0]
                    
                    # Získáme detaily diagnózy
                    diagnosis_details = mkn11_processor.get_diagnosis_by_code(best_match["code"])
                    
                    # Pokud je kód navržený AI jiný než nejlepší shoda z MKN-11,
                    # použijeme ten s vyšší důvěryhodností
                    suggested_code = diagnosis.get("suggested_code", best_match["code"])
                    if diagnosis.get("confidence", "low") != "high" and best_match["score"] > 90:
                        suggested_code = best_match["code"]
                    
                    validated_codes.append(
                        DiagnosisCode(
                            diagnosis=diagnosis["text"],
                            description=diagnosis.get("description", diagnosis_details.get("description", "")),
                            icd_code=suggested_code,
                            confidence=diagnosis.get("confidence", "low"),
                            is_preliminary=diagnosis.get("is_preliminary", True),
                            score=best_match["score"]
                        )
                    )
            except KeyError as ke:
                print(f"Chyba při zpracování diagnózy: {ke}")
                print(f"Data diagnózy: {diagnosis}")
                continue
        
        return DiagnosisResponse(codes=validated_codes)
    except Exception as e:
        print(f"Chyba při zpracování textu: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "mkn11_data_loaded": mkn11_processor.terminology_data is not None}
