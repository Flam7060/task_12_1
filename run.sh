#!/bin/bash
# GPT круто пишет баш)
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry не установлен. Установите его перед продолжением: https://python-poetry.org/docs/"
    exit 1
fi

if poetry env info &> /dev/null; then
    echo "🌟 Виртуальное окружение уже существует."
else
    echo "📦 Установка зависимостей и создание окружения..."
    poetry install || { echo "❌ Ошибка при установке зависимостей!"; exit 1; }
fi

echo "🧪 Запуск тестов..."
poetry run pytest || { echo "❌ Тесты завершились с ошибкой!"; exit 1; }

echo "🚀 Запуск приложения..."
poetry run python app/main.py || { echo "❌ Ошибка запуска приложения!"; exit 1; }
