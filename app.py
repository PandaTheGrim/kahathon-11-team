import joblib
from fastapi import FastAPI

from dto.visit_data import VisitData

app = FastAPI()
model = joblib.load('./model/model.pkl')


@app.post("/predict")
def predict(data: VisitData):
    features = [
        data.utm_source,
        data.geo_country,
        data.device_category
    ]

    pred = model.predict([features])[0]

    return {"prediction_result": int(pred)}
