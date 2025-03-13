import urllib.request
import numpy as np
import cv2
from pathlib import Path

class Loader:
    IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"

    def __init__(self, source: str):
        self._source = source
        self._image = None

    def load(self):
        if self._is_url():
            print(f"\n--- Loading from URL: {self._source} ---\n")
            self._image = self._load_from_url()
        else:
            print(f"\n--- Loading from File: {self._source} ---\n")
            self._image = self._load_from_file()

        if self._image is None:
            raise ValueError("The image could not be loaded. Check the path or URL.")

    def _is_url(self):
        return self._source.startswith("http://") or self._source.startswith("https://")

    def _load_from_url(self):
        try:
            response = urllib.request.urlopen(self._source)
            image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
            return cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        except Exception as e:
            print(f"Error while loading image from URL: {e}")
            return None

    def _load_from_file(self):
        file_path = self.IMAGES_DIR / self._source
        if not file_path.is_file():
            print(f"Error: The source file doesn't exist. Path: {file_path}")
            return None
        return cv2.imread(str(file_path))

    def get_image(self):
        return self._image

