"""
Application Styles - Liquid Glass Theme
"""

LIQUID_QSS = r"""
* { 
  font-family: "SF Pro Display", "Helvetica Neue", "Segoe UI", Roboto, Arial, sans-serif;
  font-size: 13px;
  color: #1d1d1f;
}



QWidget#GlassRoot {
  background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 rgba(248, 249, 250, 0.95),
    stop:0.3 rgba(241, 245, 249, 0.90),
    stop:0.7 rgba(236, 242, 248, 0.85),
    stop:1 rgba(230, 238, 247, 0.80));
}

.glass {
  background: qradialgradient(cx:0.3, cy:0.2, radius:1.5,
    fx:0.3, fy:0.2,
    stop:0 rgba(255, 255, 255, 0.75),
    stop:0.5 rgba(255, 255, 255, 0.55),
    stop:1 rgba(255, 255, 255, 0.35));
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 18px;
}

QGroupBox.glass {
  padding-top: 20px;
  background: qradialgradient(cx:0.2, cy:0.15, radius:1.3,
    fx:0.2, fy:0.15,
    stop:0 rgba(255, 255, 255, 0.65),
    stop:0.6 rgba(255, 255, 255, 0.45),
    stop:1 rgba(255, 255, 255, 0.30));
  border: 1px solid rgba(255, 255, 255, 0.7);
}

QGroupBox::title {
  subcontrol-origin: margin;
  subcontrol-position: top left;
  padding: 10px 20px;
  margin-left: 16px;
  border-radius: 16px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(255, 255, 255, 0.95),
    stop:1 rgba(248, 250, 252, 0.85));
  border: 2px solid rgba(77, 140, 255, 0.3);
  color: #1e293b;
  font-weight: 700;
  font-size: 15px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 14px;
}

QLineEdit, QComboBox, QTextEdit, QSpinBox {
  background: rgba(255, 255, 255, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.95);
  border-radius: 12px;
  padding: 10px 12px;
  selection-background-color: rgba(77, 140, 255, 0.3);
  font-size: 13px;
}

QLineEdit:focus, QComboBox:focus, QTextEdit:focus, QSpinBox:focus {
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(77, 140, 255, 0.5);
}

QComboBox::drop-down {
  border: none;
  border-left: 1px solid rgba(255, 255, 255, 0.8);
  background: rgba(255, 255, 255, 0.6);
  border-radius: 0 10px 10px 0;
  width: 30px;
}

QComboBox::down-arrow {
  image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDFMNiA2TDExIDEIgIHN0cm9rZT0iIzVhNmM3ZCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
  width: 12px;
  height: 8px;
}

QComboBox::down-arrow:hover {
  image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDFMNiA2TDExIDEiIHN0cm9rZT0iIzFkNGVkOCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
}

QComboBox::down-arrow:pressed {
  image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDFMNiA2TDExIDEiIHN0cm9rZT0iIzFiM2Y5ZiIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
}

QComboBox QAbstractItemView {
  background: rgba(255, 255, 255, 0.95);
  border: 1px solid rgba(77, 140, 255, 0.3);
  border-radius: 8px;
  selection-background-color: rgba(77, 140, 255, 0.2);
  selection-color: #1d4ed8;
  padding: 4px;
}

QListWidget { 
  background: transparent; 
  border: none; 
  outline: none;
}

QListWidget::item { 
  padding: 10px 14px; 
  border-radius: 10px;
  margin: 1px 0px;
  font-size: 13px;
}

QListWidget::item:hover { 
  background: rgba(255, 255, 255, 0.65); 
}

QListWidget::item:selected {
  background: rgba(77, 140, 255, 0.25);
  color: #1d4ed8;
  border: 1px solid rgba(77, 140, 255, 0.4);
  font-weight: 500;
}

QPushButton, QToolButton {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.95);
  border-radius: 12px;
  padding: 8px 16px;
  font-weight: 500;
  font-size: 13px;
}

QPushButton:hover, QToolButton:hover { 
  background: rgba(255, 255, 255, 0.95);
}

QPushButton:pressed, QToolButton:pressed { 
  background: rgba(235, 235, 240, 0.9);
}

QPushButton[checkable="true"]:checked {
  background: rgba(255, 69, 58, 0.2);
  border: 1px solid rgba(255, 69, 58, 0.45);
  color: #d12b20;
  font-weight: 600;
}

QSlider::groove:horizontal { 
  height: 6px; 
  border-radius: 3px; 
  background: rgba(0, 0, 0, 0.08); 
}

QSlider::handle:horizontal {
  width: 16px; 
  height: 16px; 
  margin: -5px 0; 
  border-radius: 8px; 
  background: white;
  border: 2px solid rgba(77, 140, 255, 0.6);
}

QSlider::handle:horizontal:hover {
  width: 18px;
  height: 18px;
  margin: -6px 0;
  border-radius: 9px;
  border: 2px solid rgba(77, 140, 255, 0.8);
}

QSlider::sub-page:horizontal { 
  background: rgba(77, 140, 255, 0.4); 
  border-radius: 3px; 
}

QProgressBar {
  background: rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  height: 16px;
  text-align: center;
}

QProgressBar::chunk { 
  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop:0 rgba(76, 217, 100, 0.8),
    stop:0.7 rgba(255, 214, 10, 0.8),
    stop:1 rgba(255, 69, 58, 0.8));
  border-radius: 10px; 
}

/* Scrollbars */
QScrollBar:vertical {
  background: rgba(0, 0, 0, 0.05);
  width: 8px;
  border-radius: 4px;
}

QScrollBar::handle:vertical {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  min-height: 20px;
}

QScrollBar::handle:vertical:hover {
  background: rgba(0, 0, 0, 0.3);
}

/* NotesWidget specific styles */
QWidget#NotesWidget {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 12px;
}

QWidget#NotesWidget QLabel[objectName="header_label"] {
  font-size: 16px;
  font-weight: 700;
  color: #1e293b;
  padding: 8px 16px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.15),
    stop:1 rgba(37, 99, 235, 0.1));
  border: 2px solid rgba(59, 130, 246, 0.3);
  border-radius: 12px;
  margin-bottom: 4px;
}

QWidget#NotesWidget QLabel[objectName="note_label"] {
  font-size: 14px;
  font-weight: 600;
  color: #2c3e50;
  padding: 4px 0px;
}

QWidget#NotesWidget QTextEdit {
  padding: 8px;
  font-size: 13px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(200, 200, 200, 0.6);
  border-radius: 6px;
}

QWidget#NotesWidget QTextEdit:focus {
  border: 2px solid rgba(77, 140, 255, 0.6);
  background: rgba(255, 255, 255, 1.0);
}

QWidget#NotesWidget QCheckBox {
  font-size: 11px;
  color: #6b7280;
}

QWidget#NotesWidget QPushButton[objectName="btn_add_note"] {
  padding: 10px 16px;
  font-size: 13px;
  font-weight: 600;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.2),
    stop:1 rgba(37, 99, 235, 0.15));
  border: 2px solid rgba(59, 130, 246, 0.4);
  border-radius: 8px;
  color: #1d4ed8;
  min-height: 20px;
}

QWidget#NotesWidget QPushButton[objectName="btn_add_note"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.3),
    stop:1 rgba(37, 99, 235, 0.25));
  border: 2px solid rgba(59, 130, 246, 0.6);
}

QWidget#NotesWidget QPushButton[objectName="btn_add_note"]:pressed {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(37, 99, 235, 0.25),
    stop:1 rgba(29, 78, 216, 0.2));
}

QWidget#NotesWidget QLabel[objectName="time_help"] {
  font-size: 10px;
  color: #9ca3af;
  font-style: italic;
  padding: 2px 0px;
}

QWidget#NotesWidget QLabel[objectName="notes_header"] {
  font-size: 14px;
  font-weight: 600;
  color: #2c3e50;
  padding: 4px 0px;
}

QWidget#NotesWidget QLabel[objectName="notes_subheader"] {
  font-size: 10px;
  color: #9ca3af;
}

QWidget#NotesWidget QListWidget {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(200, 200, 200, 0.6);
  border-radius: 6px;
  padding: 6px;
}

QWidget#NotesWidget QListWidget::item {
  padding: 6px 8px;
  border-radius: 3px;
  margin: 1px 0px;
  font-size: 12px;
  background: transparent;
}

QWidget#NotesWidget QListWidget::item:hover {
  background: rgba(243, 244, 246, 0.8);
}

QWidget#NotesWidget QListWidget::item:selected {
  background: rgba(59, 130, 246, 0.1);
  color: #1d4ed8;
}

QWidget#NotesWidget QPushButton[objectName="btn_delete_note"] {
  padding: 8px 12px;
  font-size: 12px;
  font-weight: 600;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.15),
    stop:1 rgba(220, 38, 38, 0.1));
  border: 2px solid rgba(239, 68, 68, 0.4);
  border-radius: 6px;
  color: #dc2626;
  min-height: 18px;
}

QWidget#NotesWidget QPushButton[objectName="btn_delete_note"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.25),
    stop:1 rgba(220, 38, 38, 0.2));
  border: 2px solid rgba(239, 68, 68, 0.6);
}

QWidget#NotesWidget QPushButton[objectName="btn_delete_note"]:pressed {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(220, 38, 38, 0.2),
    stop:1 rgba(185, 28, 28, 0.15));
}

QWidget#NotesWidget QPushButton[objectName="btn_clear_all"] {
  padding: 8px 10px;
  font-size: 13px;
  font-weight: 600;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.2),
    stop:1 rgba(220, 38, 38, 0.15));
  border: 2px solid rgba(239, 68, 68, 0.4);
  border-radius: 8px;
  color: #dc2626;
  min-width: 32px;
  max-width: 32px;
  min-height: 20px;
}

QWidget#NotesWidget QPushButton[objectName="btn_clear_all"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.3),
    stop:1 rgba(220, 38, 38, 0.25));
  border: 2px solid rgba(239, 68, 68, 0.6);
}

QWidget#NotesWidget QPushButton[objectName="btn_clear_all"]:pressed {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(220, 38, 38, 0.25),
    stop:1 rgba(185, 28, 28, 0.2));
}

QWidget#NotesWidget QPushButton[objectName="btn_export_notes"] {
  padding: 8px 12px;
  font-size: 12px;
  font-weight: 600;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.15),
    stop:1 rgba(22, 163, 74, 0.1));
  border: 2px solid rgba(34, 197, 94, 0.4);
  border-radius: 6px;
  color: #16a34a;
  min-height: 18px;
  min-width: 32px;
  max-width: 32px;
}

QWidget#NotesWidget QPushButton[objectName="btn_export_notes"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.25),
    stop:1 rgba(22, 163, 74, 0.2));
  border: 2px solid rgba(34, 197, 94, 0.6);
}

QWidget#NotesWidget QPushButton[objectName="btn_export_notes"]:pressed {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(22, 163, 74, 0.2),
    stop:1 rgba(20, 83, 45, 0.15));
}

QWidget#NotesWidget QPushButton[objectName="btn_import_notes"] {
  padding: 8px 12px;
  font-size: 12px;
  font-weight: 600;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.15),
    stop:1 rgba(37, 99, 235, 0.1));
  border: 2px solid rgba(59, 130, 246, 0.4);
  border-radius: 6px;
  color: #2563eb;
  min-height: 18px;
  min-width: 24px;
  max-width: 24px;
}

QWidget#NotesWidget QPushButton[objectName="btn_import_notes"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.25),
    stop:1 rgba(37, 99, 235, 0.2));
  border: 2px solid rgba(59, 130, 246, 0.6);
}

QWidget#NotesWidget QPushButton[objectName="btn_import_notes"]:pressed {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(37, 99, 235, 0.2),
    stop:1 rgba(29, 78, 216, 0.15));
}

/* PlayerWidget specific styles */
QGroupBox[class="glass"] QLabel[objectName="lbl_title"] {
  font-weight: 500;
  font-size: 15px;
  color: #9ca3af;
  padding: 4px 8px;
}

QGroupBox[class="glass"] QLabel[objectName="lbl_title_loaded"] {
  font-weight: 600;
  font-size: 15px;
  color: #2c3e50;
  padding: 4px 8px;
}

QGroupBox[class="glass"] QToolButton[objectName="btn_play"] {
  background: rgba(77, 140, 255, 0.15);
  border: 1px solid rgba(77, 140, 255, 0.3);
  border-radius: 20px;
  padding: 8px;
  min-width: 32px;
  min-height: 32px;
}

QGroupBox[class="glass"] QToolButton[objectName="btn_play"]:hover {
  background: rgba(77, 140, 255, 0.25);
  border: 1px solid rgba(77, 140, 255, 0.4);
}

QGroupBox[class="glass"] QToolButton[objectName="btn_play"]:pressed {
  background: rgba(77, 140, 255, 0.35);
}

QGroupBox[class="glass"] QSlider[objectName="position_slider"]::groove:horizontal {
  height: 8px;
  border-radius: 4px;
  background: rgba(0, 0, 0, 0.08);
}

QGroupBox[class="glass"] QSlider[objectName="position_slider"]::handle:horizontal {
  width: 18px;
  height: 18px;
  margin: -5px 0;
  border-radius: 9px;
  background: rgba(77, 140, 255, 0.9);
  border: 2px solid white;
}

QGroupBox[class="glass"] QSlider[objectName="position_slider"]::handle:horizontal:hover {
  background: rgba(77, 140, 255, 1.0);
  width: 20px;
  height: 20px;
  margin: -6px 0;
  border-radius: 10px;
}

QGroupBox[class="glass"] QSlider[objectName="position_slider"]::sub-page:horizontal {
  background: rgba(77, 140, 255, 0.4);
  border-radius: 4px;
}

QGroupBox[class="glass"] QLabel[objectName="lbl_time"] {
  font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
  font-size: 13px;
  font-weight: 500;
  color: #5a6c7d;
  padding: 0px 8px;
}

QGroupBox[class="glass"] QTextEdit[objectName="transcription_display"] {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(200, 200, 200, 0.6);
  border-radius: 8px;
  padding: 8px;
  font-size: 14px;
  line-height: 1.4;
}

QGroupBox[class="glass"] QTextEdit[objectName="transcription_display"]:focus {
  border: 2px solid rgba(77, 140, 255, 0.6);
  background: rgba(255, 255, 255, 1.0);
}

QGroupBox[class="glass"] QLabel[objectName="translation_label"] {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(200, 200, 200, 0.6);
  border-radius: 8px;
  padding: 8px;
  font-size: 14px;
  line-height: 1.4;
}

QGroupBox[class="glass"] QLabel[objectName="translation_label"]:focus {
  border: 2px solid rgba(77, 140, 255, 0.6);
  background: rgba(255, 255, 255, 1.0);
}

QGroupBox[class="glass"] QLabel[objectName="transcription_label"] {
  font-size: 13px;
  font-weight: 600;
  color: #1e293b;
  padding: 6px 12px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(16, 185, 129, 0.12),
    stop:1 rgba(5, 150, 105, 0.08));
  border: 1px solid rgba(16, 185, 129, 0.2);
  border-radius: 10px;
}

QGroupBox[class="glass"] QLabel[objectName="translation_label_header"] {
  font-size: 13px;
  font-weight: 600;
  color: #1e293b;
  padding: 6px 12px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(234, 179, 8, 0.12),
    stop:1 rgba(202, 138, 4, 0.08));
  border: 1px solid rgba(234, 179, 8, 0.2);
  border-radius: 10px;
}

QGroupBox[class="glass"] QLabel[objectName="speed_label"] {
  font-size: 13px;
  font-weight: 600;
  color: #1e293b;
  padding: 6px 12px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(99, 102, 241, 0.12),
    stop:1 rgba(79, 70, 229, 0.08));
  border: 1px solid rgba(99, 102, 241, 0.2);
  border-radius: 10px;
}

QGroupBox[class="glass"] QLabel[objectName="volume_label"] {
  font-size: 13px;
  font-weight: 600;
  color: #1e293b;
  padding: 6px 12px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(236, 72, 153, 0.12),
    stop:1 rgba(219, 39, 119, 0.08));
  border: 1px solid rgba(236, 72, 153, 0.2);
  border-radius: 10px;
}

QGroupBox[class="glass"] QSlider[objectName="volume_slider"]::groove:horizontal {
  height: 6px;
  border-radius: 3px;
  background: rgba(0, 0, 0, 0.08);
}

QGroupBox[class="glass"] QSlider[objectName="volume_slider"]::handle:horizontal {
  width: 16px;
  height: 16px;
  margin: -5px 0;
  border-radius: 8px;
  background: rgba(236, 72, 153, 0.9);
  border: 2px solid white;
}

QGroupBox[class="glass"] QSlider[objectName="volume_slider"]::handle:horizontal:hover {
  background: rgba(236, 72, 153, 1.0);
}

QGroupBox[class="glass"] QSlider[objectName="volume_slider"]::sub-page:horizontal {
  background: rgba(236, 72, 153, 0.4);
  border-radius: 3px;
}

/* TranscriptionWidget specific styles */
QWidget QLabel[objectName="trans_header"] {
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  padding: 12px 20px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(16, 185, 129, 0.15),
    stop:1 rgba(5, 150, 105, 0.1));
  border: 2px solid rgba(16, 185, 129, 0.3);
  border-radius: 16px;
  margin-bottom: 4px;
}

QWidget QLabel[objectName="trans_subheader"] {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 12px;
}

QWidget QLabel[objectName="model_label"] {
  font-size: 15px;
  font-weight: 600;
  color: #1e293b;
  padding: 8px 14px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.12),
    stop:1 rgba(37, 99, 235, 0.08));
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 12px;
  margin-bottom: 4px;
}

QWidget QLabel[objectName="model_help"] {
  font-size: 12px;
  color: #9ca3af;
}

QWidget QLabel[objectName="status_label"] {
  font-size: 15px;
  font-weight: 600;
  color: #1e293b;
  padding: 8px 14px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(245, 158, 11, 0.12),
    stop:1 rgba(217, 119, 6, 0.08));
  border: 1px solid rgba(245, 158, 11, 0.2);
  border-radius: 12px;
  margin-bottom: 4px;
}

QWidget QLabel[objectName="words_status"] {
  font-size: 13px;
  font-weight: 500;
  padding: 16px 20px;
  background: rgba(249, 250, 251, 0.8);
  border: 1px solid rgba(229, 231, 235, 0.8);
  border-radius: 10px;
  min-height: 20px;
}

/* LibraryWidget specific styles */
QWidget QLabel[objectName="library_header"] {
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  padding: 12px 20px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(77, 140, 255, 0.15),
    stop:1 rgba(59, 130, 246, 0.1));
  border: 2px solid rgba(77, 140, 255, 0.25);
  border-radius: 16px;
  margin-bottom: 8px;
  text-align: center;
}

QWidget QLineEdit[objectName="library_search"] {
  padding: 12px 16px;
  font-size: 14px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 14px;
}

QWidget QLineEdit[objectName="library_search"]:focus {
  background: rgba(255, 255, 255, 0.85);
  border: 2px solid rgba(77, 140, 255, 0.6);
}

QWidget QListWidget[objectName="library_list"] {
  padding: 12px;
  background: transparent;
  border: none;
  outline: none;
}

QWidget QListWidget[objectName="library_list"]::item {
  padding: 12px 16px;
  border-radius: 12px;
  margin: 2px 0px;
  font-size: 14px;
  font-weight: 500;
}

QWidget QListWidget[objectName="library_list"]::item:hover {
  background: rgba(255, 255, 255, 0.6);
}

QWidget QListWidget[objectName="library_list"]::item:selected {
  background: rgba(77, 140, 255, 0.25);
  color: #0e1116;
  border: 1px solid rgba(77, 140, 255, 0.4);
  font-weight: 600;
}

QWidget QPushButton[objectName="library_import_btn"] {
  padding: 12px 20px;
  font-size: 14px;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.95);
  border-radius: 14px;
}

QWidget QPushButton[objectName="library_import_btn"]:hover {
  background: rgba(255, 255, 255, 0.95);
}

QWidget QPushButton[objectName="library_import_btn"]:pressed {
  background: rgba(235, 235, 240, 0.85);
}

QWidget QPushButton[objectName="library_delete_btn"] {
  padding: 12px 20px;
  font-size: 14px;
  font-weight: 600;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 14px;
  color: #dc2626;
}

QWidget QPushButton[objectName="library_delete_btn"]:hover {
  background: rgba(239, 68, 68, 0.2);
}

QWidget QPushButton[objectName="library_delete_btn"]:pressed {
  background: rgba(239, 68, 68, 0.3);
}

QWidget QTabWidget[objectName="media_tab_widget"] {
  background: transparent;
}

QWidget QTabWidget[objectName="media_tab_widget"]::pane {
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-top-left-radius: 0px;
  border-top-right-radius: 12px;
  border-bottom-right-radius: 12px;
  border-bottom-left-radius: 12px;
  background: rgba(255, 255, 255, 0.8);
  margin-top: -1px;
}

QWidget QTabWidget[objectName="media_tab_widget"]::tab-bar {
  alignment: left;
}

QWidget QTabWidget[objectName="media_tab_widget"] QTabBar::tab {
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-bottom: none;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  padding: 12px 18px;
  margin-right: 4px;
  font-weight: 500;
  font-size: 13px;
  color: #5a6c7d;
}

QWidget QTabWidget[objectName="media_tab_widget"] QTabBar::tab:selected {
  background: rgba(77, 140, 255, 0.15);
  border: 1px solid rgba(77, 140, 255, 0.3);
  border-bottom: none;
  color: #1d4ed8;
  font-weight: 600;
}

QWidget QSplitter[objectName="main_splitter"] {
  background: transparent;
}

QWidget QSplitter[objectName="main_splitter"]::handle {
  background: rgba(255, 255, 255, 0.3);
  width: 2px;
  margin: 20px 0px;
  border-radius: 1px;
}

QWidget QSplitter[objectName="main_splitter"]::handle:hover {
  background: rgba(255, 255, 255, 0.5);
}

/* RecorderWidget specific styles */
QGroupBox[class="glass"] QComboBox[objectName="device_combo"] {
  padding: 8px 12px;
  font-size: 13px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 10px;
}

QGroupBox[class="glass"] QComboBox[objectName="device_combo"]:focus {
  border: 1px solid rgba(77, 140, 255, 0.5);
}

QGroupBox[class="glass"] QComboBox[objectName="device_combo"]::drop-down {
  border: none;
  padding-right: 8px;
}

QGroupBox[class="glass"] QProgressBar[objectName="level_bar"] {
  background: rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  height: 16px;
}

QGroupBox[class="glass"] QProgressBar[objectName="level_bar"]::chunk {
  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop:0 rgba(76, 217, 100, 0.7),
    stop:0.7 rgba(255, 214, 10, 0.7),
    stop:1 rgba(255, 69, 58, 0.7));
  border-radius: 8px;
}

QGroupBox[class="glass"] QPushButton[objectName="btn_record"] {
  padding: 10px 18px;
  font-size: 14px;
  font-weight: 700;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(255, 255, 255, 0.95),
    stop:1 rgba(248, 250, 252, 0.85));
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 12px;
  color: #1a202c;
  min-height: 16px;
}

QGroupBox[class="glass"] QPushButton[objectName="btn_record"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(255, 255, 255, 1.0),
    stop:1 rgba(250, 252, 255, 0.95));
  border: 2px solid rgba(59, 130, 246, 0.3);
}

QGroupBox[class="glass"] QPushButton[objectName="btn_record"]:pressed {
  background: rgba(241, 245, 249, 0.9);
}

QGroupBox[class="glass"] QPushButton[objectName="btn_record"][checkable="true"]:checked {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.15),
    stop:1 rgba(220, 38, 38, 0.1));
  border: 2px solid rgba(239, 68, 68, 0.4);
  color: #dc2626;
  font-weight: 800;
}

QGroupBox[class="glass"] QPushButton[objectName="btn_record"][checkable="true"]:checked:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.25),
    stop:1 rgba(220, 38, 38, 0.2));
  border: 2px solid rgba(239, 68, 68, 0.6);
}

QGroupBox[class="glass"] QLabel[objectName="status_label"] {
  font-size: 11px;
  font-weight: 500;
  color: #5a6c7d;
  padding: 0px 6px;
}

QGroupBox[class="glass"] QLabel[objectName="device_label"] {
  font-size: 14px;
  font-weight: 600;
  color: #1e293b;
  padding: 8px 14px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.12),
    stop:1 rgba(220, 38, 38, 0.08));
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 12px;
  margin-bottom: 6px;
}

QGroupBox[class="glass"] QLabel[objectName="level_label"] {
  font-size: 14px;
  font-weight: 600;
  color: #1e293b;
  padding: 8px 14px;
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.12),
    stop:1 rgba(22, 163, 74, 0.08));
  border: 1px solid rgba(34, 197, 94, 0.2);
  border-radius: 12px;
  margin-bottom: 6px;
}

/* Dialog styles for QMessageBox, QFileDialog, QInputDialog */
QMessageBox {
  background: qradialgradient(cx:0.5, cy:0.5, radius:0.5,
    stop:0 rgba(255, 255, 255, 0.95),
    stop:1 rgba(248, 250, 252, 0.85));
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  color: #1e293b;
}

QMessageBox QLabel {
  color: #1e293b;
  font-size: 14px;
  padding: 8px;
}

QMessageBox QPushButton {
  padding: 10px 20px;
  font-size: 13px;
  border-radius: 10px;
  min-width: 80px;
  margin: 4px;
}

QMessageBox QPushButton[text="&Yes"], QMessageBox QPushButton[text="Yes"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.15),
    stop:1 rgba(22, 163, 74, 0.1));
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #16a34a;
}

QMessageBox QPushButton[text="&Yes"]:hover, QMessageBox QPushButton[text="Yes"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.25),
    stop:1 rgba(22, 163, 74, 0.2));
  border: 1px solid rgba(34, 197, 94, 0.5);
}

QMessageBox QPushButton[text="&Yes"]:pressed, QMessageBox QPushButton[text="Yes"]:pressed {
  background: rgba(22, 163, 74, 0.15);
}

QMessageBox QPushButton[text="&No"], QMessageBox QPushButton[text="No"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.15),
    stop:1 rgba(220, 38, 38, 0.1));
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #dc2626;
}

QMessageBox QPushButton[text="&No"]:hover, QMessageBox QPushButton[text="No"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(239, 68, 68, 0.25),
    stop:1 rgba(220, 38, 38, 0.2));
  border: 1px solid rgba(239, 68, 68, 0.5);
}

QMessageBox QPushButton[text="&No"]:pressed, QMessageBox QPushButton[text="No"]:pressed {
  background: rgba(220, 38, 38, 0.15);
}

QMessageBox QPushButton[text="OK"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.15),
    stop:1 rgba(37, 99, 235, 0.1));
  border: 1px solid rgba(59, 130, 246, 0.3);
  color: #2563eb;
}

QMessageBox QPushButton[text="OK"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(59, 130, 246, 0.25),
    stop:1 rgba(37, 99, 235, 0.2));
  border: 1px solid rgba(59, 130, 246, 0.5);
}

QMessageBox QPushButton[text="OK"]:pressed {
  background: rgba(37, 99, 235, 0.15);
}

QMessageBox QPushButton[text="Cancel"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(156, 163, 175, 0.15),
    stop:1 rgba(107, 114, 128, 0.1));
  border: 1px solid rgba(156, 163, 175, 0.3);
  color: #6b7280;
}

QMessageBox QPushButton[text="Cancel"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(156, 163, 175, 0.25),
    stop:1 rgba(107, 114, 128, 0.2));
  border: 1px solid rgba(156, 163, 175, 0.5);
}

QMessageBox QPushButton[text="Cancel"]:pressed {
  background: rgba(107, 114, 128, 0.15);
}

QFileDialog {
  background: qradialgradient(cx:0.5, cy:0.5, radius:0.5,
    stop:0 rgba(255, 255, 255, 0.95),
    stop:1 rgba(248, 250, 252, 0.85));
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  color: #1e293b;
}

QFileDialog QWidget {
  background: transparent;
  color: #1e293b;
}

QFileDialog QLabel {
  color: #1e293b;
  font-size: 14px;
}

QFileDialog QLineEdit {
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  color: #1e293b;
}

QFileDialog QLineEdit:focus {
  border: 2px solid rgba(59, 130, 246, 0.5);
  background: rgba(255, 255, 255, 0.85);
}

QFileDialog QListView, QFileDialog QTreeView {
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  alternate-background-color: rgba(248, 250, 252, 0.8);
}

QFileDialog QListView::item, QFileDialog QTreeView::item {
  padding: 6px;
  border-radius: 6px;
  margin: 1px;
}

QFileDialog QListView::item:hover, QFileDialog QTreeView::item:hover {
  background: rgba(59, 130, 246, 0.1);
}

QFileDialog QListView::item:selected, QFileDialog QTreeView::item:selected {
  background: rgba(59, 130, 246, 0.2);
  border: 1px solid rgba(59, 130, 246, 0.4);
}

QFileDialog QPushButton {
  padding: 10px 16px;
  font-size: 13px;
  border-radius: 10px;
  min-width: 80px;
  margin: 4px;
}

QFileDialog QPushButton[text="&Open"], QFileDialog QPushButton[text="Open"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.15),
    stop:1 rgba(22, 163, 74, 0.1));
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #16a34a;
}

QFileDialog QPushButton[text="&Open"]:hover, QFileDialog QPushButton[text="Open"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.25),
    stop:1 rgba(22, 163, 74, 0.2));
  border: 1px solid rgba(34, 197, 94, 0.5);
}

QFileDialog QPushButton[text="&Open"]:pressed, QFileDialog QPushButton[text="Open"]:pressed {
  background: rgba(22, 163, 74, 0.15);
}

QFileDialog QPushButton[text="&Cancel"], QFileDialog QPushButton[text="Cancel"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(156, 163, 175, 0.15),
    stop:1 rgba(107, 114, 128, 0.1));
  border: 1px solid rgba(156, 163, 175, 0.3);
  color: #6b7280;
}

QFileDialog QPushButton[text="&Cancel"]:hover, QFileDialog QPushButton[text="Cancel"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(156, 163, 175, 0.25),
    stop:1 rgba(107, 114, 128, 0.2));
  border: 1px solid rgba(156, 163, 175, 0.5);
}

QFileDialog QPushButton[text="&Cancel"]:pressed, QFileDialog QPushButton[text="Cancel"]:pressed {
  background: rgba(107, 114, 128, 0.15);
}

QInputDialog {
  background: qradialgradient(cx:0.5, cy:0.5, radius:0.5,
    stop:0 rgba(255, 255, 255, 0.95),
    stop:1 rgba(248, 250, 252, 0.85));
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  color: #1e293b;
}

QInputDialog QLabel {
  color: #1e293b;
  font-size: 14px;
  padding: 8px;
}

QInputDialog QLineEdit {
  padding: 10px 12px;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 8px;
  color: #1e293b;
  font-size: 14px;
}

QInputDialog QLineEdit:focus {
  border: 2px solid rgba(59, 130, 246, 0.5);
  background: rgba(255, 255, 255, 0.85);
}

QInputDialog QPushButton {
  padding: 10px 16px;
  font-size: 13px;
  border-radius: 10px;
  min-width: 80px;
  margin: 4px;
}

QInputDialog QPushButton[text="OK"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.15),
    stop:1 rgba(22, 163, 74, 0.1));
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #16a34a;
}

QInputDialog QPushButton[text="OK"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(34, 197, 94, 0.25),
    stop:1 rgba(22, 163, 74, 0.2));
  border: 1px solid rgba(34, 197, 94, 0.5);
}

QInputDialog QPushButton[text="OK"]:pressed {
  background: rgba(22, 163, 74, 0.15);
}

QInputDialog QPushButton[text="Cancel"] {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(156, 163, 175, 0.15),
    stop:1 rgba(107, 114, 128, 0.1));
  border: 1px solid rgba(156, 163, 175, 0.3);
  color: #6b7280;
}

QInputDialog QPushButton[text="Cancel"]:hover {
  background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 rgba(156, 163, 175, 0.25),
    stop:1 rgba(107, 114, 128, 0.2));
  border: 1px solid rgba(156, 163, 175, 0.5);
}

QInputDialog QPushButton[text="Cancel"]:pressed {
  background: rgba(107, 114, 128, 0.15);
}
"""