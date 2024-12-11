from pydantic import BaseModel, model_validator


class Shape(BaseModel):
    """Базовый класс для геометрических фигур с общей валидацией"""

    @model_validator(mode="before")
    def validate_positive(cls, values):
        """Проверка, что значения сторон положительные и выполняется неравенство треугольника"""
        a, b, c = values.get("a"), values.get("b"), values.get("c")

        if any(side <= 0 for side in [a, b, c]):
            raise ValueError(
                "Все стороны треугольника должны быть положительными числами."
            )

        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(
                "Для треугольника сумма любых двух сторон должна быть больше третьей."
            )

        return values
