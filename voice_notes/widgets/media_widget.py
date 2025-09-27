"""
Media Widget - Combined Player, Recorder, and Transcription in Tabs
"""
from pathlib import Path
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QPushButton, QMessageBox, QFileDialog
from .player_widget import PlayerWidget
from .recorder_widget import RecorderWidget
from .transcription_widget import TranscriptionWidget

class MediaWidget(QWidget):
    """Combined Player and Recorder widget with tabs"""
    
    # Forward signals from recorder
    recording_finished = pyqtSignal(Path)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(450, 280)  # Ensure minimum size for tabbed interface
        
        # Initialize transcription manager
        self.current_audio_path = None
        
        self._setup_ui()
        self._connect_signals()
    
    def _setup_ui(self):
        """Setup the tabbed interface"""
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create tab widget with custom styling
        self.tab_widget = QTabWidget()
        self.tab_widget.setObjectName("media_tab_widget")  # For QSS styling
        
        # Create player, recorder, and transcription widgets
        self.player_widget = PlayerWidget()
        self.recorder_widget = RecorderWidget()
        self.transcription_widget = TranscriptionWidget()
        
        # Remove the group box styling since we're using tabs
        self.player_widget.setTitle("")  # Remove title
        self.recorder_widget.setTitle("")  # Remove title
        
        # Add tabs
        self.tab_widget.addTab(self.player_widget, "🎵 Player")
        self.tab_widget.addTab(self.recorder_widget, "🎤 Record")
        self.tab_widget.addTab(self.transcription_widget, "🤖 Transcribe")
        
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)
    
    def _connect_signals(self):
        """Connect internal signals"""
        # Forward recorder signals
        self.recorder_widget.recording_finished.connect(self.recording_finished.emit)

        # Handle tab changes to refresh transcription display
        self.tab_widget.currentChanged.connect(self._on_tab_changed)
    
    def _on_tab_changed(self, index: int):
        """Handle tab change events"""
        # Refresh transcription display when switching to player tab
        if index == 0:  # Player tab
            self.player_widget.refresh_transcription()
    
    # Forward player methods
    def load_audio(self, file_path: str):
        """Load audio file into player"""
        self.current_audio_path = Path(file_path)
        self.player_widget.load_audio(file_path)
        self.transcription_widget.set_current_audio(self.current_audio_path)
        # Switch to player tab when loading audio
        self.tab_widget.setCurrentIndex(0)
    
    def toggle_play(self):
        """Toggle play/pause"""
        self.player_widget.toggle_play()
    
    def jump_to_time(self, seconds: float):
        """Jump to specific time"""
        self.player_widget.jump_to_time(seconds)
    
    def current_seconds(self) -> float:
        """Get current playback position"""
        return self.player_widget.current_seconds()
    
    # Forward recorder methods
    def start_recording(self):
        """Start recording"""
        self.recorder_widget.start_recording()
        # Switch to recorder tab when starting recording
        self.tab_widget.setCurrentIndex(1)