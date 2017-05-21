import random
from src.UniverseGen import Elliptical


def generateuniverse(name, *args):
    """
    :param name: Name of Universe
    :param args: type: Type of generation
                 NoStars : Number Of Stars
                 clusters : Number of Clusters
                 starpercluster : Stars Per clusters
                 distrostars : Distribution of Star Number in each Cluster
                 Galaxylength : How wide the galaxy is
                 PNGSIZE = Well duh?
                 seed = seed in args or random seed...
    :return: 
    """
    for (type, NoStars, clusters, starpercluster, distrostars, Galaxylength, PNGSIZE, seed) in args:
        TYPE = type
        if clusters is None or 0:
            Elliptical.NUMC = 1
        else:
            Elliptical.NUMC = clusters
        Elliptical.NUMSTR = NoStars
        Elliptical.NUMCLUS = clusters
        Elliptical.GALX = Galaxylength
        Elliptical.GALY = Galaxylength
        Elliptical.CLUSRADA = Elliptical.GALX // 12
        Elliptical.DISCLRADA = Elliptical.CLUSRADA // 5
        RAND = random.seed(seed)
    if type == "0":
        Elliptical.generateclusters()
        Elliptical.generateStars()
        Elliptical.drawtopng("ellipticalgalaxy" + str(RAND) + "-" + str(name) + ".png")
