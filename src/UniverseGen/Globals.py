NAME = None

NUMC = 0

NUMSTR = int(input('Number of Stars <Default:2000>:') or "2000")

NUMCLUSA = NUMSTR // 70

NUMCLUS = int(input('Number of Stars in each Cluster <Default:Hub / 70>:') or str(NUMCLUSA))

DISCLUSA = NUMCLUS // 4

DISCLUS = int(input('Distribution of Star Number in each Cluster <Default: Avg/ 4>:') or str(DISCLUSA))

GALX = float(input('X Length of Galaxy <Default:90.0>:') or "90.0")

GALY = float(input('Y Length of Galaxy <Default:90.0>:') or "90.0")

GALZ = float(input('Maximum Depth of Galaxy <Default:0.0>:') or "0.0")

CLUSRADA = GALX // 12

CLUSRAD = float(input('Radius of each cluster <Default:Hub / 12>:') or str(CLUSRADA))

DISCLRADA = CLUSRAD // 5

DISCLRAD = float(input('Distribution of Cluster Radius <Default:Avg / 5>:') or str(DISCLRADA))

PNGSIZE = float(input('X and Y Size of PNG <Default:1200>:') or "1200")

PNGFRAME = float(input('PNG Frame Size <Default:50>:') or "50")