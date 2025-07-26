from pydantic import BaseModel


# TODO расширить по необходимости входными параметрами, актуализировать названия
class VisitData(BaseModel):
    go_to_car_card: str
    pagination_click: str
    photos: str
    photos_all: str
    quiz_show: str
    sap_search_form_cost_from: str
    sap_search_form_cost_to: str
    search_form_mark_select: str
    search_form_model_select: str
    search_form_region: str
    search_form_search_btn: str
    search_form_search_car_type_select: str
    search_kpp: str
    showed_number_ads: str
    sub_car_page: str
    sub_landing: str
    sub_view_cars_click: str
    view_card: str
    view_more_click: str
    view_new_card: str
    custom_target: str
