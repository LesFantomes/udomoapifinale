from logging import exception
from tokenize import String
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from sqlmodel import Session, select

from .models.mangaModel import  mangas2, mangaUpdate

from .schema.mangaSchema import mangaSchema

from .database import init_db, engine

UdomoAPI = FastAPI()


@UdomoAPI.on_event("startup")
def on_startup():
    init_db()

# Redirect to docs


@UdomoAPI.get("/", tags=["Root"])
async def read_route():
    response = RedirectResponse(url='/docs')
    return response


# Mangas
@UdomoAPI.post("/mangas")
async def createManga(manga: mangas2):
    with Session(engine) as session:
        db_manga = mangaSchema(title=manga.title, author=manga.author, editor=manga.editor)
        session.add(db_manga)
        session.commit()
        return db_manga


@UdomoAPI.get("/mangas/{id}", response_model=mangas2)
async def getOneManga(id: int):
    with Session(engine) as session:
        db_get = session.get(mangas2,id)
        return db_get


@UdomoAPI.get('/mangas')
async def getMangas():
    with Session(engine) as session:
        #manga = db.session.query(mangaSchema).all()
        mangas = session.exec(select(mangas2)).all()
        return mangas


@UdomoAPI.delete('/mangas/{id}')
async def deleteManga(idDelete: int):
    with Session(engine) as session:
        db_delete = session.get(mangas2,idDelete)
        session.delete(db_delete)
        session.commit()
        return "ok"

@UdomoAPI.put('/mangas/{id}')
async def updateManga(id:int,manga:mangaUpdate):
    with Session(engine) as session:
        db_put = session.get(mangas2,id)
        manga_data = db_put.dict(exclude_unset=True)
        for key, value in manga_data.items():
            setattr(db_put,key,value)
        session.add(db_put)
        session.commit()
        session.refresh(db_put)
        return db_put