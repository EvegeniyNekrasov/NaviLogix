import logging

from databases import Database
from fastapi import APIRouter, HTTPException, Response
from typing import Type, List
from pydantic import BaseModel
from sqlalchemy import Table


def get_crud_router(
    table: Table,
    model_in: Type[BaseModel],
    model_out: Type[BaseModel],
    prefix: str,
    database: Database,
    logger: logging.Logger,
) -> APIRouter:
    router = APIRouter()

    async def find_item(item_id: int):
        logger.debug(f"Buscando {prefix} con id: {item_id}")
        query = table.select().where(table.c.id == item_id)
        logger.debug(query)
        return await database.fetch_one(query)

    @router.post(f"/create_{prefix}", response_model=model_out, status_code=201)
    async def create_item(item: model_in, response: Response):
        data = item.model_dump()
        logger.debug(f"Creando nuevo {prefix}: {data}")
        query = table.insert().values(**data)
        last_id = await database.execute(query)
        response.status_code = 201  # Aseguramos el código de estado
        logger.info(
            f"{prefix.capitalize()} creado con id: {last_id} - Código de estado: {response.status_code}"
        )
        return {**data, "id": last_id}

    @router.get(f"/{prefix}/{{item_id}}", response_model=model_out)
    async def get_item(item_id: int, response: Response):
        item = await find_item(item_id)
        if not item:
            response.status_code = 404
            logger.warning(
                f"{prefix.capitalize()} con id: {item_id} no encontrado - Código de estado: {response.status_code}"
            )
            raise HTTPException(
                status_code=404,
                detail=f"{prefix.capitalize()} con id: {item_id} no encontrado",
            )
        response.status_code = 200
        logger.info(
            f"{prefix.capitalize()} encontrado: {item} - Código de estado: {response.status_code}"
        )
        return item

    @router.get(f"/{prefix}", response_model=List[model_out])
    async def get_all_items(response: Response):
        logger.debug(f"Obteniendo todos los {prefix}")

        query = table.select()
        logger.debug(query)

        items = await database.fetch_all(query)

        response.status_code = 200
        logger.info(
            f"{len(items)} {prefix} encontrados - Código de estado: {response.status_code}"
        )

        return items

    @router.put(f"/update_{prefix}/{{item_id}}", response_model=model_out)
    async def update_item(item_id: int, item: model_in, response: Response):
        existing_item = await find_item(item_id)

        if not existing_item:
            response.status_code = 404
            logger.warning(
                f"No se puede actualizar. {prefix.capitalize()} con id: {item_id} no encontrado - Código de estado: {response.status_code}"
            )

            raise HTTPException(
                status_code=404,
                detail=f"{prefix.capitalize()} con id: {item_id} no encontrado",
            )

        data = item.model_dump()
        logger.debug(f"Actualizando {prefix} con id: {item_id}, datos: {data}")

        query = table.update().where(table.c.id == item_id).values(**data)
        logger.debug(query)

        await database.execute(query)
        updated_item = await find_item(item_id)

        response.status_code = 200
        logger.info(
            f"{prefix.capitalize()} con id: {item_id} actualizado - Código de estado: {response.status_code}"
        )

        return updated_item

    @router.delete(f"/delete_{prefix}/{{item_id}}", response_model=bool)
    async def delete_item(item_id: int, response: Response):
        existing_item = await find_item(item_id)
        if not existing_item:
            response.status_code = 404
            logger.warning(
                f"No se puede eliminar. {prefix.capitalize()} con id: {item_id} no encontrado - Código de estado: {response.status_code}"
            )

            raise HTTPException(
                status_code=404,
                detail=f"{prefix.capitalize()} con id: {item_id} no encontrado",
            )

        logger.debug(f"Eliminando {prefix} con id: {item_id}")
        query = table.delete().where(table.c.id == item_id)

        logger.debug(query)
        await database.execute(query)

        response.status_code = 200
        logger.info(
            f"{prefix.capitalize()} con id: {item_id} eliminado - Código de estado: {response.status_code}"
        )
        return True

    return router
