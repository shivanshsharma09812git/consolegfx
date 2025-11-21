

class Entity:
    def __init__(self):
        pass 
    def add_sprite(self, canvas, sprite):
        self.canvas=canvas 
        self.sprite=sprite 
    def move_sprite(self, x, y, erase_value):
        self.x=x 
        self.y=y 
        self.erase_sprite(erase_value)
        self.draw_sprite()
    def draw_sprite(self):
        self.sprite_width=self.sprite.shape[1]
        self.sprite_height=self.sprite.shape[0]
        row_i=0
        cell_i=0
        for j in range(self.y, self.y + self.sprite_height):
            for i in range(self.x, self.x + self.sprite_width):
                if 0 <= j < self.canvas.data.shape[0] and 0 <= i < self.canvas.data.shape[1]:
                    self.canvas.data[j][i]=self.sprite[row_i][cell_i]
                    cell_i+=1 
            row_i+=1
            cell_i=0 
        row_i=0
    def erase_sprite(self, value):
        self.sprite_width=self.sprite.shape[1]
        self.sprite_height=self.sprite.shape[0]
        row_i=0
        cell_i=0
        for j in range(self.y, self.y + self.sprite_height):
            for i in range(self.x, self.x + self.sprite_width):
                if 0 <= j < self.canvas.data.shape[0] and 0 <= i < self.canvas.data.shape[1]:
                    self.canvas.data[j][i]=value 
                    cell_i+=1 
            row_i+=1
            cell_i=0 
        row_i=0