# GameEngine README

## Overview

The `GameEngine` library provides a simple framework for creating interactive applications and games. This library features a window management system, event handling, and essential components like `Transform` and `RigidBody` for 2D game development. The following documentation explains how to set up a basic game window, handle input events, and use core components.

## Installation

To use the `GameEngine` library, ensure you have Python installed on your system. You can then install the library via pip (if it’s available in PyPI) or by cloning the repository directly:

```bash
pip install GameEngine
```

Alternatively, clone the repository:

```bash
git clone <repository-url>
```

## Usage

Here's a basic example demonstrating how to create a window, handle events, and use core components from the `GameEngine` library.

### Basic Setup

```python
from GameEngine import Window, app
from GameEngine.components import Transform, RigidBody
from GameEngine.math import Vector2 as Vec2
from GameEngine.utils import Color, ColorDataBase
```

### Create Components

To create a transform and a rigid body component, you can initialize them as follows:

```python
# Create a Transform component
transform_component = Transform(position=Vec2(), rotation=Vec2(), scale=Vec2())

# Create a RigidBody component
rigid_body_component = RigidBody(velocity=Vec2(), acceleration=Vec2(), mass=1.0)

# Define a color
red = Color.from_hex("#ff0000")
```

### Window and Event Handling

Set up the game window and define event handlers:

```python
# Create a window
window = Window()

@window.event
def on_draw():
    window.clear(ColorDataBase.black)

@window.event
def on_close():
    print("Fermeture de la fenêtre...")
    window.close()

@window.event
def on_key_press(symbol, modifiers):
    print(f"Touche enfoncée: {symbol}, Modificateurs: {modifiers}")

@window.event
def on_key_release(symbol, modifiers):
    print(f"Touche relâchée: {symbol}, Modificateurs: {modifiers}")

@window.event
def on_mouse_press(x, y, button, modifiers):
    print(f"Clic de souris à ({x}, {y}) avec le bouton {button}")

@window.event
def on_mouse_release(x, y, button, modifiers):
    print(f"Relâchement de la souris à ({x}, {y}) avec le bouton {button}")

@window.event
def on_mouse_motion(x, y):
    print(f"Mouvement de la souris à ({x}, {y})")

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    print(f"Défilement de la souris à ({x}, {y}) avec défilement ({scroll_x}, {scroll_y})")

@window.event
def on_gain_focus():
    print("Fenêtre gain focus")

@window.event
def on_lose_focus():
    print("Fenêtre lose focus")

@window.event
def on_show():
    print("Fenêtre show")

@window.event
def on_hide():
    print("Fenêtre hide")
```

### Application Loop

You can also define update functions to handle game logic:

```python
@app.event
def on_update(dt):
    pass  # Game logic updates

@app.event
def on_fix_update(fdt):
    pass  # Physics updates
```

### Running the Application

Finally, start the application loop with:

```python
app.run()
```

## Event Summary

- **on_draw**: Called to render the window.
- **on_close**: Handles window close events.
- **on_key_press**: Handles key press events.
- **on_key_release**: Handles key release events.
- **on_mouse_press**: Handles mouse button press events.
- **on_mouse_release**: Handles mouse button release events.
- **on_mouse_motion**: Handles mouse movement events.
- **on_mouse_scroll**: Handles mouse scrolling events.
- **on_gain_focus**: Called when the window gains focus.
- **on_lose_focus**: Called when the window loses focus.
- **on_show**: Called when the window is shown.
- **on_hide**: Called when the window is hidden.

## Components

### Transform

- `position`: A `Vector2` indicating the object's position.
- `rotation`: A `Vector2` representing the object's rotation.
- `scale`: A `Vector2` indicating the object's scale.

### RigidBody

- `velocity`: A `Vector2` indicating the object's velocity.
- `acceleration`: A `Vector2` indicating the object's acceleration.
- `mass`: A float representing the mass of the object.

## Colors

### Color

Use the `Color` class to define colors in your application. Colors can be created from hex values:

```python
red = Color.from_hex("#ff0000")
```

### ColorDataBase

The `ColorDataBase` provides a set of predefined colors, including:

- `ColorDataBase.black`
- `ColorDataBase.white`
- `ColorDataBase.red`
- etc.

## Conclusion

The `GameEngine` library offers a straightforward way to create games and interactive applications. This README provides a basic overview of how to set up your environment, create components, handle events, and run a game loop. Explore further to create engaging game mechanics and visuals!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
