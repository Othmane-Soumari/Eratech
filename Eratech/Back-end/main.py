from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permettre les requêtes CORS (utile pour le développement local avec un frontend React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines (à ajuster en production)
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les en-têtes
)

@app.get("/api/data")
def get_data():
    return {"message": "Hello from FastAPI!"}
