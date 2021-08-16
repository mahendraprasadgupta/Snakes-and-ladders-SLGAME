"""
Created on 2021-08-14 || Version 0.0.1
@author: Mahendra Prasad Gupta

Project: Snakes and ladders  (SLGAME)

"""
import random


class SLGAME:

    # Pre Define Messages used in this Game...!

    WELCOME = "====== Welcome To Snakes and ladders ======"
    RULE = "Minimum 2 players and maximum 4 players can play this game."
    QUIT = "You want to QUIT this game TRUE or FALSE."
    GREETINGS = "Hello {} SLGAME welcomes you all to our planet."
    START = "Let's start the Game."
    YOURTURN = "Hey {} its your turn please Enter to continue or type QUIT."
    DICE = "Your curent postion is {} and you got {}. Your New positionis {}."
    CLIMBED = "{} you climed the ladder,Now your position is {}"
    BITTEN = "{} you bitten by Snake,Now your position is {}"
    WINNER = "Congratulations {} you are the {} Winner of this game."
    GRETER = "{} you got greter value your turn is skip."
    BYE = "Thank You For Playing This Game."
    SNAKES = {47: 5, 29: 9, 38: 15, 53: 33, 62: 57, 92: 70}
    LADDER = {2: 23, 8: 34, 20: 77, 32: 68, 41: 79, 74: 88, 85: 95, 82: 100}

    # __init__(): are used to initialize the object’s state...!

    def __init__(self, players_count=0, players_name=[], players_pos=[], winners=[], decision=False, turn=0):
        self.players_count = players_count
        self.players_name = players_name
        self.players_pos = players_pos
        self.winners = winners
        self.decision = decision
        self.turn = turn

    # input(self): are used to take input from the user and check its int or not work according to input type...!

    def input(self):
        try:
            self.players_count = int(input("How many players want to play.?"))
        except ValueError:
            print("Please input integer only...")
            self.input()

    # getInput(self): are used to take input Name and no. of player to play from the user and  work according to input and condition...!

    def getInput(self):

        self.input()

        if self.players_count > 1 and self.players_count <= 4:
            for x in range(self.players_count):
                self.players_name.append(input(f"Enter {x+1} player Name.:"))
            self.players_pos = [0] * self.players_count
        else:
            return False

    # winner(self, name, i): are used to display winner...!

    def winner(self, name, i):
        print("||===================    Winner    ===================||")
        print()
        self.winners.append(name)
        player_index = self.winners.index(name)
        print(SLGAME.WINNER.format(name, player_index+1))
        print()
        print(self.winners)
        print()
        self.players_count -= 1
        self.players_name.remove(name)
        self.players_pos.pop(i)
        if self.players_count == 0:
            self.result()

    # result(self): are used to display Result...!

    def result(self):
        print("___________________ RESULT _________________")
        print()
        for x in range(len(self.winners)):
            print(f"{x+1} Winner {self.winners[x]}.")
        print()
        print(self.winners)
        print()
        print(SLGAME.BYE)
        print()
        exit()

    # turns(self): are used to rotate turns between players ...!

    def turns(self):
        i = 0
        while i < self.players_count:
            decision = input(SLGAME.YOURTURN.format(
                self.players_name[i])).upper()
            if decision == 'QUIT':
                self.decision = True
            if self.decision:
                self.result()
            else:
                old_val = self.players_pos[i]
                name = self.players_name[i]
                new_val = random.randrange(1, 7)
                fpos = self.move(new_val, old_val, name, i)
                if fpos != True:
                    self.players_pos[i] = fpos
                i += 1

# move(self, new_val, old_val, name, i): are used to move the position of players ...!

    def move(self, new_val, old_val, name, i):
        new_pos = new_val + old_val
        if (new_val + old_val) > 100:
            print(SLGAME.GRETER.format(name))
            return old_val
        else:

            print(SLGAME.DICE.format(old_val, new_val, new_pos))
            if new_pos in SLGAME.SNAKES.keys():
                print(SLGAME.BITTEN.format(name, SLGAME.SNAKES[new_pos]))
                return SLGAME.SNAKES[new_pos]

            elif new_pos in SLGAME.LADDER.keys():
                clpos = SLGAME.LADDER[new_pos]
                print(SLGAME.CLIMBED.format(name, clpos))
                if clpos == 100:
                    self.winner(name, i)
                    return True
                else:
                    return SLGAME.LADDER[new_pos]

            elif new_pos == 100:
                self.winner(name, i)
                return True
            else:
                return new_pos

    # main(self): Main Method Starting of Execution ...!

    def main(self):
        print(SLGAME.WELCOME)
        print(SLGAME.RULE)
        if self.getInput() == False:
            print(SLGAME.RULE)
            self.decision = input(SLGAME.QUIT).capitalize()
            if self.decision:
                self.getInput()
            else:
                self.result()
        else:
            print(SLGAME.GREETINGS.format(self.players_name))
            print(SLGAME.START)

            while self.decision != True:
                self.turns()


# Object Creation and call main() ...!
SL = SLGAME()
SL.main()
