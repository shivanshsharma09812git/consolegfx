#📌 examples/rotating_ball.py
from consolegfx.canvas import Canvas
from  consolegfx import Renderer
from consolegfx import Entity

from math import sin, cos
from rich.console import Console
import time, keyboard, os 
import numpy as np

tiles={
    0:{"char": "  ", "style": None},
    1:{"char": "()", "style": None}
}
sprite=np.array([
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1]
])
console=Console(force_terminal=True, soft_wrap=False)
term_size=os.get_terminal_size()
canvas = Canvas(45, term_size.columns // 2)
renderer = Renderer(canvas, tiles, console)
entity = Entity()
entity.add_sprite(canvas, sprite)
X=10
Y=10
def update():
    global X, Y, term_size
    canvas.clear(0)
    entity.move_sprite(X, Y, 0)
    if keyboard.is_pressed("w") and Y > 0:Y-=1
    if keyboard.is_pressed("a") and X > 0:X-=1
    if keyboard.is_pressed("s") and Y+8 < term_size.lines:Y+=1
    if keyboard.is_pressed("d") and X+8 < term_size.columns // 2:X+=1

renderer.render_loop(update, fps=60)