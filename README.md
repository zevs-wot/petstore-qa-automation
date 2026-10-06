# Petstore QA Automation

Тестирование Swagger Petstore API (CRUD операции)

##  Что внутри

### API тесты (Python + pytest)
- 5 тестов, покрывающих полный CRUD цикл
- Независимые тесты с изоляцией состояния
- Проверка позитивных и негативных сценариев
- Стек: Python 3.11, pytest, requests

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

# Запуск всех API тестов
pytest api_tests/ -v

# Запуск конкретного файла
pytest api_tests/test_petstore.py -v