# Imports
from fastapi import FastAPI, Body, Depends, HTTPException
from database import engine, Base, SessionLocal 
from sqlalchemy.orm import Session
import models
import schemas

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# create FastAPI() instance
app = FastAPI()

# Handle the HTTP request here.
# Note- instance means task

# GET: get all the tasks
@app.get("/")
async def get_tasks(session: Session=Depends(get_session)):
    # return all the tasks or 404 error(Task not found)
    try:
        # retrive all the instances and return it
        items = session.query(models.Item).all()
        return items
    except:
        raise HTTPException(status_code=404, detail='Task not found')

# POST: add a task
@app.post("/")
async def add_task(item:schemas.Item, session = Depends(get_session)):
    # add the task or raise 400 error('Invalid data entry')
    try:
        # intialize the instance with the POST data
        item = models.Item(task = item.task)
        # add the instance in the database
        session.add(item)
        # commit the changes in the database
        session.commit()
        session.refresh(item)
        # return the object
        return item
    except:
        raise HTTPException(status_code=400, detail='Invalid data entry')

# GET/{pk}/: get single task
@app.get("/{id}")
async def get_task(id:int, session: Session = Depends(get_session)):
    # return a task by id or 404 error('Task not found')
    try:
        # retrive the instance by id
        item = session.query(models.Item).get(id)
        # return the retrived instance
        return item
    except:
        raise HTTPException(status_code=404, detail='Task not found')

# PUT/{pk}/: update a task
@app.put("/{id}")
async def update_task(id:int, item:schemas.Item, session = Depends(get_session)):
    # update the existing task or raise error('Task not found')
    try:
        # retrived the instance by id
        itemObject = session.query(models.Item).get(id)
        # update the instance with the PUT data
        itemObject.task = item.task
        session.commit()
        return itemObject
    except:
        raise HTTPException(status_code=404, detail='Task not found')

# DELETE/{pk}/: delete a task
@app.delete("/{id}")
async def delete_task(id:int, session = Depends(get_session)):
    # delete the task or raise error('Task not found')
    try:
        # retrive the instance by id
        itemObject = session.query(models.Item).get(id)
        # delete the instance
        session.delete(itemObject)
        session.commit()
        session.close()
        return 'Task deleted!'
    except:
        raise HTTPException(status_code=404, detail='Task not found')