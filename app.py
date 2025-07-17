import joblib
from fastapi import FastAPI

from dto.visit_data import VisitData

app = FastAPI()
# прогружаем нашу модель
model = joblib.load('./model/model.pkl')


@app.post("/predict")
def predict(data: VisitData):
    # тут складываем фичи, которые подаем на вход модели в нужном порядке
    features = [
        data.utm_source,
        data.geo_country,
        data.device_category
    ]
    # вызываем "предсказывалку"
    pred = model.predict([features])[0]
    # возвращаем 1 или 0
    return {"prediction_result": int(pred)}
