import pytest
import sqlite3

## Имитация подключения к базе данных
@pytest.fixture
def db_connection():
    """
    Создание временной базы данных для тестов
    """
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    """
    Создание таблицы 'pets'
    """
    cursor.execute("""
        CREATE TABLE pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            status TEXT
        )
    """)

    connection.commit()
    yield connection

    connection.close()

def test_pet_saved_in_db(db_connection):
    """
    Данные из API корректно сохраняются в БД
    """
    cursor = db_connection.cursor()

    ## Имитация сохранения питомца в БД
    pet_id = 777888999
    cursor.execute(
        "INSERT INTO pets (id, name, status) VALUES (?, ?, ?)",
        (pet_id, "qa_automation_dog", "available")
    )
    db_connection.commit()

    ## Проверка наличия питомца
    cursor.execute(
        "SELECT name, status FROM pets WHERE id = ?", (pet_id, )
    )
    result = cursor.fetchone()

    assert result is not None, "Запись не найдена в БД"
    assert result[0] == "qa_automation_dog", "Имя в БД не совпадает"
    assert result[1] == "available", "Статус в БД не совпадает"