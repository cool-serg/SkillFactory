import requests

# Пример входных данных
payload = {
    "sqft": 1800,
    "age": 20,
    "baths": 2,
    "rating_mean": 4.5,
    "stories": 2,
    "distance_mean": 3.2,
    "lotsize": 5000,
    "schools_count": 3,
    "propertyType_single family": 1,  # 1 = да, 0 = нет
    "beds": 3,
    "cooling_other": 0
}

# Отправка запроса к серверу
response = requests.post("http://localhost:5000/predict", json=payload)

# Вывод результата
if response.status_code == 200:
    print("💰 Предсказанная цена:", response.json()["predicted_price"])
else:
    print("Ошибка:", response.text)
