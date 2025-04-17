import os
from PIL import Image

# Lista de extensiones comunes de imágenes
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')

# Recorre todos los archivos en la carpeta actual
for filename in os.listdir('.'):
    ext = os.path.splitext(filename)[1].lower()

    # Saltar si ya es .tiff o .tif
    if ext in ('.tiff', '.tif'):
        continue

    # Procesar solo si es una imagen común
    if ext in image_extensions:
        try:
            img = Image.open(filename)
            output_name = os.path.splitext(filename)[0] + '.tiff'

            # Guardar como TIFF (incluye múltiples frames si aplica)
            img.save(output_name, format='TIFF', save_all=True)

            # Eliminar el archivo original después de conversión exitosa
            os.remove(filename)

            print(f"Convertido y eliminado: {filename} -> {output_name}")
        except Exception as e:
            print(f"Error al convertir {filename}: {e}")

