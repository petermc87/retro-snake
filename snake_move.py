from turtle import Turtle
# initial position stays fixed. if there is an error with this, or it
# needed to change for any reason (example, maybe a different initial position) it is much easier to change it in one
# location here than in multiple locations within the code where it is called.
STARTING_LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]
# same as above

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # first, create an empty list to store the squares
        self.square_list = []
        # secondly, run the method "create_squares". square_list is used in here
        self.create_squares()
        # creating a new variable and naming it the head. You will be changing the
        # direction of the head and the rest of the squares will follow
        self.head = self.square_list[0]

    def create_squares(self):
        for pos in STARTING_LOCATIONS:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(pos)
            self.square_list.append(new_square)

    def follow(self):
        for sq_num in range(len(self.square_list) - 1, 0, -1):
            # going from 2,1,0, starting at 2 stepping backwards to 0
            # getting hold of the 2nd to last position (pos 1) x coor in sq_list
            new_x = self.square_list[sq_num - 1].xcor()
            # getting hold of the 2nd to last position (pos 1) y coor in sq_list
            new_y = self.square_list[sq_num - 1].ycor()
            # moving the last square (pos 2) to pos 1
            self.square_list[sq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        # Storing the xy coordinates of the last positon.
        last_square_x = self.square_list[len(self.square_list) - 1].xcor()
        last_square_y = self.square_list[len(self.square_list) - 1].ycor()
        # Instantiating a new square and calling it the tail (where we will grow the snake).
        tail_square = Turtle("square")
        tail_square.color("white")
        tail_square.penup()
        # Using the Turtle library to move the square to the stored coordinates.
        tail_square.goto(last_square_x, last_square_y)
        # Finally, appending the square.
        self.square_list.append(tail_square)

    def up(self):
        # this means that if the current heading is not down (i.e. left right or up),
        # then you are allowed to move up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_pos(self):
        # resetting the position as soon as the snake hits itself or goes out of bounds. The position of the old snake
        # gets moved to a location way off screen (this is because the old snake will stay on the screen
        for pos in self.square_list:
            pos.goto(1000, 1000)
        # clear the snake list to start all over again with the create_squares() method
        self.square_list.clear()
        self.create_squares()
        # make sure to redefine what position in the list the head is, otherwise there will be squares appearing on
        # different parts of the screen
        self.head = self.square_list[0]


