"""
Translation Manager - Handles text translation
"""
from typing import Optional

try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False

class TranslationManager:
    def __init__(self, source_lang: str = 'auto', target_lang: str = 'en'):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator(source=source_lang, target=target_lang) if TRANSLATOR_AVAILABLE else None
    
    def set_target_language(self, target_lang: str):
        """Set the target language for translation"""
        self.target_lang = target_lang
        if self.translator:
            self.translator = GoogleTranslator(source=self.source_lang, target=target_lang)
    
    def translate_text(self, text: str) -> Optional[str]:
        """Translate the given text"""
        if not self.translator or not text.strip():
            return None
        
        try:
            return self.translator.translate(text)
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")
    
    def is_available(self) -> bool:
        """Check if translation is available"""
        return self.translator is not None