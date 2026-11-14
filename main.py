import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(
    title="My AI Robot",
    description="Bangla and English AI Assistant",
    version="1.0"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "My AI Robot is running!"
    }

@app.get("/test")
def test():
    return {"status": "OK"}

@app.post("/chat")
def chat(request: ChatRequest):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is missing"
        )

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5.5",
            instructions=(
                "You are Soyon, a friendly AI robot assistant. "
                "Speak naturally in Bangla or English. "
                "Reply in the language used by the user. "
                "Be helpful, friendly and educational."
            ),
            input=request.message
        )

        return {
            "status": "success",
            "reply": response.output_text
        }

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI service request failed. Check server logs."
        )
