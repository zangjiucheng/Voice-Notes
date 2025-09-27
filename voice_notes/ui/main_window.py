"""
Main Application Window
"""
from pathlib import Path
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSplitter
from ..widgets.library_widget import LibraryWidget
from ..widgets.media_widget import MediaWidget
from ..widgets.notes_widget import NotesWidget
from ..utils.platform import apply_soft_shadow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Notes")
        self.resize(1600, 1000)  # Larger default size for better usability
        self.setMinimumSize(1400, 1000)  # Increased minimum size to prevent squeeze
        self.setObjectName("GlassRoot")
        
        self.current_audio_path = None
        
        self._setup_ui()
        self._connect_signals()
        self._setup_actions()
        
        # UI update timer
        self.ui_timer = QTimer(self)
        self.ui_timer.timeout.connect(lambda: None)
        self.ui_timer.start(250)
    
    def _setup_ui(self):
        # Left panel - Library
        self.library_widget = LibraryWidget()
        
        # Right panel widgets - Combined media (player + recorder) and notes
        self.media_widget = MediaWidget()  # Combined player and recorder
        self.notes_widget = NotesWidget()
        
        # Right panel layout with horizontal arrangement
        right_layout = QHBoxLayout()
        right_layout.setContentsMargins(16, 12, 16, 12)
        right_layout.setSpacing(16)  # Space between media and notes
        right_layout.addWidget(self.media_widget)
        right_layout.addWidget(self.notes_widget)
        
        right_panel = QWidget()
        right_panel.setLayout(right_layout)
        
        # Main splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setObjectName("main_splitter")  # For QSS styling
        splitter.addWidget(self.library_widget)
        splitter.addWidget(right_panel)
        splitter.setSizes([350, 850])  # Wider panels for better usability
        splitter.setCollapsible(0, False)  # Prevent library panel from collapsing
        splitter.setCollapsible(1, False)  # Prevent right panel from collapsing
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(splitter)
        
        # Apply enhanced shadows
        for widget in [self.media_widget, self.notes_widget, self.library_widget]:
            apply_soft_shadow(widget, radius=32, dy=12, opacity=0.28)
    
    def _connect_signals(self):
        # Library signals
        self.library_widget.file_selected.connect(self.open_audio_file)
        self.library_widget.file_opened.connect(self.open_audio_file)
        
        # Media widget signals (combines player and recorder)
        self.media_widget.recording_finished.connect(self._on_recording_finished)
        
        # Notes signals
        self.notes_widget.jump_to_time.connect(self.media_widget.jump_to_time)
        
        # Set up current time callback for notes widget
        self.notes_widget.set_current_time_callback(
            self.media_widget.current_seconds
        )
    
    def _setup_actions(self):
        """Setup keyboard shortcuts"""
        # Import action
        import_action = QAction("Import…", self)
        import_action.setShortcut(QKeySequence.StandardKey.Paste)
        import_action.triggered.connect(self.library_widget.import_files)
        self.addAction(import_action)
        
        # New recording action
        new_action = QAction("New Recording", self)
        if hasattr(QKeySequence, "New"):
            new_action.setShortcut(QKeySequence.StandardKey.New)
        else:
            # Fallback for older PyQt6 versions
            new_action.setShortcut(QKeySequence("Ctrl+N"))
        new_action.triggered.connect(self.start_new_recording)
        self.addAction(new_action)
        
        # Play/Pause action
        playpause_action = QAction("Play/Pause", self)
        playpause_action.setShortcut(QKeySequence(Qt.Key.Key_Space))
        playpause_action.triggered.connect(self.media_widget.toggle_play)
        self.addAction(playpause_action)
    
    def open_audio_file(self, file_path: Path):
        """Open an audio file for playback and editing"""
        self.current_audio_path = file_path
        
        # Load into media widget (player)
        self.media_widget.load_audio(str(file_path))
        
        # Load notes
        self.notes_widget.set_current_audio(file_path)
    
    def start_new_recording(self):
        """Start a new recording"""
        self.media_widget.start_recording()
    
    def _on_recording_finished(self, file_path: Path):
        """Handle recording completion"""
        # Refresh library
        self.library_widget.refresh_list()
        
        # Select the new recording
        self.library_widget.select_file(file_path)
        
        # Open the new recording
        self.open_audio_file(file_path)