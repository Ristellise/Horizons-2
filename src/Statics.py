from src import classes, Gconstants


def mainscreen():
    classes.Text('hello World!', 100, 100, (0, 0, 0), False).draw(Gconstants.screen)
    classes.Text('hello World!2', 100, 100, (0, 0, 0), False).draw(Gconstants.screen)
    classes.Image(600, 500, "testimg.png")
