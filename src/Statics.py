from src import classes, Gconstants


def mainscreen():
    classes.text('hello World!', 100, 100, (0, 0, 0), False).draw(Gconstants.screen)
    classes.text('hello World!2', 100, 100, (0, 0, 0), False).draw(Gconstants.screen)
    classes.image(600,500,"testimg.png")