import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")

    chroma_db_path: str = os.getenv("CHROMA_DB_PATH", "./ai_immigration_agent/.chroma")
    chroma_collection_kb: str = os.getenv("CHROMA_COLLECTION_KB", "kb")
    chroma_collection_plans: str = os.getenv("CHROMA_COLLECTION_PLANS", "plans")

    page_registry_path: str = os.getenv("PAGE_REGISTRY_PATH", "./ai_immigration_agent/data/page_registry.json")

    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))

settings = Settings()
