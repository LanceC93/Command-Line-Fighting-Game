import Player

def decide_turn(player):
    player.next = int(input(player.name + " " + str(player.hit) + " : Attack(1), Move(2), Block(3) "))
    while(player.next < 0):
        player.next = int(input(player.name + " " + player.hit[0] + " : Attack(1), Move(2), Block(3) "))


def resolve_turn(p1, p2):
    if(p1.next == 2):
        p1.move(other = p2)
    if(p2.next == 2):
        p2.move(other = p1)


def main():
    p1 = Player.Player(40, 0, "Player 1")
    p2 = Player.Player(60, 1, "Player 2")

    ongoing = True
    while (p1.wins != 2 and p2.wins != 2):   #games goes as long as no one has won best of 3
        while(p1.hp > 0 and p2.hp > 0):
            decide_turn(p1)
            decide_turn(p2)
            resolve_turn(p1, p2)


if __name__=="__main__":
    main()