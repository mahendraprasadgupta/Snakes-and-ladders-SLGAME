
# Snakes & Ladders (SLGAME)

Here is a Snakes and Ladders virtual board game to play with your friends and family.


## Description:

100 squares full of traps and tricks…Roll the dice and try your luck! Ladders will take you up but Snakes will take you down!

  
## Features

- Choose how many players want to play.
- Fantastic result board.
- Attractive Winners List board.
- Nobody lost the game. He is the last winner.
- The game greets you at starting and ending of the game.

  
## Available Methods.

### 1. Main():
```http
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

```

### 2.move():
```http
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
```
- 
### 3.turns():
```http
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
```
### 4.result():
```http
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
```
### 5.winner():
```http
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
```
### 6.getInput():
```http
  def getInput(self):

        self.input()

        if self.players_count > 1 and self.players_count <= 4:
            for x in range(self.players_count):
                self.players_name.append(input(f"Enter {x+1} player Name.:"))
            self.players_pos = [0] * self.players_count
        else:
            return False
```
### 7. input();

```http
  def input(self):
        try:
            self.players_count = int(input("How many players want to play.?"))
        except ValueError:
            print("Please input integer only...")
            self.input()
```




### 7.\_\_init__();

```http
def __init__(self, players_count=0, players_name=[], players_pos=[], winners=[], decision=False, turn=0):
        self.players_count = players_count
        self.players_name = players_name
        self.players_pos = players_pos
        self.winners = winners
        self.decision = decision
        self.turn = turn
``` 

## Available Messages:

```http
1.   WELCOME = "====== Welcome To Snakes and ladders ======"
2.   RULE = "Minimum 2 players and maximum 4 players can play this game."
3.   QUIT = "You want to QUIT this game TRUE or FALSE."
4.   GREETINGS = "Hello {} SLGAME welcomes you all to our planet."
5.   START = "Let's start the Game."
6.   YOURTURN = "Hey {} its your turn please Enter to continue or type QUIT."
7.   DICE = "Your curent postion is {} and you got {}. Your New positionis {}."
8.   CLIMBED = "{} you climed the ladder,Now your position is {}"
9.   BITTEN = "{} you bitten by Snake,Now your position is {}"
10.  WINNER = "Congratulations {} you are the {} Winner of this game."
11.  GRETER = "{} you got greter value your turn is skip."
12.  BYE = "Thank You For Playing This Game."
``` 
## Authors

- [@Mahendra Prasad Gupta](https://github.com/mahendraprasadgupta)


  | Created on 2021-08-14 || Version 0.0.1 |

   Project: Snakes and ladders  (SLGAME)


  
## License

Preferable LICENSEs

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


  
![Logo](https://content.techgig.com/photo/79386213/5-myths-around-python-programming-language-that-every-programmer-must-know.jpg?88712)

    