from pydantic import BaseModel


# TODO расширить по необходимости входными параметрами, актуализировать названия
class VisitData(BaseModel):
    utm_source: str
    geo_country: str
    device_category: str
