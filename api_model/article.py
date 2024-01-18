from pydantic import BaseModel

class Article(BaseModel):
    title: str
    desc: str
    link: str
