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
        """...""" 
        pass

    def _is_url(self):
        """...""" 
        pass

    def _load_from_url(self):
        """...""" 
        pass

    def _load_from_file(self):
        """...""" 
        pass

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Carga una imagen desde un archivo o URL.")
    parser.add_argument("-i", "--image", required=True, help="Ruta del archivo o URL de la imagen.")
    args = vars(parser.parse_args())

    loader = ImageLoader(args["image"])
    image = loader.load()

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()