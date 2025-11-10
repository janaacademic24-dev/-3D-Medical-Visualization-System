"""
Medical Visualization System - Main Entry Point
Run this file to start the application
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

from ui.main_window import MultiOrganVisualizationApp


def setup_dark_theme(app):
    """Configure dark theme for application"""
    app.setStyle('Fusion')
    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(45, 45, 45))
    palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(45, 45, 45))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(50, 130, 184))
    palette.setColor(QPalette.Highlight, QColor(15, 76, 117))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    
    app.setPalette(palette)


def main():
    """Main entry point"""
    print("=" * 60)
    print("🏥 Medical Visualization System")
    print("=" * 60)
    print("Initializing application...")
    
    app = QApplication(sys.argv)
    setup_dark_theme(app)
    
    print("✓ Qt application initialized")
    print("✓ Dark theme applied")
    print("Creating main window...")
    
    window = MultiOrganVisualizationApp()
    window.show()
    
    print("✓ Application ready!")
    print("=" * 60)
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
