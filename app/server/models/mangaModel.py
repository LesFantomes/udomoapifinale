from sqlmodel import SQLModel, Field


class mangaBase(SQLModel):
    title: str
    author: str
    editor: str


class mangas2(mangaBase, table=True):
    idManga: int = Field(default=None, primary_key=True)


class mangaCreate(mangaBase):
    pass


class mangaDelete(mangaBase):
    pass


class mangaUpdate(mangaBase):
    title: str
    author: str
    editor: str
