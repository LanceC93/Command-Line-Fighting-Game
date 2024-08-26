class Player:
    def __init__(self, position, side, name, icon):
        self.position = position
        self.name = name
        self.hp = 3
        self.wins = 0
        self.next = -1
        self.icon = icon
        self.side = side   #0 for left side, 1 for right
        self.recovery = 0           ## of recovery frames

    def __str__(self):
        return self.name
    
    def next_turn(self, next):
        if(next != 1 and next != 2 and next != 3):
            self.next = -1
        else:
            self.next = next

    def move(self, other, direction, stage):
        if(direction):
            if(self.position + 1 != other.position and self.position != 9 ):
                stage[self.position] = "_"
                self.position += 1
                stage[self.position] = self.icon

        elif(self.position - 1 != other.position and self.position != 0 ):
            stage[self.position] = "_"
            self.position -= 1
            stage[self.position] = self.icon
            

    def attack(self, other, stage):
        self.recovery = 30
        if(self.side):
            if(self.position - 2 <= other.position):
                other.hp -= 1
            stage[self.position - 1] = "-"
            if(self.position > 2):
                stage[self.position - 2] = "<"
        else:
            if(self.position + 2 >= other.position):
                other.hp -= 1
            stage[self.position + 1] = "-"
            if(self.position > 2):
                stage[self.position + 2] = ">"
        


        