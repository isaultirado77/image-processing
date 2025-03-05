import argparse
import cv2
import numpy as np
import urllib.request
from pathlib import Path

class ImageLoader: 
    """
    Clase para cargar imagenes desde archivos locales o URLs.
    """
    def __init__(self, source: str):
        """..."""
        self._soruce = source
        self._image = None
    
    def load(self):
        """
        Carga la imagen desde la fuente específicada. 
        : return: Imagen cargada en formato OpenCV (numpy array)
        """ 
        if self._is_url(): 
            self._image = self._load_from_url()
        else: 
            self._image = self._load_from_file()
        
        if self._image is None: 
            raise ValueError("The image could not be loaded. Check the path or URL. ")

    def _is_url(self):
        """Verifica si la fuente es una URL.""" 
        return self._soruce.startswith("http://") or self._soruce.startswith("https://")

    def _load_from_url(self):
        """Carga una imagen desde una URL."""
        try: 
            response = urllib.request.urlopen(self._soruce)
            image_array = np.asarray(bytearray(response.read(), dtype=np.uint8))
            return cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        except Exception as e: 
            print(f"Error while loading image from URL: {e}")
            return 
        
    def _load_from_file(self):
        """Carga una imagen desde un archivo local.""" 
        if not Path(self._soruce).is_file(): 
            print("Error: The source file doesn't exists.")
            return
        return cv2.imread(self._soruce)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Carga una imagen desde un archivo o URL.")
    parser.add_argument("-i", "--image", required=True, help="Ruta del archivo o URL de la imagen.")
    args = vars(parser.parse_args())

    loader = ImageLoader(args["image"])
    image = loader.load()

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()