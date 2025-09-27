"""
Notes Widget
"""
import re
from pathlib import Path
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QFormLayout,
    QTextEdit, QCheckBox, QSpinBox, QPushButton, QListWidget,
    QListWidgetItem, QComboBox, QLabel, QMessageBox, QFileDialog,
    QTabWidget, QFrame
)
from ..core.notes_manager import NotesManager
from ..utils.helpers import extract_time_from_text, parse_note_time

class NotesWidget(QFrame):
    """Notes widget"""
    jump_to_time = pyqtSignal(float)  # Emitted to request jump to specific time
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("NotesWidget")  # Set object name for CSS styling
        self.setMinimumSize(450, 500)  # Ensure minimum size for interface
        self.setFrameStyle(QFrame.Shape.NoFrame)  # Remove frame border
        
        self.notes_manager = NotesManager()
        self.current_audio_path = None

        
        self._setup_ui()
        self._connect_signals()
    
    def _setup_ui(self):
        """Setup the notes interface"""
        self.setAutoFillBackground(True)  # Enable background painting for QSS
        
        layout = QVBoxLayout()
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        # Notes header
        header_label = QLabel("📝 Notes")
        header_label.setObjectName("header_label")  # For QSS styling
        
        # Note input section
        input_section = QVBoxLayout()
        input_section.setSpacing(8)
        
        note_label = QLabel("Write a Note")
        note_label.setObjectName("note_label")  # For QSS styling
        
        self.note_text = QTextEdit()
        self.note_text.setMaximumHeight(60)
        self.note_text.setMinimumHeight(45)
        self.note_text.setPlaceholderText("Type your note here...")
        
        # Checkbox and button in one row
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(8)
        
        self.chk_anchor_nearest = QCheckBox("Auto-anchor to current time")
        
        self.btn_add_note = QPushButton("Add Note")
        self.btn_add_note.setObjectName("btn_add_note")  # For QSS styling
        
        controls_layout.addWidget(self.chk_anchor_nearest)
        controls_layout.addStretch()
        controls_layout.addWidget(self.btn_add_note)
        
        # Time stamp help
        time_help = QLabel("Tip: Use [[MM:SS]] format to add timestamps")
        time_help.setObjectName("time_help")  # For QSS styling
        
        input_section.addWidget(note_label)
        input_section.addWidget(self.note_text)
        input_section.addWidget(time_help)
        input_section.addLayout(controls_layout)
        
        # Notes list section
        list_section = QVBoxLayout()
        list_section.setSpacing(6)
        
        notes_header = QLabel("Your Notes")
        notes_header.setObjectName("notes_header")  # For QSS styling
        
        notes_subheader = QLabel("Double-click to jump to timestamp")
        notes_subheader.setObjectName("notes_subheader")  # For QSS styling
        
        self.notes_list = QListWidget()
        self.notes_list.setMinimumHeight(150)
        
        # Delete button
        self.btn_delete_note = QPushButton("🗑️ Delete")
        self.btn_delete_note.setObjectName("btn_delete_note")  # For QSS styling
        
        list_section.addWidget(notes_header)
        list_section.addWidget(notes_subheader)
        list_section.addWidget(self.notes_list, 1)
        list_section.addWidget(self.btn_delete_note, 0, Qt.AlignmentFlag.AlignRight)
        
        # Button layer for global actions
        button_layer = QHBoxLayout()
        button_layer.setSpacing(6)
        
        self.btn_clear_all = QPushButton("🗑️")
        self.btn_clear_all.setToolTip("Clear All Notes")
        self.btn_clear_all.setObjectName("btn_clear_all")  # For QSS styling
        
        self.btn_export_notes = QPushButton("📤")
        self.btn_export_notes.setToolTip("Export Notes")
        self.btn_export_notes.setObjectName("btn_export_notes")  # For QSS styling
        
        self.btn_import_notes = QPushButton("📥")
        self.btn_import_notes.setToolTip("Import Notes")
        self.btn_import_notes.setObjectName("btn_import_notes")  # For QSS styling
        
        button_layer.addWidget(self.btn_clear_all)
        button_layer.addWidget(self.btn_export_notes)
        button_layer.addWidget(self.btn_import_notes)
        button_layer.addStretch()
        
        # Add sections to main layout
        layout.addWidget(header_label)
        layout.addLayout(button_layer)
        layout.addLayout(input_section)
        layout.addSpacing(12)
        layout.addLayout(list_section)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def _connect_signals(self):
        self.btn_add_note.clicked.connect(self.add_note)
        self.btn_delete_note.clicked.connect(self.delete_selected_note)
        self.btn_clear_all.clicked.connect(self.clear_all_notes)
        self.btn_export_notes.clicked.connect(self.export_notes)
        self.btn_import_notes.clicked.connect(self.import_notes)
        self.notes_list.itemDoubleClicked.connect(self._on_note_double_clicked)
    
    def set_current_audio(self, audio_path: Path):
        """Set the current audio file and load its notes"""
        self.current_audio_path = audio_path
        self.load_notes()
    
    def set_current_time_callback(self, callback):
        """Set callback to get current playback time"""
        self._get_current_time = callback
    
    def load_notes(self):
        """Load notes for current audio file"""
        if not self.current_audio_path:
            return
        
        self.notes_manager.load_notes(self.current_audio_path)
        self._refresh_notes_list()
    
    def save_notes(self):
        """Save notes for current audio file"""
        if self.current_audio_path:
            self.notes_manager.save_notes(self.current_audio_path)
    
    def _refresh_notes_list(self):
        """Refresh the notes list widget"""
        self.notes_list.clear()
        
        for note in self.notes_manager.notes:
            note_line = self.notes_manager.note_to_line(note)
            self.notes_list.addItem(note_line)
    
    def add_note(self):
        """Add a new note"""
        if not self.current_audio_path:
            QMessageBox.information(
                self, "No file", "Open or record an audio first."
            )
            return
        
        text = self.note_text.toPlainText().strip()
        if not text:
            return
        
        # Simple anchor time logic
        anchor_time = extract_time_from_text(text)
        
        # Use current playback time if auto-anchor is enabled and no timestamp in text
        if (anchor_time is None and 
            self.chk_anchor_nearest.isChecked() and 
            hasattr(self, '_get_current_time')):
            
            current_time = self._get_current_time()
            anchor_time = current_time
        
        # Add note
        self.notes_manager.add_note(text, anchor_time)
        self._refresh_notes_list()
        self.save_notes()
        
        # Clear input
        self.note_text.clear()
    
    def delete_selected_note(self):
        """Delete the selected note"""
        current_row = self.notes_list.currentRow()
        if current_row >= 0:
            self.notes_manager.delete_note(current_row)
            self._refresh_notes_list()
            self.save_notes()
    
    def clear_all_notes(self):
        """Clear all notes for current audio file"""
        if not self.current_audio_path:
            QMessageBox.information(
                self, "No file", "Open or record an audio first."
            )
            return
        
        reply = QMessageBox.question(
            self, "Clear All Notes",
            "Are you sure you want to delete all notes for this audio file?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.notes_manager.clear_all_notes()
            self._refresh_notes_list()
            self.save_notes()
    
    def export_notes(self):
        """Export notes to a text file"""
        if not self.current_audio_path or not self.notes_manager.notes:
            QMessageBox.information(
                self, "No notes", "No notes to export."
            )
            return
        
        from PyQt6.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Notes", f"{self.current_audio_path.stem}_notes.txt",
            "Text Files (*.txt);;All Files (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"Notes for: {self.current_audio_path.name}\n")
                    f.write("=" * 50 + "\n\n")
                    for note in self.notes_manager.notes:
                        f.write(self.notes_manager.note_to_line(note) + "\n")
                
                QMessageBox.information(
                    self, "Export Complete", f"Notes exported to {file_path}"
                )
            except Exception as e:
                QMessageBox.critical(self, "Export Error", str(e))
    
    def import_notes(self):
        """Import notes from a text file"""
        if not self.current_audio_path:
            QMessageBox.information(
                self, "No file", "Open or record an audio first."
            )
            return
        
        from PyQt6.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Import Notes", "", "Text Files (*.txt);;All Files (*)"
        )
        
        if file_path:
            try:
                imported_count = 0
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("Notes for:") and not line.startswith("="):
                            # Try to parse as a note with timestamp
                            time_seconds = parse_note_time(line)
                            text = line
                            if time_seconds is not None:
                                # Remove timestamp from text for storage
                                text = re.sub(r'\[\[.*?\]\]\s*', '', line).strip()
                            
                            self.notes_manager.add_note(text, time_seconds)
                            imported_count += 1
                
                if imported_count > 0:
                    self._refresh_notes_list()
                    self.save_notes()
                    QMessageBox.information(
                        self, "Import Complete", f"Imported {imported_count} notes from {file_path}"
                    )
                else:
                    QMessageBox.information(
                        self, "Import Complete", "No valid notes found in the file."
                    )
                    
            except Exception as e:
                QMessageBox.critical(self, "Import Error", str(e))
    
    def _on_note_double_clicked(self, item: QListWidgetItem):
        """Handle note double-click to jump to time"""
        note_text = item.text()
        time_seconds = parse_note_time(note_text)
        
        if time_seconds is not None:
            self.jump_to_time.emit(time_seconds)