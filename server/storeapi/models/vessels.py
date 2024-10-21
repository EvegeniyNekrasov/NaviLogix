from pydantic import BaseModel


class VesselsIn(BaseModel):
    name: str
    imo_number: str
    mmsi_number: str
    call_sign: float
    flag: float
    capacity: int
    built_year: int
    vessel_type: str


class Vessels(VesselsIn):
    id: int
