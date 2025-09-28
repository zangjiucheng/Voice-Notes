"""
Application Constants and Configuration
"""
from pathlib import Path

# Application settings
APP_NAME = "Voice Notes"

# Directories
BASE_DIR = Path.home() / ".voice-notes"
BASE_DIR.mkdir(parents=True, exist_ok=True)

LIB_DIR = BASE_DIR / "recordings"
LIB_DIR.mkdir(parents=True, exist_ok=True)

OUT_DIR = BASE_DIR / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Supported audio file extensions
AUDIO_EXTS = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".aiff", ".aif"}

# Recording settings
DEFAULT_SAMPLERATE = 48000
DEFAULT_CHANNELS = 1

# Translation settings
# Set the default target language for translation (e.g., 'en' for English, 'zh-CN' for Chinese, 'es' for Spanish)
DEFAULT_TRANSLATION_TARGET = "en"

TRANSLATION_OPTIONS = {
    "en": "English",
    "es": "Spanish", 
    "fr": "French",
    "de": "German",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean", 
    "ru": "Russian",
    "pt": "Portuguese",
    "it": "Italian",
    "ar": "Arabic",
    "hi": "Hindi"
}