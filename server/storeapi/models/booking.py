from pydantic import BaseModel


class BookingIn(BaseModel):
    customer_id: int
    voyage_id: int
    status: str
    total_weight: float
    total_volume: float
    number_of_containers: int


class Booking(BookingIn):
    id: int
