from flask import Flask, request, render_template
from catboost import CatBoostRegressor
import pandas as pd

app = Flask(__name__)

# Загружаем модель
model = CatBoostRegressor()
model.load_model("catboost_model_top11.cbm")

# Список признаков, как в обучении
feature_names = [
    "sqft", "age", "baths", "rating_mean", "stories",
    "distance_mean", "lotsize", "schools_count",
    "propertyType_single family", "beds", "cooling_other"
]

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Получаем данные из формы
        input_data = {f: float(request.form[f]) for f in feature_names}
        
        # Преобразуем в DataFrame
        df = pd.DataFrame([input_data])
        
        # Предсказание
        prediction = model.predict(df)[0]
        return render_template('form.html', prediction=round(prediction, 2))
    
    return render_template('form.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
