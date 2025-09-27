"""
Application Constants and Configuration
"""
from pathlib import Path

# Application settings
APP_NAME = "Voice Notes"

# Directories
LIB_DIR = Path("recordings")
LIB_DIR.mkdir(exist_ok=True)

OUT_DIR = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)

# Supported audio file extensions
AUDIO_EXTS = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".aiff", ".aif"}

# Recording settings
DEFAULT_SAMPLERATE = 48000
DEFAULT_CHANNELS = 1

# Translation settings
# Set the default target language for translation (e.g., 'en' for English, 'zh-CN' for Chinese, 'es' for Spanish)
DEFAULT_TRANSLATION_TARGET = "en"