"""
Audio Recorder Widget
"""
from pathlib import Path
from PyQt6.QtCore import pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QGroupBox, QFormLayout, QHBoxLayout, QVBoxLayout,
    QComboBox, QPushButton, QLabel, QProgressBar, QMessageBox
)
from ..core.recorder import RecorderThread
from ..core.audio_devices import AudioDeviceManager

class RecorderWidget(QGroupBox):
    recording_finished = pyqtSignal(Path)  # Emitted when recording is complete
    
    def __init__(self, parent=None):
        super().__init__("Record", parent)
        self.setProperty("class", "glass")
        self.setMinimumSize(400, 200)  # Ensure minimum size for recorder controls
        
        self.recorder = None
        self._setup_ui()
        self._connect_signals()
    
    def _setup_ui(self):
        # Device selection
        self.device_combo = QComboBox()
        self.device_combo.setMinimumWidth(150)  # Ensure minimum combo box width
        self.device_combo.setObjectName("device_combo")
        self._populate_devices()
        
        # Level indicator with enhanced styling
        self.level_bar = QProgressBar()
        self.level_bar.setRange(0, 100)
        self.level_bar.setTextVisible(False)
        self.level_bar.setObjectName("level_bar")
        
        # Record button with enhanced visual emphasis
        self.btn_record = QPushButton("🔴 Record")
        self.btn_record.setCheckable(True)
        self.btn_record.setObjectName("btn_record")
        
        self.status_label = QLabel("Idle")
        self.status_label.setObjectName("status_label")
        
        # Layout with improved spacing
        layout = QVBoxLayout()
        layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinimumSize)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)
        
        # Device selection
        device_layout = QHBoxLayout()
        device_label = QLabel("🎤 Input Device")
        device_label.setObjectName("device_label")
        device_layout.addWidget(device_label)
        device_layout.addWidget(self.device_combo, 1)
        layout.addLayout(device_layout)
        
        # Record button and status
        record_layout = QHBoxLayout()
        record_layout.setSpacing(12)
        record_layout.addWidget(self.btn_record)
        record_layout.addWidget(self.status_label, 1)
        layout.addLayout(record_layout)
        
        # Level indicator
        level_layout = QVBoxLayout()
        level_layout.setSpacing(4)
        level_label = QLabel("📊 Input Level")
        level_label.setObjectName("level_label")
        level_layout.addWidget(level_label)
        level_layout.addWidget(self.level_bar)
        layout.addLayout(level_layout)
        layout.addStretch(1)
        
        self.setLayout(layout)
    
    def _connect_signals(self):
        self.btn_record.clicked.connect(self.toggle_recording)
    
    def _populate_devices(self):
        """Populate the device combo box"""
        devices = AudioDeviceManager.get_input_devices()
        
        for device in devices:
            self.device_combo.addItem(device['name'], userData=device)
    
    def toggle_recording(self):
        """Toggle recording on/off"""
        if self.recorder and self.recorder.isRunning():
            self.stop_recording()
        else:
            self.start_recording()
    
    def start_recording(self, save_path: Path = None):
        """Start audio recording"""
        if self.recorder and self.recorder.isRunning():
            return
        
        if save_path is None:
            from ..core.audio_library import AudioLibrary
            save_path = AudioLibrary.generate_recording_path()
        
        # Get selected device
        device_index = None
        device_name = self.device_combo.currentText()
        device_index = AudioDeviceManager.find_device_index(device_name)
        
        # Create and start recorder thread
        self.recorder = RecorderThread(save_path, device=device_index)
        self.recorder.level.connect(self._on_level_changed)
        self.recorder.recording_started.connect(self._on_recording_started)
        self.recorder.recording_stopped.connect(self._on_recording_stopped)
        self.recorder.error.connect(self._on_recording_error)
        
        self.recorder.start()
        
        self.btn_record.setChecked(True)
        self.btn_record.setText("⏹️ Stop Recording")
        self.status_label.setText(f"Recording → {save_path.name}")
    
    def stop_recording(self):
        """Stop audio recording"""
        if self.recorder:
            self.recorder.stop()
            self.btn_record.setEnabled(False)
    
    @pyqtSlot(float)
    def _on_level_changed(self, level: float):
        """Handle audio level change"""
        self.level_bar.setValue(int(level * 100))
    
    @pyqtSlot(Path)
    def _on_recording_started(self, path: Path):
        """Handle recording started"""
        pass  # Status already set in start_recording
    
    @pyqtSlot(Path, float)
    def _on_recording_stopped(self, path: Path, duration: float):
        """Handle recording stopped"""
        self.btn_record.setEnabled(True)
        self.btn_record.setChecked(False)
        self.btn_record.setText("🔴 Record")
        self.status_label.setText(f"Saved {path.name} ({duration:.1f}s)")
        
        self.recorder = None
        self.recording_finished.emit(path)
    
    @pyqtSlot(str)
    def _on_recording_error(self, error_msg: str):
        """Handle recording error"""
        self.btn_record.setEnabled(True)
        self.btn_record.setChecked(False)
        self.btn_record.setText("🔴 Record")
        self.status_label.setText("Error")
        
        self.recorder = None
        QMessageBox.critical(self, "Recording Error", error_msg)