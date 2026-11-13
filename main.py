from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "My Bangla AI Robot is running!"
    }

@app.get("/chat")
def chat(message: str):
    return {
        "user_message": message,
        "reply": "তোমার কথা শুনছি।"
    }
