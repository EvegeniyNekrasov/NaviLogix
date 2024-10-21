from fastapi import APIRouter, HTTPException

from storeapi.database import vessels_table, database
from storeapi.models.vessels import (Vessels, VesselsIn)

router = APIRouter()

async def find_vessel(vessel_id: int):
    query = vessels_table.select().where(vessels_table.c.id == vessel_id)
    return await database.fetch_one(query)


@router.post("/create_vessels", response_model=Vessels, status_code=201)
async def create_vessels(vessels: VesselsIn):
    data = vessels.model_dump()
    query = vessels_table.insert().values(**data)

    last_id = await database.execute(query)
    return { **data, "id": last_id }

@router.get("/vessels", response_model=list[Vessels], status_code=200)
async def get_all_vessels():
    query = vessels_table.select()
    vessels = await database.fetch_all(query)
    return vessels

@router.get("/vessels/{vessel_id}", response_model=Vessels, status_code=200)
async def get_vessel(vessel_id: int):
    vessel = await find_vessel(vessel_id)

    if not vessel:
        raise HTTPException(status_code=404, detail=f"Vessel with id: {vessel_id} not found")
    
    return vessel