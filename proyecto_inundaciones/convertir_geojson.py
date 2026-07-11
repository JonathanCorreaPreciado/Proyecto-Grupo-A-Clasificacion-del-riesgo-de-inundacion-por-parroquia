import geopandas as gpd

# Leer el shapefile
gdf = gpd.read_file("data/shp/nxparroquias.shp")

# Filtrar únicamente la provincia del Guayas
guayas = gdf[gdf["DPA_DESPRO"] == "GUAYAS"]

# Mostrar cuántas parroquias quedaron
print("Número de parroquias:", len(guayas))

# Guardar el GeoJSON
guayas.to_file(
    "data/parroquias_guayas.geojson",
    driver="GeoJSON"
)

print("GeoJSON creado correctamente.")

print("\nParroquias del GeoJSON:")
print(guayas["DPA_DESPAR"].head(10))