from flask import Flask, render_template, request
import folium
import geopandas as gpd
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Cargar archivos del modelo
modelo = joblib.load("data/modelo_riesgo_inundacion.pkl")
scaler = joblib.load("data/scaler.pkl")
label_encoder = joblib.load("data/label_encoder.pkl")
features_modelo = joblib.load("data/features_modelo.pkl")

def color_riesgo(riesgo):
    if riesgo == "Alto":
        return "red"
    elif riesgo == "Medio":
        return "orange"
    elif riesgo == "Bajo":
        return "green"
    else:
        return "gray"

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    probabilidad_resultado = None

    # Si el usuario envía el formulario
    if request.method == "POST":
        valores = []

        for feature in features_modelo:
            valor = float(request.form[feature])
            valores.append(valor)

        datos_usuario = pd.DataFrame([valores], columns=features_modelo)
        datos_escalados = scaler.transform(datos_usuario)

        prediccion = modelo.predict(datos_escalados)[0]
        probabilidades = modelo.predict_proba(datos_escalados)[0]

        resultado = label_encoder.inverse_transform([prediccion])[0]
        probabilidad_resultado = round(max(probabilidades) * 100, 2)

    # Crear mapa
    mapa = folium.Map(
        location=[-2.2, -79.9],
        zoom_start=8,
        width="100%",
        height=600
    )

    parroquias = gpd.read_file("data/parroquias_guayas.geojson")
    predicciones = pd.read_csv("data/predicciones_finales.csv")

    # Unir por nombre de parroquia
    predicciones["DPA_PARROQ"] = predicciones["DPA_PARROQ"].astype(str).str.zfill(6)
    parroquias["DPA_PARROQ"] = parroquias["DPA_PARROQ"].astype(str)

    riesgo_dict = dict(zip(predicciones["DPA_PARROQ"], predicciones["riesgo_predicho"]))
    prob_dict = dict(zip(predicciones["DPA_PARROQ"], predicciones["probabilidad_max"]))

    def estilo(feature):
        codigo = str(feature["properties"]["DPA_PARROQ"])
        riesgo = riesgo_dict.get(codigo, "Sin dato")

        return {
            "fillColor": color_riesgo(riesgo),
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6
        }

    parroquias["riesgo"] = parroquias["DPA_PARROQ"].map(riesgo_dict).fillna("Sin dato")
    parroquias["probabilidad"] = parroquias["DPA_PARROQ"].map(prob_dict).fillna("Sin dato")

    folium.GeoJson(
        parroquias,
        name="Riesgo de inundación",
        style_function=estilo,
        tooltip=folium.GeoJsonTooltip(
            fields=["DPA_DESPAR", "DPA_DESCAN", "DPA_DESPRO"],
            aliases=["Parroquia:", "Cantón:", "Provincia:"]
        ),
        popup=folium.GeoJsonPopup(
            fields=["DPA_DESPAR", "DPA_DESCAN", "DPA_DESPRO", "riesgo", "probabilidad"],
            aliases=["Parroquia:", "Cantón:", "Provincia:", "Riesgo:", "Probabilidad:"],
            localize=True
        )
    ).add_to(mapa)

    mapa_html = mapa._repr_html_()

    return render_template(
        "index.html",
        mapa=mapa_html,
        resultado=resultado,
        probabilidad_resultado=probabilidad_resultado,
        features=features_modelo
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )