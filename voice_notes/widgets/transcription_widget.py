"""
Transcription Widget
"""
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QPushButton, QMessageBox, QFileDialog, QProgressBar
from PyQt6.QtCore import QThread, pyqtSignal, QTimer
from ..core.transcription import TranscriptionManager

class TranscriptionWorker(QThread):
    """Worker thread for transcription operations"""
    progress_updated = pyqtSignal(str)  # Progress message
    finished_success = pyqtSignal(Path)  # Success with words path
    finished_error = pyqtSignal(str)     # Error message

    def __init__(self, audio_path: Path, model: str, transcription_manager: TranscriptionManager):
        super().__init__()
        self.audio_path = audio_path
        self.model = model
        self.transcription_manager = transcription_manager

    def run(self):
        """Run transcription in background thread"""
        try:
            self.progress_updated.emit("🎙️ Starting transcription...")

            # Run the transcription
            success = self.transcription_manager.transcribe_audio(self.audio_path, self.model)

            if success:
                self.progress_updated.emit("📝 Processing results...")

                # Check for words.json file
                words_path = self.transcription_manager.words_path_for(self.audio_path)

                # Wait a bit for file to be written (in case it's still being written)
                import time
                max_wait = 10  # seconds
                waited = 0
                while not words_path.exists() and waited < max_wait:
                    time.sleep(0.5)
                    waited += 0.5
                    self.progress_updated.emit(f"⏳ Waiting for output file... ({waited:.1f}s)")

                if words_path.exists():
                    self.finished_success.emit(words_path)
                else:
                    self.finished_error.emit("Transcription completed but words.json file not found")
            else:
                self.finished_error.emit("Transcription failed")

        except Exception as e:
            self.finished_error.emit(f"Transcription error: {str(e)}")

class TranscriptionWidget(QWidget):
    """Transcription widget for AI-powered audio transcription"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize transcription manager
        self.transcription_manager = TranscriptionManager()
        self.current_audio_path = None
        self.worker = None  # Current transcription worker thread

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

        # Progress bar for transcription
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        self.progress_bar.setVisible(False)
        self.progress_bar.setObjectName("progress_bar")  # For QSS styling

        self.progress_label = QLabel("")
        self.progress_label.setVisible(False)
        self.progress_label.setObjectName("progress_label")  # For QSS styling

        status_section.addWidget(status_label)
        status_section.addWidget(self.words_status)
        status_section.addWidget(self.progress_bar)
        status_section.addWidget(self.progress_label)

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
        """Run Whisper transcription in background thread"""
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

        # Check if already running
        if self.worker and self.worker.isRunning():
            QMessageBox.information(self, "Already running", "Transcription is already in progress.")
            return

        model = self.model_combo.currentText()

        # Disable buttons during transcription
        self._set_transcription_enabled(False)

        # Show progress
        self.progress_bar.setVisible(True)
        self.progress_label.setVisible(True)
        self.progress_label.setText("🎙️ Starting transcription...")
        self._set_status_success("🔄 Transcription in progress...")

        # Create and start worker thread
        self.worker = TranscriptionWorker(self.current_audio_path, model, self.transcription_manager)
        self.worker.progress_updated.connect(self._on_progress_updated)
        self.worker.finished_success.connect(self._on_transcription_success)
        self.worker.finished_error.connect(self._on_transcription_error)
        self.worker.start()

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

    def _on_progress_updated(self, message: str):
        """Handle progress updates from worker thread"""
        self.progress_label.setText(message)

    def _on_transcription_success(self, words_path: Path):
        """Handle successful transcription completion"""
        # Hide progress
        self.progress_bar.setVisible(False)
        self.progress_label.setVisible(False)

        # Re-enable buttons
        self._set_transcription_enabled(True)

        # Load the words.json file
        try:
            self.load_words_json(words_path)
            QMessageBox.information(
                self, "Transcription Complete", f"Successfully transcribed and loaded {words_path.name}"
            )
        except Exception as e:
            self._set_status_error(f"⚠️ Transcription completed but failed to load words: {str(e)}")
            QMessageBox.warning(
                self, "Transcription", f"Completed, but failed to load words.json: {str(e)}"
            )

    def _on_transcription_error(self, error_message: str):
        """Handle transcription error"""
        # Hide progress
        self.progress_bar.setVisible(False)
        self.progress_label.setVisible(False)

        # Re-enable buttons
        self._set_transcription_enabled(True)

        # Show error
        self._set_status_error(f"❌ {error_message}")
        QMessageBox.critical(self, "Transcription Error", error_message)

    def _set_transcription_enabled(self, enabled: bool):
        """Enable/disable transcription controls"""
        self.btn_transcribe.setEnabled(enabled)
        self.btn_load_words.setEnabled(enabled)
        self.model_combo.setEnabled(enabled)