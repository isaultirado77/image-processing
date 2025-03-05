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
    pass