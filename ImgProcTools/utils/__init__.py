__version__ = "1.0.0"
__author__ = "isaul_t22 <https://github.com/isaultirado77>"
__doc__ = """
Módulo de utilidades para procesamiento de imágenes

Contiene:
- Herramientas de visualización (draw_utils, plot_utils)
- Análisis de histogramas (histogram_utils)
- Funciones auxiliares generales (utils)
"""

# Importaciones principales
from .utils import (
    print_image_info,
    scale_image
)

from .histogram_utils import (
    compute_histogram, 
    compute_cumulative_histogram, 
    plot_histogram, 
    plot_histogram_3d, 
    normalize_histogram, 
    compare_histograms,
    histogram_matching,
    get_histogram_stats, 
    plot_histogram_comparison,
    plot_histogram_with_stats
)

from .draw_utils import (
    create_canvas, 
    draw_line, 
    draw_rectangle, 
    draw_polygon, 
    draw_circle, 
    draw_ellipse, 
    draw_text, 
    draw_arrow, 
    add_grid, 
    blend_with_canvas, 
    random_shapes,
    draw_bounding_box,
    draw_orientation_line
)

from .plot_utils import (
    side_by_side
)

# Lista de todas las funciones exportadas
__all__ = [
    # utils.py
    'print_image_info',
    'scale_image',
    
    # histogram_utils.py
    'compute_histogram',
    'compute_cumulative_histogram',
    'plot_histogram',
    'plot_histogram_3d',
    'normalize_histogram',
    'compare_histograms',
    'histogram_matching',
    'get_histogram_stats',
    'plot_histogram_comparison',
    'plot_histogram_with_stats',
    
    # draw_utils.py
    'create_canvas',
    'draw_line',
    'draw_rectangle',
    'draw_polygon',
    'draw_circle', 
    'draw_ellipse',
    'draw_text',
    'draw_arrow',
    'add_grid',
    'blend_with_canvas',
    'random_shapes',
    'draw_bounding_box',
    'draw_orientation_line',
    
    # plot_utils.py
    'side_by_side'
]
