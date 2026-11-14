import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="Soyon AI Robot")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class Chat(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Soyon AI is Online!"}

@app.post("/chat")
def chat(data: Chat):
    try:
        response = client.responses.create(
            model="gpt-5.5",
            instructions="You are Soyon, a friendly Bangla and English AI assistant.",
            input=data.message
        )
        return {"reply": response.output_text}

    except Exception as e:
        return {"error": str(e)}
