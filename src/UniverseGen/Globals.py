import random


def setup():
    if hsb == 0:
        NUMSTR = random.randrange(1, 100)
    elif hsb == 1:
        NUMSTR = random.randrange(100, 1000)
    elif hsb == 2:
        NUMSTR = random.randrange(1000, 100000)
    elif hsb == 3:
        NUMSTR = random.randrange(100000, 1000000)
    elif hsb == 4:
        NUMSTR = random.randrange(1000000, 2000000)


Name = "The Nameless Galaxy"
hsb = 0
Galz = 0
RAND = random.randint(0, 1000000000)
pngsize = 2048
NUMSTR = 0
