__version__ = "1.0.0"
__author__ = "isaul_t22 <https://github.com/isaultirado77>"
__doc__ = """
Módulo central para procesamiento de imágenes

Contiene:
- Carga de imágenes (image_loader)
- Transformaciones geométricas y de color (image_transform)
- Mejora de imágenes (image_enhancement)
- Aplicación de filtros y detección de bordes (image_filter)
- Análisis de imágenes (image_analysis)
"""

# Importaciones principales
from .image_loader import (
    load_image
)

from .image_transform import (
    translate, 
    rotate, 
    resize, 
    crop, 
    convert_color, 
    add, 
    subtract, 
    multiply,
    apply_mask
)

from .image_enhancement import (
    adjust_brightness, 
    adjust_contrast, 
    adjust_brightness_contrast, 
    histogram_equalization, 
    clahe, 
    gamma_correction, 
    auto_contrast
)

from .image_filter import (
    avgerage_blur, 
    median_blur,
    gaussian_blur, 
    bilateral_filter, 
    sobel_edges, 
    canny_edges, 
    laplacian_edges, 
    sharpen, 
    apply_kernel, 
    emboss_filter
)

from .image_analysis import (
    find_contours, 
    approximate_contour, 
    detect_shapes, 
    simple_threshold, 
    adaptive_threshold, 
    otsu_threshold,
    compute_moments, 
    compute_shape_descriptors, 
    detect_edges, 
    detect_corners, 
    draw_contours, 
    draw_corners
)

# Lista de todas las funciones exportadas
__all__ = [
    # image_loader.py
    'load_image',

    # image_transform.py
    'translate',
    'rotate',
    'resize',
    'crop',
    'convert_color',
    'add',
    'subtract',
    'multiply',
    'apply_mask',

    # image_enhancement.py
    'adjust_brightness',
    'adjust_contrast',
    'adjust_brightness_contrast',
    'histogram_equalization',
    'clahe',
    'gamma_correction',
    'auto_contrast',

    # image_filter.py
    'avgerage_blur',
    'median_blur',
    'gaussian_blur',
    'bilateral_filter',
    'sobel_edges',
    'canny_edges',
    'laplacian_edges',
    'sharpen',
    'apply_kernel',
    'emboss_filter',

    # image_analysis.py
    'find_contours',
    'approximate_contour',
    'detect_shapes',
    'simple_threshold',
    'adaptive_threshold',
    'otsu_threshold',
    'compute_moments',
    'compute_shape_descriptors',
    'detect_edges',
    'detect_corners',
    'draw_contours',
    'draw_corners'
]
