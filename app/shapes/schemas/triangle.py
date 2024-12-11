from pydantic import model_validator
from shapes.schemas.base import Shape


class Triangle(Shape):
    a: float
    b: float
    c: float

    @model_validator(mode="before")
    def validate_triangle_inequality(cls, values):
        """Проверка неравенства треугольника: сумма двух сторон должна быть больше третьей"""
        a, b, c = values.get("a"), values.get("b"), values.get("c")

        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(
                "Для треугольника сумма любых двух сторон должна быть больше третьей."
            )

        return values
