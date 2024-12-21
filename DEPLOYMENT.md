# Nasazení na Coolify

## Příprava

1. Naklonujte repozitář
2. Ujistěte se, že máte:
   - Soubor `mkn-11-terminologie-202403.xlsx` ve složce `backend/data/`
   - OpenAI API klíč

## Nasazení v Coolify

1. **Vytvoření služeb**:
   
   a) **Backend služba**:
   - Vytvořte novou službu typu "Docker Service"
   - Zvolte váš Git repozitář
   - Nastavte build kontext na `/backend`
   - Nastavte port na `8000`
   - Přidejte povinnou proměnnou prostředí:
     ```
     OPENAI_API_KEY=váš-openai-api-klíč
     ```
   - Volitelné proměnné (mají výchozí hodnoty):
     ```
     MODEL_NAME=gpt-4-1106-preview
     MAX_TOKENS=2000
     TEMPERATURE=0.3
     DEBUG=False
     MKN11_EXCEL_PATH=/app/data/mkn-11-terminologie-202403.xlsx
     ```

   b) **Frontend služba**:
   - Vytvořte novou službu typu "Docker Service"
   - Zvolte váš Git repozitář
   - Nastavte build kontext na `/frontend`
   - Nastavte port na `3000`
   - Přidejte povinnou proměnnou prostředí:
     ```
     NEXT_PUBLIC_BACKEND_URL=https://api.vase-domena.com
     ```

2. **Nastavení domén**:
   - Pro backend: `api.vase-domena.com`
   - Pro frontend: `vase-domena.com`

3. **SSL/HTTPS**:
   - Coolify automaticky nastaví SSL certifikáty
   - Zkontrolujte, že DNS záznamy jsou správně nastaveny

## Vysvětlení proměnných prostředí

1. **Povinné proměnné**:
   - `OPENAI_API_KEY`: Váš OpenAI API klíč
   - `NEXT_PUBLIC_BACKEND_URL`: URL backendu (např. https://api.vase-domena.com)

2. **Volitelné proměnné** (mají výchozí hodnoty):
   - `MODEL_NAME`: OpenAI model (výchozí: gpt-4-1106-preview)
   - `MAX_TOKENS`: Maximální počet tokenů (výchozí: 2000)
   - `TEMPERATURE`: Teplota pro generování (výchozí: 0.3)
   - `DEBUG`: Debug mód (výchozí: False v produkci)
   - `MKN11_EXCEL_PATH`: Cesta k Excel souboru (výchozí: /app/data/mkn-11-terminologie-202403.xlsx)

3. **Automaticky nastavené Coolify**:
   - Interní směrování mezi službami
   - SSL certifikáty
   - Porty a síťování

## Ověření nasazení

1. **Backend kontrola**:
   - Otevřete `https://api.vase-domena.com/health`
   - Měli byste vidět odpověď o stavu služby

2. **Frontend kontrola**:
   - Otevřete `https://vase-domena.com`
   - Aplikace by měla být plně funkční

## Řešení problémů

1. **Backend není dostupný**:
   - Zkontrolujte logy v Coolify
   - Ověřte `OPENAI_API_KEY`
   - Zkontrolujte DNS záznam pro `api.vase-domena.com`

2. **Frontend není dostupný**:
   - Zkontrolujte logy v Coolify
   - Ověřte `NEXT_PUBLIC_BACKEND_URL`
   - Zkontrolujte DNS záznam pro `vase-domena.com`

3. **Problémy s buildem**:
   - V Coolify rozhraní zkuste "Rebuild"
   - Zkontrolujte build logy pro chyby

## Monitoring

- Coolify poskytuje monitoring a logy pro obě služby
- Health check endpointy jsou automaticky kontrolovány
- Metriky jsou dostupné v Coolify dashboardu