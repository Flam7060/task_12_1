from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)
from pydantic import ValidationError
from shapes import Triangle
from config import get_config

class TriangleApp(QWidget):
    def __init__(self, title="Треугольник", width=400, height=300):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        self.a_input = QLineEdit(self)
        self.b_input = QLineEdit(self)
        self.c_input = QLineEdit(self)

        self.form_layout.addRow("Сторона a:", self.a_input)
        self.form_layout.addRow("Сторона b:", self.b_input)
        self.form_layout.addRow("Сторона c:", self.c_input)

        self.calculate_button = QPushButton("Рассчитать", self)
        self.calculate_button.clicked.connect(self.calculate_triangle)

        self.result_label = QLabel(self)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.calculate_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def calculate_triangle(self):
        try:
            a = float(self.a_input.text())
            b = float(self.b_input.text())
            c = float(self.c_input.text())

            triangle = Triangle(a=a, b=b, c=c)

            type_of_triangle = triangle.type_of_triangle()
            angle_type = triangle.angle_type()
            area = triangle.area()

            result_text = (
                f"Тип треугольника: {type_of_triangle}\n"
                f"Тип углов: {angle_type}\n"
                f"Площадь: {area:.2f}"
            )

            self.result_label.setText(result_text)
        except ValidationError as e:
            self.result_label.setText(f"Ошибка валидации: {e.errors()[0]['msg']}")
        except ValueError as e:
            self.result_label.setText(f"Ошибка: {str(e)}")
        except Exception as e:
            self.result_label.setText(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = TriangleApp(title=get_config.app_name, width=get_config.width, height=get_config.height)
    window.show()
    sys.exit(app.exec_())
