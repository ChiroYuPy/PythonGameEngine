from .window import Window
from .app import App
from . import components, math, utils
app = App(fix_update_interval=1/20, fps=60)