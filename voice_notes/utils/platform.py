"""
Platform-specific utilities
"""
from PyQt6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

# Optional macOS vibrancy (removed for stability)
HAVE_VIBRANCY = False

def apply_window_vibrancy(widget: QWidget):
    """Apply window vibrancy effect (no-op for stability)"""
    return

def apply_soft_shadow(widget: QWidget, radius=24, dx=0, dy=8, opacity=0.35):
    """Apply soft shadow effect to widget"""
    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(radius)
    shadow.setOffset(dx, dy)
    
    color = QColor(0, 0, 0)
    color.setAlphaF(opacity)
    shadow.setColor(color)
    
    widget.setGraphicsEffect(shadow)