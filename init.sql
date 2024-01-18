create extension if not exists vector;

CREATE TABLE articles (
            id bigserial primary key,
            title text unique,
            url text,
            description text,
            title_embedding vector(1536)
            );