# Proyecto-Grupo-A-Clasificacion-del-riesgo-de-inundacion-por-parroquia
Las inundaciones representan uno de los desastres naturales más frecuentes y devastadores en Ecuador. La provincia del Guayas concentra el mayor riesgo, afectando miles de familias, infraestructura y actividades agrícolas cada año. Comprender y clasificar este riesgo por parroquia es clave para la toma de decisiones.

# Clasificación del Riesgo de Inundación por Parroquia – Provincia del Guayas

## Descripción

Este proyecto desarrolla un modelo de aprendizaje automático para clasificar el riesgo de inundación de las parroquias de la provincia del Guayas en tres categorías:

- 🟢 Bajo
- 🟡 Medio
- 🔴 Alto

Para ello se integran variables climáticas, geográficas, hidrológicas, demográficas e históricas. Posteriormente se entrenan y comparan diferentes modelos de clasificación hasta seleccionar el de mejor rendimiento.

---

# Estructura del Proyecto

```
Proyecto-Grupo-A-Clasificacion-del-riesgo-de-inundacion-por-parroquia/
│
├── README.md
├── requirements.txt
├── parroquias_guayas.geojson
├── Link de la aplicación Web
│
├── Archivos csv/
│   ├── predicciones_finales.csv
│   └── tabla_comparativa_modelos.csv
│   
├── Archivos.pkl/
│   ├── modelo_riesgo_inundacion.pkl
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│   └── features_modelo.pkl
│
├── Notebook/
│   ├── requirements.txt
│   └── Proyecto_Grupo_A.ipynb
│
├── Código Flask/
│   └── app.py
│
├── Informe en Latex/
│   ├── Proyecto_Final_Materia_-pdf
│   └── Proyecto_LaTex_fuente_v2_.zip
│
├── Capturas del hosting
│   └── Capturas del hosting
│
└── Videos
    └── Vídeo demostrativo de la web

```

---

# Contenido del Notebook

El notebook realiza las siguientes etapas:

1. Carga de librerías.
2. Importación de los conjuntos de datos.
3. Limpieza y preparación de datos.
4. Integración de información geográfica y climática.
5. Construcción de la variable objetivo (Riesgo de Inundación).
6. Selección de variables.
7. Entrenamiento de varios modelos de clasificación.
8. Optimización del modelo mediante GridSearchCV.
9. Evaluación del desempeño.
10. Exportación del modelo entrenado y archivos necesarios para producción.

---

# Modelos Evaluados

Durante el desarrollo del proyecto se probaron diferentes algoritmos de clasificación:

- Regresión Logística
- Árbol de Decisión
- Support Vector Machine (SVM)
- Random Forest
- Modelo de Ensamble

Después de comparar sus métricas, el modelo seleccionado fue **Random Forest**, debido a su mejor desempeño en la clasificación del riesgo de inundación.

---

# Archivos Generados

Al finalizar la ejecución del notebook se crean automáticamente los siguientes archivos:

- `modelo_riesgo_inundacion.pkl`
- `scaler.pkl`
- `label_encoder.pkl`
- `features_modelo.pkl`
- `predicciones.csv`

Estos archivos permiten reutilizar el modelo sin necesidad de volver a entrenarlo.

---

# Requisitos

Se recomienda utilizar **Python 3.10 o superior**.

Instalar las dependencias mediante:

```bash
pip install -r requirements.txt
```

Si no existe el archivo `requirements.txt`, instalar manualmente:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install scikit-learn
pip install geopandas
pip install shapely
pip install rasterio
pip install pyogrio
pip install scipy
pip install joblib
pip install openpyxl
```

---

# Ejecución

1. Descargar el proyecto.

2. Abrir el notebook: ```Proyecto_Grupo_A.ipynb```

3. Ejecutar todas las celdas en orden.

4. Esperar hasta que finalice el entrenamiento.

5. Verificar que se hayan generado:

- modelo_riesgo_inundacion.pkl
- scaler.pkl
- label_encoder.pkl
- features_modelo.pkl
- predicciones_finales.csv

---

# Despliegue

Una vez entrenado el modelo, pueden utilizarse los archivos exportados para integrarlo en una aplicación web, API o sistema de predicción.

Los archivos necesarios son:

- modelo_riesgo_inundacion.pkl
- scaler.pkl
- label_encoder.pkl
- features_modelo.pkl

Estos contienen el modelo entrenado, el escalador, el codificador de etiquetas y la lista de variables utilizadas durante el entrenamiento.

---

# Resultados

El modelo final permite:

- Clasificar automáticamente el nivel de riesgo de inundación.
- Generar predicciones para nuevas parroquias.
- Exportar los resultados en formato CSV.
- Facilitar el análisis para la gestión del riesgo.

---

# Integrantes

*   Correa Preciado Jonathan Alexi
*   Franco Vera Junior Alexander
*   Rivas Toala Rodrigo Alexander
*   Mora Baque Carlos Andrés
*   Domenech Verdesoto Juan Pablo
