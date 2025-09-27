#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Voice Notes Application - Main Entry Point
"""
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.app import VoiceNotesApp

def main():
    app = VoiceNotesApp()
    sys.exit(app.run())

if __name__ == "__main__":
    main()