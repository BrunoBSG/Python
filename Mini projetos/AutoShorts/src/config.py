import os
from pathlib import Path

from dotenv import load_dotenv

# ==================================================
# Carrega as variáveis do arquivo .env
# ==================================================

load_dotenv()

# ==================================================
# Diretórios do projeto
# ==================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOWNLOADS_DIR = PROJECT_ROOT / "downloads"
OUTPUT_DIR = PROJECT_ROOT / "output"
TEMP_DIR = PROJECT_ROOT / "temp"

# Cria as pastas caso não existam
DOWNLOADS_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)

# ==================================================
# Configuração da IA
# ==================================================

AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini").lower()

# ---------- OpenAI ----------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# ---------- Gemini ----------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# ==================================================
# Configuração dos Shorts
# ==================================================

MAX_SHORT_DURATION = 60
MIN_SHORT_DURATION = 30
NUMBER_OF_SHORTS = 5
print(f"AI_PROVIDER: {AI_PROVIDER}")
print(f"GEMINI_MODEL: {GEMINI_MODEL}")