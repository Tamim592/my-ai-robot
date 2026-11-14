import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

class Chat(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Soyon AI is Online!"}

@app.post("/chat")
def chat(data: Chat):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-5.5",
        input=data.message
    )

    return {"reply": response.output_text}
