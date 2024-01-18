from openai import OpenAI

def get_embedding(text: str, model: str = "text-embedding-ada-002") -> list[float]:
    client = OpenAI()
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding
