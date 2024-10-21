from fastapi import APIRouter, HTTPException
from typing import Type, List
from pydantic import BaseModel
from databases import Database
from sqlalchemy import Table

def get_crud_router(
        table: Table,
        model_in: Type[BaseModel],
        model_out: Type[BaseModel],
        prefix: str,
        database: Database
) -> APIRouter:
    router = APIRouter()

    async def find_item(item_id: int):
        query = table.select().where(table.c.id == item_id)
        return await database.fetch_one(query)
    

    @router.post(f"/create_{prefix}", response_model=model_out, status_code=201)
    async def create_item(item: model_in):
        data = item.model_dump()
        query = table.insert().values(**data)
        last_id = await database.execute(query)
        return { **data, "id": last_id }
    
    @router.get(f"/{prefix}/{{item_id}}", response_model=model_out, status_code=200)
    async def get_item(item_id: int):
        item = await find_item(item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{prefix.capitalize()} con id: {item_id} no encontrado")
        return item
    
    @router.get(f"/{prefix}", response_model=List[model_out], status_code=200)
    async def get_all_items():
        query = table.select()
        items = await database.fetch_all(query)
        return items
    
    @router.put(f"/update_{prefix}/{{item_id}}", response_model=model_out, status_code=201)
    async def update_item(item_id: int, item: model_in):
        existing_item = await find_item(item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"{prefix.capitalize()} con id: {item_id} no encontrado")
        data = item.model_dump()
        query = table.update().where(table.c.id == item_id).values(**data)
        await database.execute(query)
        updated_item = await find_item(item_id)
        return updated_item
    
    @router.delete(f"/delete_{prefix}/{{item_id}}", response_model=bool, status_code=201)
    async def delete_item(item_id: int):
        existing_item = await find_item(item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"{prefix.capitalize()} con id: {item_id} no encontrado")
        query = table.delete().where(table.c.id == item_id)
        await database.execute(query)
        return True

    return router