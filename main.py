import Player
import keyboard
import fpstimer
import time

def decide_turn(player):
    player.next = int(input(player.name + " : Attack(1), Move(2), Block(3) "))
    while(player.next < 0):
        player.next = int(input(player.name + " : Attack(1), Move(2), Block(3) "))


def resolve_turn(p1, p2):
    if(p1.next == 2):
        p1.move(other = p2)
    if(p2.next == 2):
        p2.move(other = p1)


def main():
    timer = fpstimer.FPSTimer(20)
    p1 = Player.Player(3, 0, "Player 1", "#")
    p2 = Player.Player(6, 1, "Player 2", "@")

    while (p1.wins != 2 and p2.wins != 2):   #games goes as long as no one has won best of 3
        print("\nRound " + str(p1.wins + p2.wins + 1) + ": ", end = "")
        print("FIGHT!")
        stage = ["_","_","_","_","_","_","_","_","_","_"]  #initialize stage
        p1.position = 3
        p2.position = 6
        p1.hp = 3
        p2.hp = 3
        stage[p1.position] = p1.icon
        stage[p2.position] = p2.icon
        print(*stage, end = "\r")

        while(p1.hp > 0 and p2.hp > 0):
            if(p1.recovery == 0):
                if keyboard.is_pressed(" "):
                    p1.attack(p2, stage)
                if keyboard.is_pressed("d"):
                    p1.move(p2, 1, stage)
                elif keyboard.is_pressed("a"):
                    p1.move(p2, 0, stage)
            else:
                p1.recovery -= p1.recovery
            if(p2.recovery == 0):
                if keyboard.is_pressed("up arrow"):
                    p2.attack(p1, stage)
                elif keyboard.is_pressed("left arrow"):
                    p2.move(p1, 0, stage)
                elif keyboard.is_pressed("right arrow"):
                    p2.move(p1, 1, stage)
            else:
                p2.recovery -= p2.recovery
            print(*stage, end = "\r")     #redisplay stage
            timer.sleep()
        if(p1.hp == 0):
            p2.wins += 1
        else:
            p1.wins += 1


if __name__=="__main__":
    main()