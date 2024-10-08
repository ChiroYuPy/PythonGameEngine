import inspect
import time

from GameEngine import Window


class App:
    def __init__(self, fix_update_interval, fps):
        self.running = True

        self.fix_update_interval = fix_update_interval
        self.fps = fps

        self.current_time = time.time()
        self.accumulator = 0

        self.update_handlers = {}

    def params(self, fix_update_interval=None, fps=None):
        self.fix_update_interval = fix_update_interval if fix_update_interval is not None else self.fix_update_interval
        self.fps = fps if fps is not None else self.fps

    def event(self, func):
        event_name = func.__name__

        # Ne permettre que les méthodes 'on_update' et 'on_fix_update'
        allowed_methods = ["on_update", "on_fix_update"]
        if event_name not in allowed_methods:
            raise ValueError(f"{event_name} is not allowed. Only 'on_update' and 'on_fix_update' are allowed.")

        # Vérifier que l'événement n'est pas déjà enregistré
        if event_name in self.update_handlers:
            raise ValueError(f"{event_name} already registered")

        # Vérifier que le nombre d'arguments correspond à celui de la méthode d'origine
        expected_args = len(inspect.signature(getattr(self, event_name)).parameters)
        actual_args = len(inspect.signature(func).parameters)

        if actual_args != expected_args:
            raise ValueError(f"{event_name} expects {expected_args} arguments but got {actual_args}")

        print(f"{event_name} registered")
        self.update_handlers[event_name] = func
        return func

    def update(self):
        last_time = self.current_time
        self.current_time = time.time()
        dt = self.current_time - last_time

        self.accumulator += dt

        self.on_update(dt)
        while self.accumulator >= self.fix_update_interval:
            self.accumulator -= self.fix_update_interval
            self.on_fix_update(self.fix_update_interval)

        time.sleep(1/self.fps)
        for window in Window.window_instances:
            window.update()

    def on_update(self, dt):
        if "on_update" in self.update_handlers:
            self.update_handlers["on_update"](dt)

    def on_fix_update(self, fdt):
        if "on_fix_update" in self.update_handlers:
            self.update_handlers["on_fix_update"](self.fix_update_interval)

    def run(self):
        while self.running:
           self.update()
