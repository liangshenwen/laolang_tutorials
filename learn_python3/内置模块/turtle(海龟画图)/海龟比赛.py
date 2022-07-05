# Setting Up the Game Environment:  
# Start by importing the Python `turtle` library. After this, import the built-in `random` library, which you’ll use randomly select an item from a list:
import turtle
import random

# Setting Up the Turtles and Homes  
# You now have to create the two turtles that will represent the players. Each turtle will be a different color, corresponding to the different players. Here, player one is 
# `green` and player two is `blue`:

# One you’ve created the turtles, you place them at their starting positions and make sure that these positions are aligned. Note that you created player two’s turtle by  
# cloning player one’s turtle, changing its color, and placing it at a different starting point.

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# You now need to set up homes for the turtles. These homes will act as the finishing points for each turtle. Each of the turtles’ homes will be represented by a circle. 
# Here, you need to make sure that both `homes` are equidistant from the starting point:
# After drawing the respective homes, you send the turtles back to their starting positions:
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# Creating the Die
# You can create a virtual die for your game with a list, which is an ordered sequence of items. In real life, you might prepare grocery lists and to-do lists to help you stay
# organized. In Python, lists work in a similar way.

# In this case, you’ll be using a list to create your die. First, you define your list of numbers in ascending order from 1 to 6. You can define a list by giving it a name and then
# enclosing its items within square brackets, like this:

die = [1, 2, 3, 4, 5, 6]

# Developing the Game
# It’s time to develop the code for the rest of the game. You’ll be using loops and conditional statements here, so you need to be careful with the indentations and spaces. 
# To start, take a look at the steps your program will need to take to run the game:

# Step 1: You’ll start by telling your program to check if either turtle has reached its home.
# Step 2: If they haven’t, then you’ll tell your program to allow the players to continue trying.
# Step 3: In each loop, you tell your program to roll the die by randomly picking a number from the list.
# Step 4: You then tell it to move the respective turtle accordingly, with the number of steps based on the outcome of this random selection.
# The program keeps repeating this process, and stops once one of the turtles reaches the goal. Here’s how the code looks:
for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        # player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome_one = random.choice(die)
        print("The result of the die roll for player one is: ")
        print(die_outcome_one)
        print("The number of steps for player one will be: ")
        print(20 * die_outcome_one)
        player_one.fd(20 * die_outcome_one)
        # player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome_two = random.choice(die)
        print("The result of the die roll for player two is: ")
        print(die_outcome_two)
        print("The number of steps for play two will be: ")
        print(20 * die_outcome_two)
        player_two.fd(20 * die_outcome_two)

turtle.done()
