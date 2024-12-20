"""
Konfigurace aplikace s pevně nastavenými hodnotami.
"""

from typing import Dict, Any
import os
from dotenv import load_dotenv

# Načtení .env souboru
load_dotenv()

class Settings:
    # API URLs
    BACKEND_URL: str = os.getenv("BACKEND_URL", "http://localhost:8000")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    # Datové soubory
    MKN11_EXCEL_PATH: str = os.getenv("MKN11_EXCEL_PATH", "/app/data/mkn-11-terminologie-202403.xlsx")

    # Nastavení prostředí
    DEBUG: bool = os.getenv("DEBUG", True)
    NODE_ENV: str = os.getenv("NODE_ENV", "development")

    # API konfigurace
    API_V1_PREFIX: str = os.getenv("API_V1_PREFIX", "/api/v1")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "MKN-11 Asistované Kódování")
    VERSION: str = os.getenv("VERSION", "1.0.0")
    DESCRIPTION: str = os.getenv("DESCRIPTION", """
API pro asistované kódování diagnóz podle standardu MKN-11 s využitím umělé inteligence.
""")

    # CORS nastavení
    ALLOWED_HOSTS: list[str] = os.getenv("ALLOWED_HOSTS", [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
    ])

    # Cache nastavení
    CACHE_TTL: int = os.getenv("CACHE_TTL", 60 * 60)  # 1 hodina
    MAX_CACHE_SIZE: int = os.getenv("MAX_CACHE_SIZE", 1000)

    # Limity API
    RATE_LIMIT_PER_MINUTE: int = os.getenv("RATE_LIMIT_PER_MINUTE", 60)
    MAX_REQUEST_SIZE_MB: int = os.getenv("MAX_REQUEST_SIZE_MB", 10)

    # Kontrola povinných proměnných
    @classmethod
    def validate(cls):
        if not cls.BACKEND_URL:
            raise ValueError(
                "Chybí BACKEND_URL v .env souboru. "
                "Prosím nastavte URL backendu."
            )
        if not cls.FRONTEND_URL:
            raise ValueError(
                "Chybí FRONTEND_URL v .env souboru. "
                "Prosím nastavte URL frontendu."
            )

settings = Settings()
settings.validate()

def get_settings() -> Dict[str, Any]:
    """
    Vrátí všechna nastavení jako slovník.
    """
    return {
        "backend_url": settings.BACKEND_URL,
        "frontend_url": settings.FRONTEND_URL,
        "mkn11_excel_path": settings.MKN11_EXCEL_PATH,
        "debug": settings.DEBUG,
        "node_env": settings.NODE_ENV,
        "api_v1_prefix": settings.API_V1_PREFIX,
        "project_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "allowed_hosts": settings.ALLOWED_HOSTS,
        "cache_ttl": settings.CACHE_TTL,
        "max_cache_size": settings.MAX_CACHE_SIZE,
        "rate_limit_per_minute": settings.RATE_LIMIT_PER_MINUTE,
        "max_request_size_mb": settings.MAX_REQUEST_SIZE_MB,
    }
