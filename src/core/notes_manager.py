"""
Notes Manager - Handles note storage and retrieval
"""
import json
from pathlib import Path
from typing import List, Dict, Optional
from ..core.config import OUT_DIR

class NotesManager:
    def __init__(self):
        self.notes: List[Dict] = []
    
    @staticmethod
    def notes_path_for(audio_path: Path) -> Path:
        return OUT_DIR / f"{audio_path.stem}.notes.json"
    
    @staticmethod
    def words_path_for(audio_path: Path) -> Path:
        return OUT_DIR / f"{audio_path.stem}.words.json"
    
    def load_notes(self, audio_path: Path) -> List[Dict]:
        """Load notes for the given audio file"""
        self.notes = []
        notes_path = self.notes_path_for(audio_path)
        if notes_path.exists():
            try:
                self.notes = json.loads(notes_path.read_text(encoding="utf-8"))
            except Exception:
                self.notes = []
        return self.notes
    
    def save_notes(self, audio_path: Path):
        """Save notes for the given audio file"""
        notes_path = self.notes_path_for(audio_path)
        notes_path.write_text(
            json.dumps(self.notes, ensure_ascii=False, indent=2), 
            encoding="utf-8"
        )
    
    def add_note(self, text: str, anchor_seconds: Optional[float] = None):
        """Add a new note"""
        note = {"text": text, "anchor_seconds": anchor_seconds}
        self.notes.append(note)
        return note
    
    def delete_note(self, index: int):
        """Delete note at given index"""
        if 0 <= index < len(self.notes):
            return self.notes.pop(index)
        return None
    
    @staticmethod
    def note_to_line(note: Dict) -> str:
        """Convert note dict to display string"""
        anchor = note.get("anchor_seconds")
        prefix = f"[{anchor:.2f}s] " if isinstance(anchor, (int, float)) else ""
        text = note.get("text", "").replace("\n", " ")
        return prefix + text[:120]
    
    def nearest_word_time(self, words_index: List[Dict], target: float) -> Optional[float]:
        """Find the nearest word timestamp to target time"""
        if not words_index:
            return None
        
        best = None
        best_distance = float('inf')
        
        for word in words_index:
            start_time = word.get("start")
            if start_time is None:
                continue
            
            distance = abs(start_time - target)
            if distance < best_distance:
                best_distance = distance
                best = start_time
        
        return best