# API y pagina web de la Fase II. Solo para demostracion academica.
import json
import math
import os
from pathlib import Path

import joblib
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

CARPETA = Path(__file__).resolve().parent
modelo = joblib.load(CARPETA / "modelo.joblib")  # Modelo creado dentro de este proyecto.
ejemplos = json.loads((CARPETA / "ejemplos.json").read_text(encoding="utf-8"))
app = FastAPI(title="Fase II: demostracion de clasificacion", version="1.0")

class Entrada(BaseModel):
    valores: list[float]

@app.get("/")
def inicio():
    return FileResponse(CARPETA / "index.html")

@app.get("/api/health")
def salud():
    return {"estado": "ok", "modelo": "regresion_logistica"}

@app.get("/api/ejemplos")
def datos_ejemplo():
    return ejemplos

@app.post("/api/predict")
def predecir(entrada: Entrada):
    if len(entrada.valores) != 30 or not all(math.isfinite(x) for x in entrada.valores):
        raise HTTPException(status_code=422, detail="Se necesitan 30 numeros finitos.")
    clase = int(modelo.predict([entrada.valores])[0])
    confianza = float(max(modelo.predict_proba([entrada.valores])[0]))
    return {
        "clase_estimada": "Benigno" if clase == 1 else "Maligno",
        "confianza_modelo": round(confianza, 4),
        "aviso": "Resultado academico. No usar para diagnosticos medicos."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
