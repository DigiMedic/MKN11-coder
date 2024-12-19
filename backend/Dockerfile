FROM python:3.11-slim

WORKDIR /app

# Instalace systémových závislostí
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Kopírování a instalace Python závislostí
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopírování zdrojového kódu
COPY . .

# Vytvoření non-root uživatele
RUN adduser --system --group appuser
USER appuser

# Expose port
EXPOSE 8000

# Spuštění aplikace
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
