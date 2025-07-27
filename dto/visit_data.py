from pydantic import BaseModel


# TODO расширить по необходимости входными параметрами, актуализировать названия
class VisitData(BaseModel):
    go_to_car_card: conint(ge=0, le=1)
    pagination_click: conint(ge=0, le=1)
    photos: conint(ge=0, le=1)
    photos_all: conint(ge=0, le=1)
    sap_search_form_cost_from: conint(ge=0, le=1)
    sap_search_form_cost_to: conint(ge=0, le=1)
    search_form_mark_select: conint(ge=0, le=1)
    search_form_model_select: conint(ge=0, le=1)
    search_form_region: conint(ge=0, le=1)
    search_form_search_btn: conint(ge=0, le=1)
    search_form_search_car_type_select: conint(ge=0, le=1)
    search_kpp: conint(ge=0, le=1)
    sub_car_page: conint(ge=0, le=1)
    sub_landing: conint(ge=0, le=1)
    sub_view_cars_click: conint(ge=0, le=1)
    view_card: conint(ge=0, le=1)
    view_more_click: conint(ge=0, le=1)
    view_new_card: conint(ge=0, le=1)
