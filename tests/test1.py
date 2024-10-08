from GameEngine import Window, app
from GameEngine.keys.fr import KEY_Z, KEY_Q, KEY_S, KEY_D
from GameEngine.math import Vector2
from GameEngine.shape import Rectangle, Circle, Batch
from GameEngine.utils import ColorDataBase

app.params(fps=330)

window = Window()
window.x = 200
window.y = 200

velocity = Vector2(0, 0)
speed = 20

keys_pressed = set()

batch = Batch()
rectangle = Rectangle(100, 100, 200, 200, color=(0, 0, 255), batch=batch)
circle = Circle(200, 300, 50, color=(0, 0, 255), batch=batch)

@window.event
def on_draw():
   window.clear(ColorDataBase.red)
   circle.draw()

@window.event
def on_key_press(symbol, modifiers):
    keys_pressed.add(symbol)

@window.event
def on_key_release(symbol, modifiers):
    keys_pressed.remove(symbol)

@app.event
def on_update(dt):
    global velocity

    if KEY_Z in keys_pressed:
        velocity.y -= speed
    if KEY_Q in keys_pressed:
        velocity.x -= speed
    if KEY_S in keys_pressed:
        velocity.y += speed
    if KEY_D in keys_pressed:
        velocity.x += speed

    window.x += velocity.x * dt
    window.y += velocity.y * dt

    velocity *= 0.95

@app.event
def on_fix_update(fdt):
    pass

app.run()
