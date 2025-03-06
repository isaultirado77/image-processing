import pytest
from core.image_loader import ImageLoader

class TestLoader: 
    def test_load_from_path(self):
        loader = ImageLoader("../../images/mandrill")
        image = loader.load()
        assert image is not None and isinstance(image, np.ndarray)
    
    def test_load_from_url(self):
        loader = ImageLoader("https://pesdb.net/pes2020/images/players/7511.png")
        image = loader.load()
        assert image is not None and isinstance(image, np.ndarray)
    
    def test_invalid_path(self):
        loader = ImageLoader("invalid/path/to/image.jpg")
        with pytest.raises(ValueError):
            loader.load()
    
    def test_invalid_url(self):
        loader = ImageLoader("https://invalid-url.com/image.jpg")
        with pytest.raises(ValueError):
            loader.load()
