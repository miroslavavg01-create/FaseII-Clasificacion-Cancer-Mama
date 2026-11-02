# Fase II - Aplicacion de IA con Docker

Proyecto basado en mi **regresion logistica de la Actividad 5** para clasificar datos publicos del conjunto Wisconsin Breast Cancer Diagnostic

La pantalla web (`index.html`) llama a la API (`app.py`); la API utiliza el archivo `modelo.joblib` y devuelve una clasificacion. Incluimos dos ejemplos publicos del dataset para probar sin escribir 30 numeros.

## Archivos principales

- `app.py`: API y pagina web.
- `index.html`: pantalla con dos botones y resultados.
- `modelo.joblib`: modelo de regresion logistica ya entrenado.
- `entrenar_modelo.py`: vuelve a generar un modelo equivalente.
- `Dockerfile` y `requirements.txt`: contenedor y dependencias.
- `pruebas_api.py`: pruebas funcionales por HTTP.
- `ejemplos.json`: dos ejemplos anonimos del dataset publico.

## Ejecutar con Docker (Docker Desktop encendido)

Abre una terminal **dentro de esta carpeta** y ejecuta:

```bash
docker build -t fase2-ia .
docker run --rm -p 8080:8080 fase2-ia
```

Entra a http://localhost:8080 y pulsa los botones de ejemplo.
Tambien puedes abrir http://localhost:8080/docs para ver la documentacion de la API.

Para ejecutar pruebas, deja el contenedor abierto y usa otra terminal:

```bash
python pruebas_api.py
```

Para detener el contenedor, usa Ctrl+C.

## API

- `GET /`: pagina principal.
- `GET /api/health`: verifica que el servidor responde.
- `GET /api/ejemplos`: entrega los dos ejemplos publicos.
- `POST /api/predict`: recibe `{"valores": [30 numeros]}` y devuelve clase estimada y confianza.

## Resultados y limites

Al reproducir los parametros de la Actividad 5 (C=0.1, semilla 42, division 80/20) se obtuvo accuracy 0.973684 y F1 macro 0.971583 en el conjunto de prueba. El modelo de este repositorio se **reentreno de forma equivalente**; no se exporto directamente la corrida de MLflow anterior. No se han validado predicciones con pacientes reales.

## Estado de validacion

La aplicacion y sus endpoints se probaron localmente en Python. El **build y la ejecucion dentro de Docker** deben verificarse en un equipo con Docker Desktop; no se adjunta evidencia ficticia de ello.

## GitHub y nube

Crea un repositorio nuevo, por ejemplo `Fase2-Docker-Cancer-Mama`, y sube el contenido de esta carpeta. En el manual adjunto estan los pasos para un despliegue opcional en Render mediante Docker.
