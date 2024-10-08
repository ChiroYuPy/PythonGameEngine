import inspect
import glfw
from OpenGL.raw.GL.VERSION.GL_1_0 import glClearColor, glClear, GL_COLOR_BUFFER_BIT, glViewport, glMatrixMode, \
    GL_PROJECTION, glLoadIdentity, glOrtho, GL_MODELVIEW

from GameEngine.shape import Circle
from GameEngine.utils.color_data_base import ColorDataBase


class Window:
    window_instances = []

    def __init__(self, width=800, height=600, title="Window"):
        self._x = 0
        self._y = 0
        self._width = width
        self._height = height
        self._title = title

        self.event_handlers = {}
        self.register_window(self)

        if not glfw.init():
            raise ValueError("Failed to initialize glfw")

        self.glfw_window = glfw.create_window(width, height, title, None, None)

        if not self.glfw_window:
            raise ValueError("Failed to initialize glfw window")

        glfw.make_context_current(self.glfw_window)

        glOrtho(0, self.width, self.height, 0, -1, 1)

        # Set GLFW callbacks
        glfw.set_key_callback(self.glfw_window, self.key_callback)
        glfw.set_mouse_button_callback(self.glfw_window, self.mouse_button_callback)
        glfw.set_cursor_pos_callback(self.glfw_window, self.cursor_position_callback)
        glfw.set_window_size_callback(self.glfw_window, self.resize_callback)
        glfw.set_window_close_callback(self.glfw_window, self.close_callback)
        glfw.set_window_focus_callback(self.glfw_window, self.focus_callback)
        glfw.set_window_iconify_callback(self.glfw_window, self.iconify_callback)
        glfw.set_window_maximize_callback(self.glfw_window, self.maximize_callback)
        glfw.set_scroll_callback(self.glfw_window, self.scroll_callback)

        # Add mouse enter/leave state
        self.mouse_inside = False

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def title(self):
        return self._title

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @width.setter
    def width(self, width):
        self._width = width
        glfw.set_window_size(self.glfw_window, int(width), int(self.height))

    @height.setter
    def height(self, height):
        self._height = height
        glfw.set_window_size(self.glfw_window, int(self.width), int(height))

    @title.setter
    def title(self, title):
        self._title = title
        glfw.set_window_title(self.glfw_window, title)

    @x.setter
    def x(self, x):
        self._x = x
        glfw.set_window_pos(self.glfw_window, int(x), int(self.y))

    @y.setter
    def y(self, y):
        self._y = y
        glfw.set_window_pos(self.glfw_window, int(self.x), int(y))

    def clear(self, color=ColorDataBase.black):
        glClearColor(color.r, color.g, color.b, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def close(self):
        glfw.destroy_window(self.glfw_window)
        glfw.terminate()

    def event(self, func):
        event_name = func.__name__

        if not hasattr(self, event_name):
            raise ValueError(f"event {event_name} does not exist")

        if event_name in self.event_handlers:
            raise ValueError(f"event {event_name} already registered")

        expected_args = len(inspect.signature(getattr(self, event_name)).parameters)
        actual_args = len(inspect.signature(func).parameters)

        if actual_args != expected_args:
            raise ValueError(f"{event_name} expects {expected_args} arguments but got {actual_args}")

        print(f"event {event_name} registered")
        self.event_handlers[event_name] = func
        return func

    def update(self):
        glfw.make_context_current(self.glfw_window)
        self.on_draw()
        glfw.swap_buffers(self.glfw_window)
        glfw.poll_events()

    def on_draw(self):
        if 'on_draw' in self.event_handlers:
            self.event_handlers['on_draw']()

    def on_resize(self, width, height):
        if 'on_resize' in self.event_handlers:
            self.event_handlers['on_resize'](width, height)

    def on_close(self):
        if 'on_close' in self.event_handlers:
            self.event_handlers['on_close']()
        else:
            self.close()

    def on_key_press(self, symbol, modifiers):
        if 'on_key_press' in self.event_handlers:
            self.event_handlers['on_key_press'](symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if 'on_key_release' in self.event_handlers:
            self.event_handlers['on_key_release'](symbol, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        if 'on_mouse_press' in self.event_handlers:
            self.event_handlers['on_mouse_press'](x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if 'on_mouse_release' in self.event_handlers:
            self.event_handlers['on_mouse_release'](x, y, button, modifiers)

    def on_mouse_motion(self, x, y):
        if 'on_mouse_motion' in self.event_handlers:
            self.event_handlers['on_mouse_motion'](x, y)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if 'on_mouse_scroll' in self.event_handlers:
            self.event_handlers['on_mouse_scroll'](x, y, scroll_x, scroll_y)

    def on_gain_focus(self):
        if 'on_gain_focus' in self.event_handlers:
            self.event_handlers['on_gain_focus']()

    def on_lose_focus(self):
        if 'on_lose_focus' in self.event_handlers:
            self.event_handlers['on_lose_focus']()

    def on_show(self):
        if 'on_show' in self.event_handlers:
            self.event_handlers['on_show']()

    def on_hide(self):
        if 'on_hide' in self.event_handlers:
            self.event_handlers['on_hide']()

    @staticmethod
    def register_window(window):
        Window.window_instances.append(window)

    # Callback methods that wrap instance methods
    def key_callback(self, glfw_window, key, scancode, action, mods):
        if action == glfw.PRESS:
            self.on_key_press(key, mods)
        elif action == glfw.RELEASE:
            self.on_key_release(key, mods)

    def mouse_button_callback(self, glfw_window, button, action, mods):
        x, y = glfw.get_cursor_pos(glfw_window)
        if action == glfw.PRESS:
            self.on_mouse_press(x, y, button, mods)
        elif action == glfw.RELEASE:
            self.on_mouse_release(x, y, button, mods)

    def cursor_position_callback(self, glfw_window, xpos, ypos):
        # Call mouse motion event
        self.on_mouse_motion(xpos, ypos)

    def scroll_callback(self, glfw_window, xoffset, yoffset):
        x, y = glfw.get_cursor_pos(glfw_window)
        self.on_mouse_scroll(x, y, xoffset, yoffset)

    def resize_callback(self, glfw_window, width, height):
        self.on_resize(width, height)

    def close_callback(self, glfw_window):
        self.on_close()

    def focus_callback(self, glfw_window, focused):
        if focused:
            self.on_gain_focus()
        else:
            self.on_lose_focus()

    def iconify_callback(self, glfw_window, iconified):
        if iconified:
            self.on_hide()
        else:
            self.on_show()

    def maximize_callback(self, glfw_window, maximized):
        if maximized:
            self.on_show()
        else:
            self.on_hide()
