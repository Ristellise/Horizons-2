import sys
def __init__():
    """
    When imported, it will test for all the requred dependancies.
    :return: missing Dependants in a list.
    """
    missingdeps = []
    try:
        import numpy
    except ImportError:
        missingdeps.append("numpy")
    try:
        import cocos
    except ImportError:
        missingdeps.append("cocos2D")
    if sys.platform == ["linux", "linux2"]:
        try:
            import sdl
        except ImportError:
            try:
                import libsdl
            except ImportError:
                missingdeps.append("SDL")
    elif sys.platform == ["win32","win16"]:
        try:
            import pygame
        except ImportError:
            missingdeps.append("Pygame")
    else:
        # probably Mac but eh...
        try:
            import sdl
        except ImportError:
            try:
                import libsdl
            except ImportError:
                missingdeps.append("SDL")
