"""
visual
-------------

Handle visual properties for meshes, including color and texture
"""

from .color import (ColorVisuals,
                    random_color,
                    to_rgba,
                    create_visual,
                    interpolate,
                    DEFAULT_COLOR,
                    linear_color_map)

# explicitly list imports in __all__
# as otherwise flake8 gets mad
__all__ = [ColorVisuals,
           random_color,
           to_rgba,
           create_visual,
           DEFAULT_COLOR,
           interpolate,
           linear_color_map]