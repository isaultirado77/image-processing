from setuptools import setup, find_packages

setup(
    name="ImgProcTools",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5",
        "numpy>=1.21",
        "matplotlib>=3.4",
    ],
)