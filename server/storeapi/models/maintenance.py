from pydantic import BaseModel


class MaintananceIn(BaseModel):
    vessel_id: int
    description: str
    maintenance_date: str
    cost: float


class Maintanance(MaintananceIn):
    id: int
