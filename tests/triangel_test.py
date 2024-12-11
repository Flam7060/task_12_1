import pytest
from math import isclose
from app.main import Triangle


@pytest.mark.parametrize(
    "triangle, expected_type",
    [
        (Triangle(a=3, b=4, c=5), "Разносторонний"),
        (Triangle(a=5, b=5, c=5), "Равносторонний"),
        (Triangle(a=5, b=5, c=7), "Равнобедренный"),
        (Triangle(a=3, b=4, c=6), "Разносторонний"),
    ],
)
def test_type_of_triangle(triangle, expected_type):
    """Тестирование типа треугольника"""
    assert triangle.type_of_triangle() == expected_type


@pytest.mark.parametrize(
    "triangle, expected_angle_type",
    [
        (Triangle(a=3, b=4, c=5), "Прямоугольный"),
        (Triangle(a=5, b=5, c=7), "Остроугольный"),
        (Triangle(a=7, b=9, c=12), "Тупоугольный"),
    ],
)
def test_angle_type(triangle, expected_angle_type):
    """Тестирование типа углов треугольника"""
    assert triangle.angle_type() == expected_angle_type


@pytest.mark.parametrize(
    "triangle, expected_area",
    [
        (
            Triangle(a=3, b=4, c=5), 6,
        ), 
    ],
)
def test_area_of_triangle(triangle, expected_area):
    """Тестирование площади треугольника"""
    assert isclose(triangle.area(), expected_area, abs_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, c, expected_exception",
    [
        (3, 4, 5, None),  # Этот треугольник корректен
        (1, 2, 10, ValueError),  # Несуществующий треугольник
        (-3, 4, 5, ValueError),  # Треугольник с отрицательными сторонами
        (1, 2, 3, ValueError),  # Треугольник с нарушением неравенства
    ],
)
def test_invalid_triangle_creation(a, b, c, expected_exception):
    """Тестирование создания треугольника с неверными данными"""
    if expected_exception:
        with pytest.raises(expected_exception):
            Triangle(a=a, b=b, c=c)
    else:
        triangle = Triangle(a=a, b=b, c=c)
        assert triangle  
