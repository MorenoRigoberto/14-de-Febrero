// Cargar el polígono desde un archivo shapefile
var poly = ee.FeatureCollection("RUTA DE TU GEOMETRIA");

// Cargar la colección de imágenes Landsat 8 y filtrar por fecha y ubicación
var collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')
  .filterBounds(poly)
  .sort('system:time_start', false)  // Ordenar por fecha descendente
  .limit(1);  // Obtener la imagen más reciente

// Seleccionar la imagen más reciente
var image = ee.Image(collection.first());

// Unir geometrías para eliminar agujeros en el polígono
var polyUnion = poly.union();

// Crear un buffer alrededor del polígono
var bufferedPoly = polyUnion.geometry().buffer(100); // Ajusta el valor del buffer según sea necesario

// Rellenar el polígono con la imagen
var filledPoly = image.clip(bufferedPoly);

// Visualizar la imagen y el polígono
Map.centerObject(polyUnion, 10);  // Centrar el mapa en el polígono
Map.addLayer(filledPoly, {bands: ['B5', 'B4', 'B3'], min: 0, max: 0.3}, 'Imagen Landsat 8');
Map.addLayer(polyUnion, {color: 'FF0000'}, 'Polígono Union');
Map.addLayer(bufferedPoly, {color: '0000FF'}, 'Polígono con Buffer');

// Agregar etiqueta al mapa
Map.add(ui.Label('TU NOMBRE', {position: 'top-center'}));
