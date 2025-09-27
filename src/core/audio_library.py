"""
Audio Library Manager - Handles audio file operations
"""
import time
from pathlib import Path
from typing import List
from ..core.config import LIB_DIR, AUDIO_EXTS

class AudioLibrary:
    @staticmethod
    def get_audio_files(search_query: str = "") -> List[Path]:
        """Get list of audio files, optionally filtered by search query"""
        files = sorted(
            [p for p in LIB_DIR.iterdir() if p.suffix.lower() in AUDIO_EXTS],
            key=lambda p: p.stat().st_mtime, 
            reverse=True
        )
        
        if search_query:
            query = search_query.strip().lower()
            files = [f for f in files if query in f.stem.lower()]
        
        return files
    
    @staticmethod
    def import_audio_files(file_paths: List[str]) -> List[Path]:
        """Import audio files to the library directory"""
        imported_files = []
        
        for file_path in file_paths:
            src = Path(file_path)
            dst = LIB_DIR / src.name
            
            # Handle duplicate names
            if dst.exists():
                dst = LIB_DIR / f"{src.stem}_{int(time.time())}{src.suffix}"
            
            dst.write_bytes(src.read_bytes())
            imported_files.append(dst)
        
        return imported_files
    
    @staticmethod
    def generate_recording_path() -> Path:
        """Generate a path for a new recording"""
        name = time.strftime("Recording %b %d, %Y at %I.%M %p")
        return LIB_DIR / f"{name}.wav"
    
    @staticmethod
    def delete_audio_file(file_path: Path) -> None:
        """Delete an audio file and its associated files (notes, transcription, etc.)"""
        from ..core.config import OUT_DIR
        
        if not file_path.exists():
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        
        base_name = file_path.stem
        
        # Delete the main audio file
        file_path.unlink()
        
        # Delete associated files in outputs directory
        associated_patterns = [
            f"{base_name}.txt",          # Notes file
            f"{base_name}.segments.vtt", # Segments file
            f"{base_name}.words.json"    # Words file
        ]
        
        for pattern in associated_patterns:
            associated_file = OUT_DIR / pattern
            if associated_file.exists():
                associated_file.unlink()
    
    @staticmethod
    def format_display_name(file_path: Path) -> str:
        """Format filename for better readability in the UI"""
        name = file_path.stem
        
        # Handle new format: "Recording Jan 01, 2025 at 02.30 PM"
        if name.startswith("Recording ") and " at " in name:
            return name.replace("Recording ", "").replace(".", ":")
        
        # Handle old format: "Recording 2025-09-26 02-03-18"
        if name.startswith("Recording ") and len(name.split("-")) >= 6:
            parts = name.replace("Recording ", "").split("-")
            if len(parts) >= 6:
                year, month, day, hour, minute, second = parts[:6]
                try:
                    # Convert to readable format
                    import datetime
                    dt = datetime.datetime(int(year), int(month), int(day), 
                                         int(hour), int(minute), int(second))
                    return dt.strftime("%b %d, %Y at %I:%M %p")
                except ValueError:
                    pass
        
        # Fallback: return original name with some formatting
        return name.replace("-", " ").replace("_", " ").title()