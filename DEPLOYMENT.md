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
   - Přidejte proměnnou prostředí:
     ```
     OPENAI_API_KEY=váš-openai-api-klíč
     ```

   b) **Frontend služba**:
   - Vytvořte novou službu typu "Docker Service"
   - Zvolte váš Git repozitář
   - Nastavte build kontext na `/frontend`
   - Nastavte port na `3000`
   - Přidejte proměnnou prostředí:
     ```
     NEXT_PUBLIC_BACKEND_URL=https://api.vase-domena.com
     ```

2. **Nastavení domén**:
   - Pro backend: `api.vase-domena.com`
   - Pro frontend: `vase-domena.com`

3. **SSL/HTTPS**:
   - Coolify automaticky nastaví SSL certifikáty
   - Zkontrolujte, že DNS záznamy jsou správně nastaveny

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