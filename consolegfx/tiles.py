

class TileMap:
    def __init__(self):
        self.tiles={}
    def add(self, id:int, char:str, fg_color:str=None, bg_color:str=None) -> None:
        self.tiles[id]={"char":char, "style":fg_color, "style_on":bg_color}
    def get(self, id):
        return self.tiles[id]