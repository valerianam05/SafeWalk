from fastapi import FastAPI
from routes import router 

app = FastAPI(title="SafeWalk API Madagascar 🇲🇬")

app.include_router(router)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Bienvenue sur l'API SafeWalk - Le serveur tourne bien à Madagascar !"
    }