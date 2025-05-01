# **ImgProcTools** - Biblioteca de Procesamiento de Imágenes en Python

**ImgProcTools** es una biblioteca Python diseñada para proporcionar herramientas esenciales de procesamiento de imágenes, construida sobre OpenCV y NumPy. 

**Nota**: Este proyecto documenta mi proceso de aprendizaje en el campo del procesamiento de imágenes utilizando OpenCV, así como mi evolución en el desarrollo de software con Python. Ha sido concebido principalmente como una herramienta educativa y de autoevaluación, en la que he aplicado conceptos fundamentales de procesamiento de imagenes y buenas prácticas. Si bien puede resultar útil para otros, su propósito principal ha sido didáctico y personal.

## Características Principales

### **Módulos Principales**
| Módulo | Funcionalidades |
|--------|----------------|
| `core/` | Operaciones fundamentales de procesamiento |
| `utils/` | Herramientas auxiliares y visualización |

### **Funcionalidades Clave**
- Carga de imágenes desde archivo o URL
- Transformaciones geométricas (rotación, escalado, perspectiva)
- Filtrado avanzado (Gaussiano, bilateral, detección de bordes)
- Análisis de imágenes (detección de formas, histogramas)
- Herramientas de dibujo y visualización

## Instalación

1. **Requisitos previos**:
   ```bash
   pip install opencv-python numpy matplotlib
   ```
   
2. **Instalar ImgProcTools**:
   ```bash
   pip install git+https://github.com/isaultirado77/image-processing-tools.git
   ```
   O para instalación editable (desarrollo):
   ```bash
   git clone https://github.com/isaultirado77/image-processing-tools.git
   cd ImgProcTools
   pip install -e .
   ```

## Uso Básico

### Ejemplo 1: Procesamiento Básico
```python
from ImgProcTools.core import image_loader, image_transform
from ImgProcTools.utils import histogram_utils

# Cargar y transformar imagen
img = image_loader.load_image("ruta/imagen.jpg")
rotated = image_transform.rotate(img, angle=45)
resized = image_transform.resize(img, width=300)

# Analizar histograma
hist = histogram_utils.compute_histogram(img)
```

### Ejemplo 2: Filtrado Avanzado
```python
from ImgProcTools.core import image_filter

edges = image_filter.canny_edges(img, low_threshold=50)
denoised = image_filter.bilateral_filter(img, d=9, sigma_color=75)
```

## Documentación

Explora los notebooks de ejemplo en [`/examples`](examples/):
- [`basic_usage.ipynb`](examples/basic_usage.ipynb): Introducción a las funciones básicas
- [`advanced_techniques.ipynb`](examples/advanced_techniques.ipynb): Casos de uso avanzados

## Estructura del Proyecto
```
ImgProcTools/
├── core/               # Módulos principales
│   ├── image_loader.py
│   ├── image_transform.py
|   ├── image_analysis.py
|   ├── image_enhancement.py
|   ├── image_filter.py
│   └── frecuency_filters.py
├── utils/              # Herramientas auxiliares
│   ├── utils.py
│   ├── draw_utils.py
│   ├── histogram_utils.py
│   └── plot_utils.py
├── examples/           # Ejemplos prácticos
├── tests/              # Pruebas unitarias
└── docs/               # Documentación técnica
```
