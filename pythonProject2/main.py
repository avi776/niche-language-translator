from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QColor, QLinearGradient, QPalette, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty, QRect, QEasingCurve
from translations import translate_text

# Language code mapping (should match backend)
lang_code_mapping = [
    "English", "Romanian", "French", "German", "Spanish", "Italian",
    "Dutch", "Portuguese", "Polish", "Russian", "Telugu", "Tajik (Cyrillic)",
    "Tajik (Latin)", "Thai", "Turkish (Latin)", "Ukrainian (Cyrillic)",
    "Umbundu (Latin)", "Urdu (Arabic)", "Uzbek (Latin)", "Vietnamese (Latin)",
    "Wolof (Latin)", "Xhosa (Latin)", "Yoruba (Latin)", "Zulu (Latin)",
    "Chinese (Simplified)", "Chinese (Traditional)",
    "Bengali", "Swahili", "Tagalog", "Punjabi (Gurmukhi)", "Malayalam", "Amharic",
    "Kurdish (Kurmanji)", "Haitian Creole", "Pashto (Arabic)", "Tigrinya", "Somali",
    "Maori", "Hausa"
]

class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Colorful Translator')
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Stylish Heading
        heading_label = QLabel("Niche Language Translator")
        heading_label.setAlignment(Qt.AlignCenter)
        heading_label.setStyleSheet("""
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 20px 0;
        """)
        layout.addWidget(heading_label)

        # Source language dropdown
        self.source_combo = QComboBox()
        self.source_combo.addItems(lang_code_mapping)
        self.source_combo.setStyleSheet(self.get_dropdown_style())
        layout.addWidget(self.create_labeled_widget("Source Language:", self.source_combo))

        # Target language dropdown
        self.target_combo = QComboBox()
        self.target_combo.addItems(lang_code_mapping)
        self.target_combo.setStyleSheet(self.get_dropdown_style())
        layout.addWidget(self.create_labeled_widget("Target Language:", self.target_combo))

        # Input text box
        self.input_textbox = QTextEdit()
        self.input_textbox.setPlaceholderText("Enter text to translate")
        self.input_textbox.setFont(QFont('Arial', 14))
        layout.addWidget(self.input_textbox)

        # Output text box
        self.output_textbox = QTextEdit()
        self.output_textbox.setReadOnly(True)
        self.output_textbox.setFont(QFont('Arial', 14))
        layout.addWidget(self.output_textbox)

        # Translate button
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet(self.get_button_style())
        self.translate_button.clicked.connect(self.start_translation_animation)  # Connect button to animation function
        layout.addWidget(self.translate_button)

        # Background gradient with light yellow, light salmon, light orange, and light red
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setCoordinateMode(QLinearGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor('#FFD700'))  # Light yellow
        gradient.setColorAt(0.25, QColor('#FFA07A'))  # Light salmon
        gradient.setColorAt(0.5, QColor('#FFD700'))  # Light yellow
        gradient.setColorAt(0.75, QColor('#FFA500'))  # Light orange
        gradient.setColorAt(1.0, QColor('#FFD700'))  # Light yellow
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

    def create_labeled_widget(self, label_text, widget):
        container = QWidget()
        layout = QHBoxLayout(container)
        label = QLabel(label_text)
        label.setStyleSheet("color: white; font-weight: bold;")
        layout.addWidget(label)
        layout.addWidget(widget)
        return container

    def get_dropdown_style(self):
        return """
        QComboBox {
            padding: 10px;
            font-size: 16px;
            min-width: 250px;
            color: #333;
        }
        """

    def get_button_style(self):
        return """
        QPushButton {
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(255, 215, 0, 255),
                stop:0.25 rgba(255, 160, 122, 255),
                stop:0.5 rgba(255, 215, 0, 255),
                stop:0.75 rgba(255, 165, 0, 255),
                stop:1 rgba(255, 215, 0, 255)
            );
            color: white;
            padding: 12px;
            font-size: 18px;
            border-radius: 12px;
            border: none;
        }
        QPushButton:hover {
            background-color: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(235, 195, 0, 255),
                stop:0.25 rgba(180, 135, 100, 255),
                stop:0.5 rgba(235, 195, 0, 255),
                stop:0.75 rgba(195, 145, 80, 255),
                stop:1 rgba(235, 195, 0, 255)
            );
        }
        """

    def start_translation_animation(self):
        # Create animation for the translate button
        animation = QPropertyAnimation(self.translate_button, b"geometry")
        animation.setDuration(1000)
        animation.setStartValue(self.translate_button.geometry())
        animation.setEndValue(QRect(0, 0, 200, 40))  # Adjust size and position as needed
        animation.setEasingCurve(QEasingCurve.OutBounce)  # Use bounce effect for animation
        animation.start()

        # Perform translation after animation
        self.translate_text()

    def translate_text(self):
        input_text = self.input_textbox.toPlainText().strip()
        if not input_text:
            QMessageBox.warning(self, "Input Error", "Please enter text to translate.")
            return

        source_lang = self.source_combo.currentText()
        target_lang = self.target_combo.currentText()

        if source_lang == target_lang:
            QMessageBox.warning(self, "Input Error", "Source and target languages must be different.")
            return

        translated_text = translate_text(input_text, source_lang, target_lang)

        # Set translated text and change color to green
        self.output_textbox.setStyleSheet("color: green;")  # Set green color for text
        self.output_textbox.setPlainText(translated_text)

if __name__ == "__main__":
    app = QApplication([])
    translator_app = TranslatorApp()
    translator_app.show()
    app.exec_()

