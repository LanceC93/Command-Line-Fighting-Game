class Player:
    def __init__(self, position, side, name):
        self.position = position
        self.name = name
        self.hit = [position - 5, position + 5]
        self.hp = 3
        self.wins = 0
        self.next = -1
        self.side = side   #0 means left side, 1 means right

    def __str__(self):
        return self.name
    
    def next_turn(self, next):
        if(next != 1 and next != 2 and next != 3):
            self.next = -1
        else:
            self.next = next

    def move(self, other):
        if(self.side):
            if(self.hit[0] - 5 > other.hit[1]):
                self.hit[0] -= 5
                self.hit[1] -= 5
        else:
            if(self.hit[0] + 5 < other.hit[0]):
                self.hit[0] += 5
                self.hit[1] += 5
        