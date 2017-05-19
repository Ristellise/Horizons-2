def generateuniverse(name,*args):
    """
    :param name: Name of Universe
    :param args: type: Type of generation
                 NoStars : Number Of Stars
                 clusters : Number of Clusters
                 starpercluster : Stars Per clusters
                 distrostars : Distribution of Star Number in each Cluster
    :return: 
    """
    for(type, NoStars, clusters, starpercluster, distrostars) in args:
        TYPE = type
        if clusters is None or 0:
            NUMC = 1
        else:
            NUMC = clusters
        NUMSTR = NoStars
        NUMCLUS = clusters
