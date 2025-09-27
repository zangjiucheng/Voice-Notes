"""
Audio Library Widget - Left panel with search and file list
"""
from pathlib import Path
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, 
    QListWidget, QListWidgetItem, QPushButton, QFileDialog, QLabel,
    QMessageBox, QMenu
)
from PyQt6.QtGui import QAction
from ..core.audio_library import AudioLibrary

class LibraryWidget(QWidget):
    file_selected = pyqtSignal(Path)  # Emitted when a file is selected
    file_opened = pyqtSignal(Path)    # Emitted when a file is double-clicked
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "glass")
        self.setMinimumSize(280, 400)  # Ensure minimum size for library panel
        
        self._setup_ui()
        self._connect_signals()
        self.refresh_list()
    
    def _setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        
        # Library header
        library_header = QLabel("Voice Notes") 
        library_header.setObjectName("library_header")  # For QSS styling
        
        # Search box with improved styling
        self.search_edit = QLineEdit()
        self.search_edit.setObjectName("library_search")  # For QSS styling
        self.search_edit.setPlaceholderText("Search recordings…")
        self.search_edit.setMinimumWidth(200)  # Ensure minimum search box width
        
        # File list with enhanced styling
        self.file_list = QListWidget()
        self.file_list.setObjectName("library_list")  # For QSS styling
        self.file_list.setMinimumSize(200, 200)  # Ensure minimum list size
        self.file_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)  # Enable context menu
        
        # Action buttons with improved styling
        self.btn_import = QPushButton("Import Audio")
        self.btn_import.setObjectName("library_import_btn")  # For QSS styling
        self.btn_delete = QPushButton("🗑️ Delete")
        self.btn_delete.setObjectName("library_delete_btn")  # For QSS styling
        self.btn_delete.setEnabled(False)  # Initially disabled
        
        # Button layouts
        top_button_layout = QHBoxLayout()
        top_button_layout.setSpacing(10)
        top_button_layout.addWidget(self.btn_import)
        
        bottom_button_layout = QHBoxLayout()
        bottom_button_layout.addWidget(self.btn_delete)
        
        # Add to layout with proper spacing
        layout.addWidget(library_header)
        layout.addWidget(self.search_edit)
        layout.addSpacing(8)
        layout.addWidget(self.file_list, 1)
        layout.addSpacing(8)
        layout.addLayout(top_button_layout)
        layout.addLayout(bottom_button_layout)
        
        self.setLayout(layout)
    
    def _connect_signals(self):
        self.search_edit.textChanged.connect(self.refresh_list)
        self.file_list.itemDoubleClicked.connect(self._on_item_double_clicked)
        self.file_list.currentItemChanged.connect(self._on_current_changed)
        self.file_list.customContextMenuRequested.connect(self._show_context_menu)
        self.btn_import.clicked.connect(self.import_files)
        self.btn_delete.clicked.connect(self.delete_selected_file)
    
    def refresh_list(self):
        """Refresh the file list based on search query"""
        query = self.search_edit.text()
        files = AudioLibrary.get_audio_files(query)
        
        self.file_list.clear()
        
        for file_path in files:
            display_name = AudioLibrary.format_display_name(file_path)
            item = QListWidgetItem(display_name)
            item.setData(Qt.ItemDataRole.UserRole, str(file_path))
            self.file_list.addItem(item)
    
    def import_files(self):
        """Import audio files via file dialog"""
        files, _ = QFileDialog.getOpenFileNames(
            self, 
            "Import audio", 
            str(Path.home()),
            "Audio Files (*.wav *.mp3 *.m4a *.aac *.flac *.ogg *.aiff *.aif)"
        )
        
        if files:
            AudioLibrary.import_audio_files(files)
            self.refresh_list()
    
    def select_file(self, file_path: Path):
        """Programmatically select a file in the list"""
        for i in range(self.file_list.count()):
            item = self.file_list.item(i)
            if Path(item.data(Qt.ItemDataRole.UserRole)) == file_path:
                self.file_list.setCurrentItem(item)
                break
    
    def _on_item_double_clicked(self, item: QListWidgetItem):
        """Handle item double-click"""
        file_path = Path(item.data(Qt.ItemDataRole.UserRole))
        self.file_opened.emit(file_path)
    
    def _on_current_changed(self, current: QListWidgetItem, previous: QListWidgetItem):
        """Handle current item change"""
        if current:
            file_path = Path(current.data(Qt.ItemDataRole.UserRole))
            self.file_selected.emit(file_path)
            self.btn_delete.setEnabled(True)  # Enable delete button
        else:
            self.btn_delete.setEnabled(False)  # Disable delete button
    
    def _show_context_menu(self, position):
        """Show context menu for file operations"""
        item = self.file_list.itemAt(position)
        if not item:
            return
        
        context_menu = QMenu(self)
        
        # Delete action
        delete_action = QAction("🗑️ Delete Recording", self)
        delete_action.triggered.connect(self.delete_selected_file)
        context_menu.addAction(delete_action)
        
        # Show context menu
        global_pos = self.file_list.mapToGlobal(position)
        context_menu.exec(global_pos)
    
    def delete_selected_file(self):
        """Delete the currently selected file"""
        current_item = self.file_list.currentItem()
        if not current_item:
            return
        
        file_path = Path(current_item.data(Qt.ItemDataRole.UserRole))
        file_name = file_path.name
        
        # Confirmation dialog
        reply = QMessageBox.question(
            self,
            "Delete Recording",
            f"Are you sure you want to delete '{file_name}'?\n\n"
            f"This will also delete any associated notes and transcription files.\n"
            f"This action cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Delete the audio file and associated files
                AudioLibrary.delete_audio_file(file_path)
                
                # Refresh the list
                self.refresh_list()
                
                # Show success message
                QMessageBox.information(
                    self,
                    "File Deleted",
                    f"'{file_name}' and its associated files have been deleted."
                )
                
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Delete Error",
                    f"Failed to delete '{file_name}':\n{str(e)}"
                )