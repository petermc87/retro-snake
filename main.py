from turtle import Screen
from snake_move import Snake
from food import Food
from scoreb import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Shnake")
screen.tracer(0)
# screen.done()

# this turns of the display of moving each square into place
# call the class and give it an attribute. It will first run the __init__ in the class, which will
# create the first 3 squares that the snake begins with
snake = Snake()

# initializes the class with teh food object. Look for this in the "food.py"
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
# listens for the user to enter a key stroke, and then runs snake.up method in the
# snake class after it does
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

cont_game = True
while cont_game:
    # once the 3 squares are made, the snake appears in the form you have crated in one flash on the
    # screen
    screen.update()
    time.sleep(.05)
    snake.follow()

    if snake.head.distance(food) < 15:
        # we are using the attribute defined as "head" (snakes head) to check if its less
        # than 15 pixels away from the food. This will mean it is close enough to call it a collision. Distance is a
        # method from the Turtle class
        snake.grow()
        # moving the food to a random location
        food.new_loc()
        score.counter()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # updating the high score
        score.high_score()
        # resetting the position of the starting snake (three squares)
        snake.reset_pos()

    for squares in snake.square_list[1:]:
        # this is so that if any of the squares get within 15 pixels of each other,
        # its game over
        if snake.head.distance(squares) < 5:
            # same as above for high score
            score.high_score()
            snake.reset_pos()
            # score.game_over()

    # after each condition is checked after a move of the snake, the screen is updated again to show
    # the next move
    screen.update()

screen.exitonclick()
