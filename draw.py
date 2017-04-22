import pyglet
import Main
window = Main.window
starbatch = pyglet.graphics.Batch()
stardraw = []
"""
Do not hack into This function below! this is used for low level drawing!
"""
def add2Batch():
    print()
@window.event
def on_draw():
    window.clear()
    stardraw.draw()

def update(dt):
