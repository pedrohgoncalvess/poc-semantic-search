# Swaron semantic search

This repository is a semantic search proof of concept (POC) for the Swaron project. The embeddings were generated using the OpenAI API and stored in postgresql with the help of the vector extension.

# Running project

*you need to have docker installed*
```
docker-compose up
```

# Routes

## Create article with embeddings.

### /article/ 
method Post

Body example:
```json
{
  "title":"A little about the Scala Language.",
  "desc":"Scala is a compiled multiparadigm language that runs on the JVM. It was inspired by Java, Erlang, and Haskell.",
  "link":"https://dev.to/pedrohgoncalves/a-little-about-the-scala-language-5cm0"
}
```

## Querying articles with semantic search.

### /article?term=desired search term

Response body example:
```json
[
 {
  "title": "A little about the Scala Language.",
  "url": "https://dev.to/pedrohgoncalves/a-little-about-the-scala-language-5cm0"
 }
]
```
