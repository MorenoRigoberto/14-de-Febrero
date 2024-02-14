# Importar librerias necesarias
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from google.colab import files
import os
import shutil

# Función para crear la forma de corazón con parámetros ajustados
def create_heart(center_x, center_y, scale_factor):
    t = np.linspace(0, 2*np.pi, 100)
    x = scale_factor * 8 * np.sin(t)**3 + center_x
    y = scale_factor * (6.5 * np.cos(t) - 2.5 * np.cos(2*t) - np.cos(3*t) - 0.5 * np.cos(4*t)) + center_y
    return Polygon(np.column_stack((x, y)))

# Coordenadas de Guadalajara (aproximadamente)
guadalajara_center_x = -103.3584
guadalajara_center_y = 20.6597

# Crear la forma de corazón centrada alrededor de Guadalajara
heart = create_heart(guadalajara_center_x, guadalajara_center_y, scale_factor=0.05)

# Crear GeoDataFrame
gdf = gpd.GeoDataFrame([1], geometry=[heart])

# Cambiar los nombres de las columnas a cadenas de texto
gdf.columns = gdf.columns.astype(str)

# Carpeta de salida y ruta del archivo shapefile
output_folder = "corazon_shapefiles"
output_shapefile = f"{output_folder}/corazon.shp"

# Crear la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Guardar el GeoDataFrame como un archivo shapefile
gdf.to_file(output_shapefile)

# Mostrar el resultado
gdf.plot()
plt.show()

# Comprimir la carpeta con el shapefile en un archivo zip
shutil.make_archive(output_folder, 'zip', output_folder)

# Descargar el archivo zip que contiene el shapefile y archivos auxiliares
files.download(f"{output_folder}.zip")