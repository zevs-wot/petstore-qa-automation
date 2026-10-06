import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 777888999

def test_add_pet():
    """ Добавление питомца """
    payload = {
        "id": PET_ID,
        "name": "qa_automation_dog",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "qa_automation_dog"

def test_get_pet():
    """ Получение питомца по ID """
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")

    assert response.status_code == 200
    assert response.json()["name"] == "qa_automation_dog"

def test_update_pet():
    """ Обновление данных питомца """
    payload = {
        "id": PET_ID,
        "name": "qa_automation_dog_updated",
        "status": "pending"
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload)

    assert response.status_code == 200
    assert response.json()["name"] == "qa_automation_dog_updated"
    assert response.json()["status"] == "pending"

def test_delete_pet():
    """ Удаление питомца """
    response = requests.delete(f"{BASE_URL}/pet/{PET_ID}")

    assert response.status_code == 200
    assert response.json()["message"] == str(PET_ID)

def test_get_deleted_pet_negative():
    """ Проверка питомца после удаления - негативный тест """
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")

    assert response.status_code == 404
    assert response.json()["message"] == "Pet not found"