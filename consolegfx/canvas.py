from rich.console import Console
from rich.text import Text
import numpy as np

class Canvas:
    """
    =
    WARNING
    =
    **This canvas rendering is based on your terminal please use it carefully.**
    **If you see flickering in your terminal you can do the following**
    - Reduce your terminal size
    - Get an RGB or HEXDECIMAl supported terminal
    """

    """Basic canvas class for drawing"""
    def __init__(self, width, height, value=0):
        self.data=np.full([width, height], value, dtype=int)
    def clear(self, value:int=0) -> None:
        self.data[:]=value 
    def to_text(self, tilemap:dict, colored:bool=True) -> str:
        if not colored:
            # --- Plain text rendering ---
            text = ""
            for row in self.data:
                for cell in row:
                    tile = tilemap.get(cell, {"char": "??"})
                    text += tile["char"]
                text += "\n"
            return text
            
            # --- Rich Text rendering ---
        if colored:
            text = Text()
            for row in self.data:
                for cell in row:
                    tile = tilemap.get(cell, {"char": "??", "style": None})
                    text.append(tile["char"], style=tile["style"])
                text.append("\n")
            return text
    def draw_rect(self, x:int, y:int, width:int, height:int, value:int, fill:bool=True) -> None:
        """Draws rect in the suggested x, y with its width and height according to the fill style."""
        for j in range(y, y + height):
            for i in range(x, x + width):
                # Check bounds to avoid IndexError
                if 0 <= j < self.data.shape[0] and 0 <= i < self.data.shape[1] and fill:
                    self.data[j, i] = value
                elif 0 <= j < self.data.shape[0] and 0 <= i < self.data.shape[1] and not fill:
                    self.draw_line(x, y, x+width-1, y, value)   # added minus 1 since it counts from x/y
                    self.draw_line(x, y, x, y+height-1, value)
                    self.draw_line(x+width-1, y, x+width-1, y+height-1, value)
                    self.draw_line(x, y+height-1, x+width-1, y+height-1, value)
    def draw_ellipse(self, cx:int, cy:int, rx:int, ry:int, value:int, fill:bool=True) -> None:
        """Draw an ellipse"""
        height = len(self.data)
        width = len(self.data[0])

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
                        self.data[y][x] = value
                else:
                    # fuzzy edge check
                    if 0.95 <= equation <= 1.05:
                        self.data[y][x] = value
    def draw_line(self, x1:int, y1:int, x2:int, y2:int, value:int) -> None:
        """Draws an line"""
        dx = abs(x2 - x1)
        dy = -abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx + dy
        while True:
            if 0 <= x1 < len(self.data[0]) and 0 <= y1 < len(self.data):
                self.data[y1][x1] = value
            if x1 == x2 and y1 == y2: 
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x1 += sx
            if e2 <= dx:
                err += dx
                y1 += sy

