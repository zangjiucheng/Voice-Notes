"""
Audio Player Widget
"""
from PyQt6.QtCore import Qt, QUrl, pyqtSignal
from PyQt6.QtGui import QAction, QKeySequence, QColor, QFont, QTextCharFormat, QTextCursor
from PyQt6.QtWidgets import (
    QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, 
    QToolButton, QLabel, QSlider, QComboBox, QTextEdit
)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QStyle
from ..utils.helpers import hhmmss
from ..core.transcription import TranscriptionManager
from ..core.translation import TranslationManager
from ..core.config import DEFAULT_TRANSLATION_TARGET

class ClickableTextEdit(QTextEdit):
    word_selected = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton:
            cursor = self.cursorForPosition(event.pos())
            cursor.select(QTextCursor.SelectionType.WordUnderCursor)
            self.setTextCursor(cursor)
            selected_text = cursor.selectedText().strip()
            if selected_text:
                self.word_selected.emit(selected_text)

class PlayerWidget(QGroupBox):
    position_changed = pyqtSignal(int)  # position in seconds
    
    def __init__(self, parent=None):
        super().__init__("Player", parent)
        self.setProperty("class", "glass")
        self.setMinimumSize(400, 180)  # Ensure minimum size for player controls
        
        # Media player setup
        self.player = QMediaPlayer(self)
        self.audio_out = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_out)
        self.audio_out.setVolume(0.8)
        
        # Transcription setup
        self.transcription_manager = TranscriptionManager()
        self.current_audio_path = None
        
        # Translation setup
        self.translation_manager = TranslationManager(target_lang=DEFAULT_TRANSLATION_TARGET)
        
        self._setup_ui()
        self._connect_signals()
        
        self._updating_slider = False
    
    def set_translation_target(self, target_lang: str):
        """Set the target language for translation"""
        self.translation_manager.set_target_language(target_lang)
    
    def get_translation_target(self) -> str:
        """Get the current target language for translation"""
        return self.translation_manager.target_lang
    
    def _setup_ui(self):
        # Title and play button
        self.lbl_title = QLabel("No file selected")
        self.lbl_title.setObjectName("lbl_title")  # For QSS styling
        
        self.btn_play = QToolButton()
        self.btn_play.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.btn_play.setObjectName("btn_play")  # For QSS styling
        
        # Position slider and time label
        self.position_slider = QSlider(Qt.Orientation.Horizontal)
        self.position_slider.setRange(0, 1000)
        self.position_slider.setMinimumWidth(200)  # Ensure minimum slider width
        self.position_slider.setObjectName("position_slider")  # For QSS styling
        
        self.lbl_time = QLabel("00:00 / 00:00")
        self.lbl_time.setObjectName("lbl_time")  # For QSS styling
        
        # Transcription display
        self.transcription_display = ClickableTextEdit()
        self.transcription_display.setMaximumHeight(500)
        self.transcription_display.setMinimumHeight(50)
        self.transcription_display.setPlaceholderText("Load an audio file and transcribe it in the Notes tab to see synchronized text here...")
        self.transcription_display.setObjectName("transcription_display")  # For QSS styling
        
        # Translation display
        self.translation_label = QLabel("Double click a word to see its translation")
        self.translation_label.setObjectName("translation_label")  # For QSS styling
        self.translation_label.setWordWrap(True)
        self.translation_label.setMaximumHeight(100)
        self.translation_label.setMinimumHeight(30)
        
        # Speed and volume controls
        self.speed_combo = QComboBox()
        self.speed_combo.addItems(["0.75×", "1.0×", "1.25×", "1.5×", "2.0×"])
        self.speed_combo.setCurrentIndex(1)
        
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(80)
        self.volume_slider.setMinimumWidth(100)  # Ensure minimum slider width
        self.volume_slider.setObjectName("volume_slider")  # For QSS styling
        
        # Enhanced layout with better spacing
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)
        
        # Top section: play button and title
        top_layout = QHBoxLayout()
        top_layout.setSpacing(12)
        top_layout.addWidget(self.btn_play)
        top_layout.addWidget(self.lbl_title, 1)
        
        # Middle section: position slider and time
        middle_layout = QHBoxLayout()
        middle_layout.setSpacing(12)
        middle_layout.addWidget(self.position_slider, 1)
        middle_layout.addWidget(self.lbl_time)
        
        # Transcription section
        transcription_label = QLabel("📝 Transcription")
        transcription_label.setFixedHeight(35)
        transcription_label.setObjectName("transcription_label")  # For QSS styling
        
        translation_label = QLabel("🌐 Translation")
        translation_label.setFixedHeight(35)
        translation_label.setObjectName("translation_label_header")  # For QSS styling
        
        transcription_layout = QVBoxLayout()
        transcription_layout.setSpacing(6)
        transcription_layout.addWidget(transcription_label)
        transcription_layout.addWidget(self.transcription_display)
        transcription_layout.addWidget(translation_label)
        transcription_layout.addWidget(self.translation_label)
        
        # Bottom section: speed and volume controls
        speed_label = QLabel("🏃 Speed")
        speed_label.setObjectName("speed_label")  # For QSS styling
        
        volume_label = QLabel("🔊 Volume")
        volume_label.setObjectName("volume_label")  # For QSS styling
        
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(12)
        bottom_layout.addWidget(speed_label)
        bottom_layout.addWidget(self.speed_combo)
        bottom_layout.addSpacing(20)
        bottom_layout.addWidget(volume_label)
        bottom_layout.addWidget(self.volume_slider, 1)
        
        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(transcription_layout)
        layout.addLayout(bottom_layout)
        layout.addStretch(1)
        
        self.setLayout(layout)
    
    def _connect_signals(self):
        self.btn_play.clicked.connect(self.toggle_play)
        self.position_slider.sliderMoved.connect(self.seek)
        self.speed_combo.currentIndexChanged.connect(self.apply_speed)
        self.volume_slider.valueChanged.connect(
            lambda v: self.audio_out.setVolume(v / 100.0)
        )
        
        # Player signals
        self.player.positionChanged.connect(self._on_position_changed)
        self.player.durationChanged.connect(self._on_duration_changed)
        self.player.playbackStateChanged.connect(self._on_state_changed)
        
        # Transcription signals
        self.transcription_display.word_selected.connect(self.translate_word)
    
    def load_audio(self, file_path: str):
        """Load audio file into player"""
        from pathlib import Path
        from ..core.audio_library import AudioLibrary
        
        self.current_audio_path = Path(file_path)
        display_name = AudioLibrary.format_display_name(self.current_audio_path)
        self.lbl_title.setText(display_name)
        self.lbl_title.setObjectName("lbl_title_loaded")  # Change object name for loaded state styling
        
        # Clear transcription display immediately when loading new audio
        self.transcription_display.setPlainText("")
        self.transcription_manager.words_index = None
        
        # Clear translation
        self.translation_label.setText("")
        
        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.player.stop()
        self.btn_play.setIcon(
            self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        )
        
        # Load transcription if available
        self._load_transcription()
    
    def refresh_transcription(self):
        """Refresh the transcription display"""
        self._load_transcription()
    
    def _load_transcription(self):
        """Load transcription data for current audio file"""
        if not self.current_audio_path:
            self.transcription_display.setPlainText("")
            return
        
        words_path = self.transcription_manager.words_path_for(self.current_audio_path)
        if words_path.exists():
            try:
                self.transcription_manager.load_words_json(words_path)
                self._display_transcription()
            except Exception as e:
                self.transcription_display.setPlainText(f"Error loading transcription: {str(e)}")
        else:
            self.transcription_display.setHtml("""
                <div style="text-align: center; color: #6b7280; font-style: italic; padding: 10px;">
                    <p style="margin: 0; font-size: 14px;">🎙️ No transcription available</p>
                    <p style="margin: 5px 0 0 0; font-size: 12px;">Switch to the Notes tab and click "🤖 Start Transcription" to generate word-level timestamps for this audio.</p>
                </div>
            """)
    
    def translate_word(self, word: str):
        """Translate the selected word and display it"""
        if not self.translation_manager.is_available():
            self.translation_label.setText("Translation not available (deep-translator not installed)")
            return
        
        if not word.strip():
            self.translation_label.setText("")
            return
        
        try:
            # Translate to English (assuming the transcription is in another language)
            result = self.translation_manager.translate_text(word)
            if result:
                self.translation_label.setText(f"{word} → {result}")
            else:
                self.translation_label.setText("")
        except Exception as e:
            self.translation_label.setText(f"Translation failed: {str(e)}")
    
    def _display_transcription(self):
        """Display the full transcription text"""
        if not self.transcription_manager.words_index:
            self.transcription_display.setPlainText("No transcription data available.")
            return
        
        # Build the full text from words
        words_text = " ".join(word.get("word", "") for word in self.transcription_manager.words_index if word.get("word"))
        self.transcription_display.setPlainText(words_text)
    
    def _highlight_current_word(self, current_time: float):
        """Highlight the current word based on playback position"""
        if not self.transcription_manager.words_index or not self.current_audio_path:
            return
        
        # Find the current word
        current_word_index = -1
        for i, word in enumerate(self.transcription_manager.words_index):
            start_time = word.get("start", 0)
            end_time = word.get("end", start_time + 0.1)
            if start_time <= current_time <= end_time:
                current_word_index = i
                break
        
        if current_word_index >= 0:
            # Build the full text and track word positions
            words = [word.get("word", "") for word in self.transcription_manager.words_index]
            full_text = " ".join(words)
            self.transcription_display.setPlainText(full_text)

            # Calculate the exact position of the current word
            word_start = 0
            for i in range(current_word_index):
                word_start += len(words[i]) + 1  # +1 for space

            word_length = len(words[current_word_index])

            # Highlight the current word with yellow background (no cursor selection)
            cursor = self.transcription_display.textCursor()
            cursor.setPosition(word_start)
            cursor.setPosition(word_start + word_length, QTextCursor.MoveMode.KeepAnchor)

            format_highlight = QTextCharFormat()
            format_highlight.setBackground(QColor(255, 255, 0, 120))  # Light yellow background
            format_highlight.setForeground(QColor(0, 0, 0))  # Keep black text
            cursor.mergeCharFormat(format_highlight)

            # Don't set the text cursor to avoid visible selection

            # Ensure the highlighted word is visible and centered
            self.transcription_display.ensureCursorVisible()

            # Center the cursor in the viewport
            scrollbar = self.transcription_display.verticalScrollBar()
            if scrollbar:
                # Calculate the center position
                cursor_rect = self.transcription_display.cursorRect(cursor)
                viewport_height = self.transcription_display.viewport().height()
                center_pos = cursor_rect.top() - (viewport_height // 2) + (cursor_rect.height() // 2)
                scrollbar.setValue(scrollbar.value() + center_pos)
    
    def toggle_play(self):
        """Toggle play/pause"""
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()
    
    def seek(self, slider_val: int):
        """Seek to position based on slider value"""
        if self.player.duration() > 0:
            position = int(slider_val / 1000 * self.player.duration())
            self.player.setPosition(position)
    
    def apply_speed(self):
        """Apply playback speed"""
        speed_text = self.speed_combo.currentText()
        factor = float(speed_text.replace("×", ""))
        self.player.setPlaybackRate(factor)
    
    def current_seconds(self) -> float:
        """Get current playback position in seconds"""
        return self.player.position() / 1000.0
    
    def _on_position_changed(self, pos_ms: int):
        """Handle player position change"""
        dur_ms = self.player.duration()
        self.lbl_time.setText(f"{hhmmss(pos_ms)} / {hhmmss(dur_ms)}")
        
        if dur_ms > 0 and not self._updating_slider:
            self.position_slider.blockSignals(True)
            self.position_slider.setValue(int(1000 * pos_ms / dur_ms))
            self.position_slider.blockSignals(False)
        
        # Highlight current word in transcription
        current_time = pos_ms / 1000.0
        self._highlight_current_word(current_time)
        
        # Emit position in seconds
        self.position_changed.emit(int(pos_ms / 1000))
    
    def _on_duration_changed(self, dur_ms: int):
        """Handle duration change"""
        self._on_position_changed(self.player.position())
    
    def _on_state_changed(self, state):
        """Handle playback state change"""
        if state == QMediaPlayer.PlaybackState.PlayingState:
            icon = QStyle.StandardPixmap.SP_MediaPause
        else:
            icon = QStyle.StandardPixmap.SP_MediaPlay
        
        self.btn_play.setIcon(self.style().standardIcon(icon))
    
    def jump_to_time(self, seconds: float):
        """Jump to specific time in seconds"""
        if self.player.duration() > 0:
            self.player.setPosition(int(seconds * 1000))
            if self.player.playbackState() != QMediaPlayer.PlaybackState.PlayingState:
                self.player.play()