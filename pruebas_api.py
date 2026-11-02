# Prueba la API con la aplicacion ejecutandose en localhost:8080.
import json
import os
import urllib.error
import urllib.request

URL = os.environ.get("URL", "http://127.0.0.1:8080")

def pedir(ruta, datos=None):
    cuerpo = None if datos is None else json.dumps(datos).encode("utf-8")
    solicitud = urllib.request.Request(
        URL + ruta, data=cuerpo,
        headers={"Content-Type": "application/json"} if cuerpo else {}
    )
    try:
        with urllib.request.urlopen(solicitud, timeout=12) as res:
            return res.status, res.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8")

resultados = []
def prueba(nombre, correcto):
    resultados.append((nombre, correcto))
    print(("OK" if correcto else "ERROR") + " - " + nombre)

s, html = pedir("/")
prueba("Pagina web", s == 200 and "Demostracion" in html)
s, texto = pedir("/api/health")
prueba("Salud de API", s == 200 and json.loads(texto)["estado"] == "ok")
s, texto = pedir("/api/ejemplos")
ejemplos = json.loads(texto) if s == 200 else []
prueba("Dos ejemplos con 30 valores", s == 200 and len(ejemplos) == 2 and all(len(e["valores"]) == 30 for e in ejemplos))
for n, ejemplo in enumerate(ejemplos):
    s, texto = pedir("/api/predict", {"valores": ejemplo["valores"]})
    prueba("Prediccion ejemplo " + str(n+1), s == 200 and json.loads(texto)["clase_estimada"] in ["Benigno", "Maligno"])
s, _ = pedir("/api/predict", {"valores": [1,2]})
prueba("Rechaza 2 valores (422)", s == 422)
s, _ = pedir("/api/predict", {"valores": ["texto"]*30})
prueba("Rechaza texto (422)", s == 422)
s, _ = pedir("/api/predict", {"valores": [1]*31})
prueba("Rechaza 31 valores (422)", s == 422)
s, _ = pedir("/api/predict", {"otro_campo": [1]*30})
prueba("Rechaza ausencia de valores (422)", s == 422)
print("Resumen:", sum(v for _, v in resultados), "de", len(resultados), "correctas")
if not all(v for _, v in resultados):
    raise SystemExit(1)
