import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton

class MirandaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Miranda AI Assistant")
        self.resize(400, 600)
        self.setStyleSheet("background-color: #1e1e2e; color: #cdd6f4;") # Tema oscuro futurista
        
        layout = QVBoxLayout()
        
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Escribe un comando o di 'Hola Miranda'...")
        
        self.send_btn = QPushButton("Enviar")
        
        layout.addWidget(self.chat_history)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_btn)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MirandaGUI()
    window.show()
    sys.exit(app.exec())