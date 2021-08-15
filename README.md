"""
Created on 2021-08-14 || Version 0.0.1
@author: Mahendra Prasad Gupta

Project: Snakes and ladders  (SLGAME)

"""
# Description:

# Here is a Snakes and Ladders virtual board game to play with your friends and family.
# You don't see this board, it just shows the current position and what is the new value after rolling the dice and what is your new position on the board.

# How to play:

#   1.Each player puts their counter on position 0 as a starting point.
#   2.Take it in turns to roll the dice. Move your counter forward the number of spaces shown on the dice.
#   3.If your counter lands at the bottom of a ladder, you can move up to the top of the ladder.
#   4.If your counter lands on the head of a snake, you must slide down to the bottom of the snake.
#   5.The first player to reach the position of '100' is the first winner, respectively, other players are the other winners.

# class : SLGAME

# Available Methods:

#   1.Main():
#   2.move():
#   3.turns():
#   4.result():
#   5.winner():
#   6.getInput():
#   7.input();

# Available Messages:

#   WELCOME = "====== Welcome To Snakes and ladders ======"
#   RULE = "Minimum 2 players and maximum 4 players can play this game."
#   QUIT = "You want to QUIT this game TRUE or FALSE."
#   GREETINGS = "Hello {} SLGAME welcomes you all to our planet."
#   START = "Let's start the Game."
#   YOURTURN = "Hey {} its your turn please Enter to continue or type QUIT."
#   DICE = "Your curent postion is {} and you got {}. Your New positionis {}."
#   CLIMBED = "{} you climed the ladder,Now your position is {}"
#   BITTEN = "{} you bitten by Snake,Now your position is {}"
#   WINNER = "Congratulations {} you are the {} Winner of this game."
#   GRETER = "{} you got greter value your turn is skip."
#   BYE = "Thank You For Playing This Game."