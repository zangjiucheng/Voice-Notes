"""
Utility Functions
"""
import re
from typing import Optional

def hhmmss(ms: int) -> str:
    """Convert milliseconds to HH:MM:SS or MM:SS format"""
    if ms < 0:
        ms = 0
    
    s = ms // 1000
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"

def extract_time_from_text(text: str) -> Optional[float]:
    """Extract time anchor from text like [[123.45]]"""
    match = re.search(r"\[\[\s*([0-9]+(?:\.[0-9]+)?)\s*\]\]", text)
    if match:
        return float(match.group(1))
    return None

def parse_note_time(note_line: str) -> Optional[float]:
    """Parse time from note line like '[123.45s] note text'"""
    match = re.match(r"\[(\d+(?:\.\d+)?)s\]\s+", note_line)
    if match:
        return float(match.group(1))
    return None