import turtle as t

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_body = []
        self.shape = "square"
        self.color = "white"
        self.speed = "fastest"

    def snake_chunk(self):
        new_chunk = t.Turtle(shape=self.shape, visible=False)
        new_chunk.color(self.color)
        new_chunk.speed(self.speed)
        new_chunk.penup()
        return new_chunk

    def create_snake_part(self, chunks, new_part = False):
        if not new_part:
            for _ in range(chunks):
                snake = self.snake_chunk()
                self.snake_body.append(snake)
            for chunk in self.snake_body:
                chunk.setpos(x=self.snake_body.index(chunk)*MOVE_DISTANCE*-1, y=0)
                chunk.showturtle()
        else:
            snake = self.snake_chunk()
            self.snake_body.append(snake)
            index = self.snake_body.index(snake)
            snake.setheading(self.snake_body[index - 1].heading())
            snake.showturtle()

    def move_up(self):
        for sn in self.snake_body:
            if sn.heading() != DOWN:
                sn.setheading(UP)
        # create_snake(1, True)

    def move_down(self):
        for sn in self.snake_body:
            if sn.heading() != UP:
                sn.setheading(DOWN)
        # create_snake(1, True)

    def move_left(self):
        for sn in self.snake_body:
            if sn.heading() != RIGHT:
                sn.setheading(LEFT)
        # create_snake(1, True)

    def move_right(self):
        for sn in self.snake_body:
            if sn.heading() != LEFT:
                sn.setheading(RIGHT)
        # create_snake(1, True)

    def move(self):
        for i in reversed(self.snake_body): #self.snake_body[::-1]: #
            if self.snake_body.index(i) == 0:
                i.forward(MOVE_DISTANCE)
            else:
                last_chunk = self.snake_body[self.snake_body.index(i) - 1]
                i.goto(last_chunk.xcor(), last_chunk.ycor())

    def game_over(self):
        for i in self.snake_body[3::]:
            self.snake_body.remove(i)
            i.clear()
            i.hideturtle()
        self.snake_body[0].setpos(x=0, y=0)