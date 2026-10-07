# Petstore QA Automation

Тестирование Swagger Petstore API (CRUD операции) с валидацией данных в БД

##  Что внутри

### API тесты (Python + pytest)
- 5 тестов, покрывающих полный CRUD цикл
- Независимые тесты с изоляцией состояния
- Проверка позитивных и негативных сценариев
- Стек: Python 3.11, pytest, requests

### SQL валидация (Python + sqlite3)
- Проверка корректности сохранения данных в БД
- Проверка удаления записей
- Имитация работы с реальной базой данных
- Стек: Python, sqlite3, pytest fixtures

### Postman коллекция
- 5 запросов (POST, GET, PUT, DELETE, GET(негативный тест))
- 10 автоматических проверок
- Переменные окружения
- Интеграционные проверки (GET после DELETE)

## Запуск

### Python тесты
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск только SQL тестов
pytest api_tests/test_db_mock.py -v

# Запуск только API тестов Petstore
pytest api_tests/test_petstore.py -v