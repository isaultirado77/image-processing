import urllib.request
import numpy as np
import cv2
from pathlib import Path

def load_image(source, base_dir=None):
    """Carga una imagen desde archivo o URL."""
    if is_url(source):
        return load_from_url(source)
    else:
        return load_from_file(source, base_dir)

def is_url(source):
    return source.startswith(("http://", "https://"))

def load_from_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
            return cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    except Exception as e:
        raise ValueError(f"Error loading image from URL: {e}") from None

def load_from_file(filename, base_dir=None):
    base_dir = base_dir or Path.cwd()
    file_path = Path(base_dir) / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"No image found at: {file_path}")
    
    image = cv2.imread(str(file_path))
    if image is None:
        raise ValueError(f"Invalid image file: {file_path}")
    
    return image