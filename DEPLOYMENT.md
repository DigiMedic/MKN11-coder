# Nasazení MKN-11 Aplikace

Tento dokument popisuje postup nasazení aplikace MKN-11 Asistované Kódování pomocí Coolify.

## Předpoklady

- Přístup k Coolify instanci
- OpenAI API klíč
- Doména pro frontend a backend (volitelné)

## Kroky Nasazení

### 1. Příprava Proměnných Prostředí

Vytvořte následující proměnné prostředí v Coolify:

```env
# OpenAI API klíč (povinný)
OPENAI_API_KEY=váš-api-klíč

# URL konfigurace
BACKEND_URL=http://mkn11backend.vaše-doména.com
FRONTEND_URL=http://mkn11frontend.vaše-doména.com

# Prostředí
NODE_ENV=production
DEBUG=False

# API konfigurace
API_V1_PREFIX=/api/v1
PROJECT_NAME=MKN-11 Asistované Kódování
VERSION=1.0.0

# CORS
ALLOWED_HOSTS=http://mkn11frontend.vaše-doména.com

# Cache a limity
CACHE_TTL=3600
MAX_CACHE_SIZE=1000
RATE_LIMIT_PER_MINUTE=60
MAX_REQUEST_SIZE_MB=10

# OpenAI konfigurace
MODEL_NAME=gpt-4-1106-preview
MAX_TOKENS=2000
TEMPERATURE=0.3

# Data
MKN11_EXCEL_PATH=/app/data/mkn-11-terminologie-202403.xlsx
```

### 2. Nasazení Backend Služby

1. V Coolify vytvořte novou službu pro backend
2. Nastavte build kontext na `/backend`
3. Použijte `Dockerfile.prod` jako build soubor
4. Nastavte port na 8000
5. Přidejte všechny proměnné prostředí

### 3. Nasazení Frontend Služby

1. V Coolify vytvořte novou službu pro frontend
2. Nastavte build kontext na `/frontend`
3. Použijte `Dockerfile.prod` jako build soubor
4. Nastavte port na 3000
5. Přidejte následující proměnné prostředí:
   ```env
   NODE_ENV=production
   NEXT_PUBLIC_BACKEND_URL=http://mkn11backend.vaše-doména.com
   NEXT_PUBLIC_URL=http://mkn11frontend.vaše-doména.com
   ```

### 4. Nastavení Domén

1. Pro backend službu nastavte doménu: `mkn11backend.vaše-doména.com`
2. Pro frontend službu nastavte doménu: `mkn11frontend.vaše-doména.com`

### 5. SSL Certifikáty

Coolify automaticky zajistí SSL certifikáty pomocí Let's Encrypt.

### 6. Monitoring

1. Zkontrolujte logy obou služeb
2. Ověřte, že healthcheck endpointy jsou dostupné:
   - Backend: `http://mkn11backend.vaše-doména.com/health`
   - Frontend: `http://mkn11frontend.vaše-doména.com`

## Řešení Problémů

### CORS Chyby

Pokud se vyskytnou CORS chyby:
1. Ověřte, že `ALLOWED_HOSTS` obsahuje správnou URL frontendu
2. Zkontrolujte, že `NEXT_PUBLIC_BACKEND_URL` je správně nastaveno ve frontendu

### 404 Chyby na Frontendu

Pokud se vyskytnou 404 chyby:
1. Ověřte, že `NEXT_PUBLIC_URL` je správně nastaveno
2. Zkontrolujte, že Next.js aplikace má správně nakonfigurované `basePath` a `assetPrefix`

### Problémy s API Požadavky

1. Ověřte, že `NEXT_PUBLIC_BACKEND_URL` směřuje na správnou URL backendu
2. Zkontrolujte, že backend je dostupný a běží
3. Ověřte logy backendu pro případné chyby

## Kontakt

Pro technickou podporu kontaktujte: petr@sovadina.com