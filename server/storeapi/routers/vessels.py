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

@router.put("/update_vessels/{vessel_id}", response_model=Vessels, status_code=201)
async def update_port(vessel_id: int, ports: VesselsIn):
    executing_vessels = await find_vessel(vessel_id)

    if not executing_vessels:
        raise HTTPException(status_code=404, detail=f"Vessel with id: {vessel_id} not found")
    
    data = ports.model_dump()

    query = vessels_table.update().where(vessels_table.c.id == vessel_id).values(**data)
    await database.execute(query)

    update_port = await find_vessel(vessel_id)
    return update_port


@router.delete("/delete_vessels/{vessel_id}", response_model=bool, status_code=201)
async def delete_port(vessel_id: int):
    executing_vessel = await find_vessel(vessel_id)

    if not executing_vessel:
        raise HTTPException(status_code=404, detail=f"Vessel with id: {vessel_id} not found")
    
    query = vessels_table.delete().where(vessels_table.c.id == vessel_id)
    await database.execute(query)

    return True