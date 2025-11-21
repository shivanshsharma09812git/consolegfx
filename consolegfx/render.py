import time, keyboard , os
from rich.live import Live

class Renderer:
    def __init__(self, canvas, tiles, console):
        self.canvas = canvas
        self.tiles = tiles
        self.console = console

    def render_loop(self, update_fn, fps=30, escape_key="escape"):
        frame_time = 1 / fps
        os.system('cls' if os.name == 'nt' else 'clear')

        with Live(
            self.canvas.to_text(self.tiles),
            refresh_per_second=fps,
            transient=False,
            screen=False,
            console=self.console
        ) as live:

            while True:
                if keyboard.is_pressed(escape_key):
                    break

                update_fn()  # FIRST update game state
                live.update(self.canvas.to_text(self.tiles))  # THEN render

                time.sleep(frame_time)

        os.system('cls' if os.name == 'nt' else 'clear')
