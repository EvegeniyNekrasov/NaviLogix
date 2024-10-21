from pydantic import BaseModel


class VouyagesIn(BaseModel):
    name: str
    vessel_id: int
    route_id: int
    departure_date: str
    arrival_date: str
    status: str


class Voyages(VouyagesIn):
    id: int
