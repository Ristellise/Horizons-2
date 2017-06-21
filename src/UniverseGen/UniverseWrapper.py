from src.UniverseGen import Elliptical, Globals, Spiral,Ring


def generateuniverse(name, galtype, hsb):
    """
    :param name: Name of Universe
    :param galtype: type of galaxy
    :param hsb: Size of galaxy (0-4)
    :return: 
    """
    Globals.hsb = hsb
    Globals.Name = name
    Globals.Galz = 0  # This makes the galaxy flat :P
    if galtype == 0:
        Elliptical.generateclusters()
        Elliptical.generatestars()
        Elliptical.drawtopng("ellipticalgalaxy" + str(Globals.RAND) + "-" + str(name) + ".png")
    elif galtype == 1:
        Spiral.generateclusters()
        Spiral.generatestars()
        Spiral.drawtopng("Spiralgalaxy" + str(Globals.RAND) + "-" + str(name) + ".png")
        Spiral.textgen()
    elif galtype == 2:
        Ring.generateclusters()
        Ring.generatestars()
        Ring.drawtopng("Spiralgalaxy" + str(Globals.RAND) + "-" + str(name) + ".png")
        Ring.textgen()
generateuniverse("test1", galtype=0, hsb=4)
generateuniverse("test2", galtype=1, hsb=4)
