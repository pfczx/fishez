from os.path import curdir

from fastapi import FastAPI
from sqlalchemy import Select

from app.db.database import engine,SessionDep
from sqlmodel import Session, select,SQLModel
from app.db.models import Flashcards


app = FastAPI()

@app.on_event("startup")
def on_startup():


    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        flashcards = session.exec(Select(Flashcards)).all()
        last_id  = session.exec(select(Flashcards.id)).order_by(Flashcards.id.desc()).first()
        if last_id is not None:
            curr_id = last_id+1
        else:
            curr_id = 1



@app.get("/")
async def read_root():
    return "works"

@app.post("/flashcards")
async def create_set(session:SessionDep,id : int,title : str,words_dict: dict[str,str]):
    flashcards = Flashcards(id=id,title=title,flashcards_set=words_dict)
    session.add(flashcards)
    session.commit()

@app.get("/flashcards/{id}")
async def read_set(session:SessionDep,id:int):
    return session.get(Flashcards,id)