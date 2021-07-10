from typing import List
from fastapi import APIRouter, status, HTTPException
from db_todo_app.Schemas import ItemsSchemaIn, ItemsSchema
from db_todo_app.db import database, Items

router = APIRouter(
    tags=["Items"]
)


@router.post('/createitem/', status_code=status.HTTP_201_CREATED,
             response_model=ItemsSchema, tags=['Create'], summary='Creates item.')
async def insert_item(item: ItemsSchemaIn):
    """
                    Creates an Item with following information:

                    - **Title**: Add item's title. This field must be filled. --required
                    - **Description**: Add description for an item. This field can be left null. --optional

    """
    query = Items.insert().values(title=item.title, description=item.description)
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@router.get('/getitems/', response_model=List[ItemsSchema]
            , tags=['Get'], summary='gets list of items in the database.')
async def get_items():
    """
                    Returns list of **items**.

    """
    query = Items.select()
    return await database.fetch_all(query=query)


@router.get('/getitem/{id}/', response_model=ItemsSchema,
            tags=['Get'], summary='Returns an item with details.')
async def get_details(id:int):
    """
                    Returns detail of **item** by providing id.

    """
    query = Items.select().where(id == Items.c.id)
    my_item = await database.fetch_one(query=query)

    if not my_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return {**my_item}


@router.put('/updateitem/{id}/', response_model=ItemsSchema
            , tags=['Update'], summary='Updates the record.')
async def update_item(id: int, item: ItemsSchemaIn):
    """
                    Updates **Items** by providing id and update details.

    """
    query = Items.update().where(Items.c.id == id).values(title=item.title, description=item.description)
    await database.execute(query)

    return {**item.dict(), "id": id}


@router.delete('/removeitem/{id}/', status_code=status.HTTP_204_NO_CONTENT,
               tags=['Delete'], summary="removes item's data.")
async def delete_item(id:int):
    """
                    Removes an **Item** by providing id.

    """
    query = Items.delete().where(Items.c.id == id)
    await database.execute(query)

    return {"message": "Item deleted"}
