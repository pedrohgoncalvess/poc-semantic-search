import os
import psycopg2 as pg


class ConnectToDatabase:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.conn = pg.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password)

    def get_similar_articles(self, query_embedding: list[float]) -> dict[str:str]:
        cursor = self.conn.cursor()
        cursor.execute("select title, url FROM articles ORDER BY title_embedding <=> CAST(%s AS VECTOR) LIMIT 1",
                       (query_embedding,))
        result = [{"title": row[0], "url": row[1]} for row in cursor.fetchall()]
        self.conn.close()
        return result

    def insert_into_database(self, title: str, desc: str, link: str, embeddings: list[float]) -> None:
        cursor = self.conn.cursor()
        cursor.execute("insert into articles (title, description, url, title_embedding) values (%s, %s, %s, %s)",
                       (title, desc, link, embeddings))
        self.conn.commit()
        self.conn.close()
