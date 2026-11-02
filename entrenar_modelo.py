# Reproduce el modelo equivalente a la regresion logistica de Actividad 5.
import joblib
from pathlib import Path
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

datos = load_breast_cancer(as_frame=True)
X_ent, _, y_ent, _ = train_test_split(
    datos.data, datos.target, test_size=0.2, stratify=datos.target, random_state=42
)
modelo = Pipeline([
    ("escalado", StandardScaler()),
    ("modelo", LogisticRegression(C=0.1, max_iter=3000, random_state=42))
])
modelo.fit(X_ent, y_ent)
joblib.dump(modelo, Path(__file__).with_name("modelo.joblib"))
print("Modelo generado en modelo.joblib")
