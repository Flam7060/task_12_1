import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        # self.result_display.setReadOnly(True) # Возможность ввода в дисплей
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setStyleSheet("font-size: 30px; padding: 10px;")
        self.layout.addWidget(self.result_display)

        self.button_layout = QVBoxLayout()

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        # Добавляем кнопки на интерфейс
        for row in self.buttons:
            button_row = QHBoxLayout()
            for button in row:
                button_widget = QPushButton(button)
                button_widget.setStyleSheet(
                    "font-size: 20px; padding: 20px; background-color: #f0f0f0; border: 1px solid #ddd;"
                )
                button_widget.clicked.connect(self.on_button_click)
                button_row.addWidget(button_widget)
            self.button_layout.addLayout(button_row)

        self.layout.addLayout(self.button_layout)

        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet(
            "font-size: 20px; padding: 20px; background-color: #ff4d4d; border: 1px solid #ddd;"
        )
        self.clear_button.clicked.connect(self.clear_display)
        self.layout.addWidget(self.clear_button)

        self.setLayout(self.layout)

        self.current_input = ""
        self.operator = ""
        self.previous_input = ""

    def on_button_click(self):
        clicked_button = self.sender().text()

        if clicked_button == "=":
            try:
                result = str(eval(self.current_input))
                self.result_display.setText(result)
                self.current_input = result
            except Exception as e:
                self.result_display.setText("Error")
                self.current_input = ""
        else:
            self.current_input += clicked_button
            self.result_display.setText(self.current_input)

    def clear_display(self):
        self.current_input = ""
        self.result_display.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
