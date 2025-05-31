import pandas as pd
from catboost import CatBoostRegressor

# Загрузка модели
model = CatBoostRegressor()
model.load_model("catboost_model_top11.cbm")

# Пример входных данных (top-11 признаков)
data = {
    "sqft": 2000,
    "age": 15,
    "baths": 2,
    "rating_mean": 4.3,
    "stories": 2,
    "distance_mean": 3.0,
    "lotsize": 6000,
    "schools_count": 4,
    "propertyType_single family": 1,
    "beds": 3,
    "cooling_other": 0
}

# Преобразуем в DataFrame с одним наблюдением
df = pd.DataFrame([data])

# Предсказание
predicted_price = model.predict(df)[0]

# Вывод
print(f"💰 Предсказанная цена: {predicted_price:,.2f}")
