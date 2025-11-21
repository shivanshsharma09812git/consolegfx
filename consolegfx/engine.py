import numpy as np
from rich.text import Text

"""
consolegfx/
    consolegfx/
        __init__.py 
        canvas.py # to conver array to text 
        engine.py # easy to use engine features like collision, entites
        renderer # render single/looped frame(s) with rich.live 
        layouts # layouts for good look and control text size according to the terminal's size
        shapes.py # basic drawing shapes
        tiles.py # for easy control over data and array 
    dependencies/
        rich, numpy # if the user dont have them installed 
    examples/
        rotating_ball.py #etc...
    pyproject.toml
    README.md
     
"""

def draw(arr, tilemap, colored=False):
    if not colored:
        # --- Plain text rendering ---
        text = ""
        for row in arr:
            for cell in row:
                tile = tilemap.get(cell, {"char": "??"})
                text += tile["char"]
            text += "\n"
        return text
    
    # --- Rich Text rendering ---
    if colored:
        text = Text()
        for row in arr:
            for cell in row:
                tile = tilemap.get(cell, {"char": "??", "style": None})
                text.append(tile["char"], style=tile["style"])
            text.append("\n")
        return text
    
def color(x, y, style, text, arr):
    text=arr[:x*y]+Text(text, style=style)+arr[x*y+1:]
    return text

def draw_ellipse(cx, cy, rx, ry, value, arr, fill=False):
    height = len(arr)
    width = len(arr[0])

    for y in range(cy - ry, cy + ry + 1):
        if y < 0 or y >= height: continue
        for x in range(cx - rx, cx + rx + 1):
            if x < 0 or x >= width: continue
            # normalize x and y based on ellipse equation
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            equation = dx**2 + dy**2

            # outline tolerance
            if fill:
                if equation <= 1.0:
                    arr[y][x] = value
            else:
                # fuzzy edge check
                if 0.95 <= equation <= 1.05:
                    arr[y][x] = value


def drawRect(x, y, width, height, value, arr):
    # Draw directly on the array, not the string
    for j in range(y, y + height):
        for i in range(x, x + width):
            # Check bounds to avoid IndexError
            if 0 <= j < arr.shape[0] and 0 <= i < arr.shape[1]:
                arr[j, i] = value

def draw_circle(cx, cy, radius, value, arr):
    x = radius
    y = 0
    d = 1 - radius

    while x >= y:
        for dx, dy in [
            (x, y), (y, x), (-y, x), (-x, y),
            (-x, -y), (-y, -x), (y, -x), (x, -y)
        ]:
            px, py = cx + dx, cy + dy
            if 0 <= px < len(arr[0]) and 0 <= py < len(arr):
                arr[py][px] = value
        y += 1
        if d < 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1

def draw_line(x1, y1, x2, y2, value, arr):
    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy
    while True:
        if 0 <= x1 < len(arr[0]) and 0 <= y1 < len(arr):
            arr[y1][x1] = value
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy