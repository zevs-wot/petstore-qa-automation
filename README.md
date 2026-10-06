### Тестирование API

Проект включает тестирование CRUD-операций для Swagger Petstore API:

## Postman коллекция
- Файл: `MyPetProject.postman_collection.json`
- Окружение: `MyNewEnvironment.postman_environment.json`
- 5 запросов (POST, GET, PUT, DELETE, GET(негативный тест))
- 10 автоматических проверок

## Python автотесты
- Файл: `test_petstore.py`
- Стек: pytest, requests
- 5 тестов, покрывающих полный CRUD цикл

## Запуск
```bash
# Python тесты
pytest test_petstore.py -v

# Postman
Импорт коллекции в Postman → запуск через Collection Runner