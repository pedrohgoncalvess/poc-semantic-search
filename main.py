import uvicorn
from fastapi import FastAPI
from api_model.article import Article
from dotenv import load_dotenv
from embedding_util import get_embedding
from database.connection import ConnectToDatabase

load_dotenv()

app = FastAPI()


@app.get("/article")
async def get_articles(term: str):
    query_embedding = get_embedding(term)
    db = ConnectToDatabase()

    return db.get_similar_articles(query_embedding)


@app.post("/article", status_code=201)
async def insert_article(article_infos: Article):
    db = ConnectToDatabase()

    embeddings = get_embedding(article_infos.title)

    db.insert_into_database(article_infos.title, article_infos.desc, article_infos.link, embeddings)

    return "Created"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0", log_level="info", reload=True)
