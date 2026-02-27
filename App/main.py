from fastapi import FastAPI
from routes import router
app = FastAPI(title="SafeWalk API Madagascar 🇲🇬")

# On connecte les routes au moteur principal
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API SafeWalk - Le serveur tourne bien !"}