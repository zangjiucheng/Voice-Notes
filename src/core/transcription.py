"""
Transcription Manager - Handles audio transcription
"""
import json
from pathlib import Path
from typing import List, Dict, Optional
from ..core.config import OUT_DIR

# Optional transcription hook
from .transcribe import transcribe as whisper_transcribe

class TranscriptionManager:
    def __init__(self):
        self.words_index: Optional[List[Dict]] = None
    
    @staticmethod
    def words_path_for(audio_path: Path) -> Path:
        return OUT_DIR / f"{audio_path.stem}.words.json"
    
    def transcribe_audio(self, audio_path: Path, model: str = "small") -> bool:
        """Transcribe audio file using Whisper"""
        if whisper_transcribe is None:
            raise Exception("transcribe.py module not available")
        
        try:
            whisper_transcribe(str(audio_path), str(OUT_DIR), model)
            return True
        except Exception as e:
            raise Exception(f"Transcription failed: {str(e)}")
    
    def load_words_json(self, words_path: Path) -> bool:
        """Load words index from JSON file"""
        try:
            data = json.loads(words_path.read_text(encoding="utf-8"))
            if isinstance(data, list):
                self.words_index = data
                return True
            else:
                raise ValueError("Invalid words.json structure")
        except Exception as e:
            raise Exception(f"Failed to load words.json: {str(e)}")
    
    def get_words_count(self) -> int:
        """Get number of words in the index"""
        return len(self.words_index) if self.words_index else 0
    
    def has_transcription_module(self) -> bool:
        """Check if transcription module is available"""
        return whisper_transcribe is not None