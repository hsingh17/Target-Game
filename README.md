# Target Game
Target Game made in Python, using PyGame.

# Motivation
When I used to play FPS games, like Counter-Strike, I would frequent this website called [aimbooster](www.aimbooster.com). So when I was messing around with PyGame, I thought that recreating a simpler version of aimbooster would be fun.

![Targets](https://i.imgur.com/aYLDWew.gif)
# Installation
Before running this Target game, some prerequisites:
1. Python3
2. PyGame

## Python3
To install Python3 through the terminal, run the following:

`$ sudo apt-get update`

`$ sudo apt-get install python3.6`

For Windows, follow this [link](https://www.python.org/downloads/windows/).

## PyGame
To install Pygame through the terminal, use the following (skip to second line if PIP is already installed):

`$ sudo apt install python3-pip`

`$ pip3 install pygame`

Or you could go to the [PyGame website](https://www.pygame.org/news)

# Usage
To run the program, run either of the following in your terminal

`$ python3  TargetGame.py`

or

`$ chmod +x TargetGame.py`

`./TargetGame.py`

**Note: Make sure to include the audio folder in the same directory as the game**

# Playing
1. LMB to click on the Target
2. `Q` to exit once game is over
3. `R` to restart once game is over

There are 2 numbers displayed in the game. The first number, the one on top of the other, is the number of total targets hit. The other number is your current streak. The game gets progressively harder for every 10 you hit. You are not penalized for missing a target, only if you do not hit it in time (before it shrinks).

# Contributing
If you happen to find bugs or want to add a feature. Go for it!

*Project by Harjot Singh*
