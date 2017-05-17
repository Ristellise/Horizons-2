def drawToPNG(filename):
    image = Image.new("RGB", (int(PNGSIZE), int(PNGSIZE)), PNGBGCOLOR)
    draw = ImageDraw.Draw(image)

    # Find maximal star distance
    max = 0
    for (x, y, z, scol) in stars:
        if abs(x) > max:
            max = x
        if abs(y) > max:
            max = y
        if abs(z) > max:
            max = z

    # Calculate zoom factor to fit the galaxy to the PNG size
    factor = float(PNGSIZE - PNGFRAME * 2) / (max * 2)
    for (x, y, z, scol) in stars:
        sx = factor * x + PNGSIZE / 2
        sy = factor * y + PNGSIZE / 2
        draw.point((sx, sy), fill=scol)

    # Save the PNG
    image.save(filename)
    print(filename)

NUMCLUS = NUMSTR / 70

DISCLUS = NUMCLUS / 4

GALX = int(NUMSTR / (random.randrange(8, 20)))

GALY = int(NUMSTR / (random.randrange(6, 28)))

GALZ = int(NUMSTR / (random.randrange(10, 40)))

CLUSRAD = NUMCLUS / 5

DISCLRAD = CLUSRAD / 5

PNGSIZEA = GALX / 5

PNGFRAMEA = PNGSIZEA / 10

PNGSIZE = float(raw_input('X and Y Size of PNG <Default:Bad Idea>:') or str(PNGSIZEA))

PNGFRAME = float(raw_input('PNG Frame Size <Default:Bad Idea>:') or str(PNGFRAMEA))