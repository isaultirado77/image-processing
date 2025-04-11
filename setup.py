from setuptools import setup, find_packages

setup(
    name="image_processing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5",
        "numpy>=1.21",
        "matplotlib>=3.4",
    ],
)