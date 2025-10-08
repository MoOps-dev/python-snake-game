# Python Snake
Python Snake is a basic snake game created using the Turtle library as a part of a Python course.

__Language practices within this project:__
- OOP concepts
- Listening to keyboard input using screen object in Turtle
- Working with x,y axes
- List slicing
- Looping through reversed lists using any of these methods
    ```` python
    reserved(list)
    ````
    or 
    ```` python
    list[::-1]
    ````
- File reading and writing to save user's highest score
    ```` python
    with open("score.txt", "r") as file:
        # do something
    ````
  or
    ```` python
    with open("score.txt", "w") as file:
        # do something
    ````
- Loops .. for, while etc..

__Coded Mechanics:__
- Snake starts as 3 chunks and gains an additional chunk each time it eats an apple
- An apple will appear in a random location until it gets eaten by the snake
- The snake will lose all length and moves to the starting point if it dies
- Snake death conditions:
    - Colliding with any edge of the screen window
    - colliding with itself
- Each apple increase score by 1
  - score resets upon snake death
  - highest score is recorded upon snake death
- Snake speed is fixed