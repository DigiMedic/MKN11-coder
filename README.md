# MKN-11 Asistované Kódování

![MKN11 Cover](https://utfs.io/f/NyKlEsePJFL1Zxkg6CHqH52V3xpRUZkbs9AW0PMgyzmDavhY)

Vyvíjím systém pro asistované kódování diagnóz podle standardu MKN-11 s využitím umělé inteligence. Mým cílem je zjednodušit a zrychlit proces kódování při zachování přesnosti výsledků.

## Technologie

- **Frontend:** Next.js 14, Tailwind CSS, Shadcn/UI, Framer Motion
- **Backend:** FastAPI (Python)
- **AI Model:** OpenAI GPT-4
- **Data:** MKN-11 terminologie
- **Nasazení:** Docker, Coolify

## Struktura Projektu

```
mkn11/
├── backend/         # FastAPI backend
│   ├── app/        # Aplikační kód
│   ├── tests/      # Testy
│   └── data/       # Data MKN-11
├── frontend/       # Next.js frontend
│   ├── src/        # Zdrojový kód
│   └── public/     # Statické soubory
└── docker/        # Docker konfigurace
```

## Požadavky

- Python 3.11+
- Node.js 18+
- Docker a Docker Compose
- OpenAI API klíč

## Konfigurace

Vytvořte soubor `.env` v kořenovém adresáři pouze s konfigurací OpenAI:
```env
OPENAI_API_KEY=váš-api-klíč
MODEL_NAME=gpt-4-1106-preview
MAX_TOKENS=2000
TEMPERATURE=0.3
```

Ostatní konfigurace je pevně nastavena v `backend/config.py`.

## Instalace a Spuštění

### Lokální Vývoj

1. Backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # nebo `venv\Scripts\activate` na Windows
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

2. Frontend:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### Produkční Nasazení (Coolify)

Projekt je nakonfigurován pro automatické nasazení pomocí Coolify:

1. **Příprava**
   - Naklonujte repozitář
   - Připravte si OpenAI API klíč

2. **Nasazení na Coolify**
   - Vytvořte nový projekt v Coolify
   - Připojte Git repozitář
   - Nastavte environment proměnné:
     ```
     OPENAI_API_KEY=váš-api-klíč
     MODEL_NAME=gpt-4-1106-preview
     MAX_TOKENS=2000
     TEMPERATURE=0.3
     NEXT_PUBLIC_API_URL=https://vaše-api-url
     ```
   - Spusťte deployment

Coolify automaticky:
- Sestaví Docker kontejnery
- Nastaví SSL certifikáty
- Nakonfiguruje reverzní proxy
- Spustí monitoring

## API Dokumentace

Kompletní API dokumentace je dostupná na `/docs` nebo `/redoc` endpointech běžícího backend serveru.

### Hlavní Endpoint

`POST /api/code`

Tento endpoint přijímá text lékařské zprávy a vrací relevantní MKN-11 kódy:

Request:
```json
{
  "text": "Pacient trpí hypertenzí."
}
```

Response:
```json
{
  "codes": [
    {
      "diagnosis": "Hypertenze",
      "code": "BA00",
      "description": "Hypertenzní onemocnění"
    }
  ]
}
```

## Autor

Petr Sovadina
- [LinkedIn](https://www.linkedin.com/in/petrsovadina)
- [Blog](https://portfolio-sovadina.vercel.app/blog)
