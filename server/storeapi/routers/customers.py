from fastapi import APIRouter, HTTPException

from storeapi.database import customers_table, database
from storeapi.models.customers import (CustomersIn, Customers)

router = APIRouter()

async def find_customer(customer_id: int):
    query = customers_table.select().where(customers_table.c.id == customer_id)
    return await database.fetch_one(query)

@router.post("/create_customers", response_model=Customers, status_code=201)
async def create_customers(customers: CustomersIn):
    data = customers.model_dump()
    query = customers_table.insert().values(**data)
    last_id = await database.execute(query)
    return { **data, "id": last_id }

@router.get("/customers/{customer_id}", response_model=Customers, status_code=200)
async def get_customers(customer_id: int):
    port = await find_customer(customer_id)

    if not port:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customer_id} not found")
    
    return port

@router.get("/customers", response_model=list[Customers], status_code=200)
async def get_all_customers():
    query = customers_table.select()
    ports = await database.fetch_all(query)
    return ports

@router.put("/update_customers/{customers_id}", response_model=Customers, status_code=201)
async def update_customers(customers_id: int, customers: CustomersIn):
    executing_port = await find_customer(customers_id)

    if not executing_port:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customers_id} not found")
    
    data = customers.model_dump()

    query = customers_table.update().where(customers_table.c.id == customers_id).values(**data)
    await database.execute(query)

    update_customer = await find_customer(customers_id)
    return update_customer


@router.delete("/delete_customers/{customers_id}", response_model=bool, status_code=201)
async def delete_customers(customers_id: int):
    executing_port = await find_customer(customers_id)

    if not executing_port:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customers_id} not found")
    
    query = customers_table.delete().where(customers_table.c.id == customers_id)
    await database.execute(query)

    return True