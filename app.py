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
        data.go_to_car_card,
        data.pagination_click,
        data.photos,
        data.photos_all,
        data.sap_search_form_cost_from,
        data.sap_search_form_cost_to,
        data.search_form_mark_select,
        data.search_form_model_select,
        data.search_form_region,
        data.search_form_search_btn,
        data.search_form_search_car_type_select,
        data.search_kpp,
        data.sub_car_page,
        data.sub_landing,
        data.sub_view_cars_click,
        data.view_card,
        data.view_more_click,
        data.view_new_card
    ]
    # вызываем "предсказывалку"
    pred = model.predict([features])[0]
    # возвращаем 1 или 0
    return {"prediction_result": int(pred)}
