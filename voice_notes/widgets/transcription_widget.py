"""
Transcription Widget
"""
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QPushButton, QMessageBox, QFileDialog
from ..core.transcription import TranscriptionManager

class TranscriptionWidget(QWidget):
    """Transcription widget for AI-powered audio transcription"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize transcription manager
        self.transcription_manager = TranscriptionManager()
        self.current_audio_path = None

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        """Setup the transcription interface"""
        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)

        # Transcription header
        trans_header = QLabel("🤖 AI Transcription")
        trans_header.setObjectName("trans_header")  # For QSS styling

        trans_subheader = QLabel("Generate word-level timestamps using OpenAI Whisper")
        trans_subheader.setObjectName("trans_subheader")  # For QSS styling

        # Whisper model selection
        model_section = QVBoxLayout()
        model_section.setSpacing(10)

        model_label = QLabel("⚙️ Whisper Model Size")
        model_label.setObjectName("model_label")  # For QSS styling

        model_help = QLabel("Larger models are more accurate but slower")
        model_help.setObjectName("model_help")  # For QSS styling

        self.model_combo = QComboBox()
        self.model_combo.addItems(["tiny", "base", "small", "medium", "large"])
        self.model_combo.setCurrentText("small")
        self.model_combo.setMinimumWidth(120)

        model_section.addWidget(model_label)
        model_section.addWidget(model_help)
        model_section.addWidget(self.model_combo)

        # Action buttons
        button_section = QVBoxLayout()
        button_section.setSpacing(14)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(14)

        self.btn_transcribe = QPushButton("🎙️ Start Transcription")
        self.btn_load_words = QPushButton("📁 Load Existing words.json")

        button_layout.addWidget(self.btn_transcribe)
        button_layout.addWidget(self.btn_load_words)
        button_section.addLayout(button_layout)

        # Status display
        status_section = QVBoxLayout()
        status_section.setSpacing(12)

        status_label = QLabel("📊 Transcription Status")
        status_label.setObjectName("status_label")  # For QSS styling

        self.words_status = QLabel("No words data loaded")
        self.words_status.setObjectName("words_status")  # For QSS styling

        status_section.addWidget(status_label)
        status_section.addWidget(self.words_status)

        # Add sections to layout
        layout.addWidget(trans_header)
        layout.addWidget(trans_subheader)
        layout.addSpacing(12)
        layout.addLayout(model_section)
        layout.addSpacing(20)
        layout.addLayout(button_section)
        layout.addSpacing(20)
        layout.addLayout(status_section)
        layout.addStretch(1)

        self.setLayout(layout)

    def _connect_signals(self):
        """Connect widget signals"""
        self.btn_transcribe.clicked.connect(self.run_transcription)
        self.btn_load_words.clicked.connect(self.load_words_dialog)

    def set_current_audio(self, audio_path: Path):
        """Set the current audio file path"""
        self.current_audio_path = audio_path

    def run_transcription(self):
        """Run Whisper transcription"""
        if not self.current_audio_path:
            QMessageBox.information(
                self, "No file", "Open or record an audio first."
            )
            return

        if not self.transcription_manager.has_transcription_module():
            QMessageBox.warning(
                self, "Missing transcribe()",
                "Put transcribe.py with transcribe(audio_path, out_dir, model_size)."
            )
            return

        model = self.model_combo.currentText()

        try:
            self.transcription_manager.transcribe_audio(self.current_audio_path, model)

            # Try to load words.json
            words_path = self.transcription_manager.words_path_for(self.current_audio_path)
            if words_path.exists():
                self.load_words_json(words_path)
                QMessageBox.information(
                    self, "Transcription Complete", f"Successfully transcribed and loaded {words_path.name}"
                )
            else:
                self._set_status_error("⚠️ Transcription completed but no words file found")
                QMessageBox.information(
                    self, "Transcription", "Finished, but words.json not found."
                )

        except Exception as e:
            QMessageBox.critical(self, "Transcription Error", str(e))

    def load_words_dialog(self):
        """Load words.json via file dialog"""
        from ..core.config import OUT_DIR

        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select words.json", str(OUT_DIR), "JSON (*.json)"
        )

        if file_path:
            self.load_words_json(Path(file_path))

    def load_words_json(self, words_path: Path):
        """Load words index from JSON file"""
        try:
            self.transcription_manager.load_words_json(words_path)
            count = self.transcription_manager.get_words_count()
            self._set_status_success(f"✅ Loaded {count:,} words with timestamps")

        except Exception as e:
            self._set_status_error(f"❌ Error loading words: {str(e)}")
            QMessageBox.critical(self, "words.json Error", str(e))

    def _set_status_success(self, message: str):
        """Set success status message"""
        self.words_status.setText(message)

    def _set_status_error(self, message: str):
        """Set error status message"""
        self.words_status.setText(message)