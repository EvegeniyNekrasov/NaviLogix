from fastapi import APIRouter, HTTPException

from storeapi.database import ports_table, database
from storeapi.models.ports import (Ports, PortsIn)

router = APIRouter()

async def fint_port(port_id: int):
    query = ports_table.select().where(ports_table.c.id == port_id)
    return await database.fetch_one(query)

@router.post("/create_port", response_model=Ports, status_code=201)
async def create_ports(ports: PortsIn):
    data = ports.model_dump()
    query = ports_table.insert().values(**data)
    last_id = await database.execute(query)
    return { **data, "id": last_id }

@router.get("/ports/{port_id}", response_model=Ports, status_code=200)
async def get_port(port_id: int):
    port = await fint_port(port_id)

    if not port:
        raise HTTPException(status_code=404, detail="Port not found")
    
    return port

@router.get("/ports", response_model=list[Ports], status_code=200)
async def get_all_ports():
    query = ports_table.select()
    ports = await database.fetch_all(query)
    return ports

@router.put("/update_port/{port_id}", response_model=Ports, status_code=201)
async def update_port(port_id: int, ports: PortsIn):
    executing_port = await fint_port(port_id)

    if not executing_port:
        raise HTTPException(status_code=404, detail=f"Port with id: {port_id} not found")
    
    data = ports.model_dump()

    query = ports_table.update().where(ports_table.c.id == port_id).values(**data)
    await database.execute(query)

    update_port = await fint_port(port_id)
    return update_port


@router.delete("/delete_port/{port_id}", response_model=bool, status_code=201)
async def delete_port(port_id: int):
    executing_port = await fint_port(port_id)

    if not executing_port:
        raise HTTPException(status_code=404, detail=f"Port with id: {port_id} not found")
    
    query = ports_table.delete().where(ports_table.c.id == port_id)
    await database.execute(query)

    return True