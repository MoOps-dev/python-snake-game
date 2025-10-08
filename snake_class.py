import turtle as t

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

class Snake:
    """Snake class will handle snake creation, movement and death"""
    def __init__(self):
        self.snake_body = []
        self.shape = "square"
        self.color = "white"
        self.speed = "fastest"

    def snake_chunk(self):
        """Creates a snake chunk using a new turtle object"""
        new_chunk = t.Turtle(shape=self.shape, visible=False)
        new_chunk.color(self.color)
        new_chunk.speed(self.speed)
        new_chunk.penup()
        return new_chunk

    def create_snake_part(self, chunks, new_part = False):
        """Creates a new snake that has the number of 'chunks' or add a new chunk(s) to the existing snake"""
        if not new_part:
            for _ in range(chunks):
                snake = self.snake_chunk()
                self.snake_body.append(snake)
            # arrange the snake chunks for the first time
            for chunk in self.snake_body:
                chunk.setpos(x=self.snake_body.index(chunk)*MOVE_DISTANCE*-1, y=0)
                chunk.showturtle()
        else:
            snake = self.snake_chunk()
            self.snake_body.append(snake)
            index = self.snake_body.index(snake)
            # change the chunk direction to match the rest of the body
            snake.setheading(self.snake_body[index - 1].heading())
            snake.showturtle()

    def move_up(self):
        """Changes the heading of the snake chunks to UP"""
        for sn in self.snake_body:
            if sn.heading() != DOWN:
                sn.setheading(UP)

    def move_down(self):
        """Changes the heading of the snake chunks to DOWN"""
        for sn in self.snake_body:
            if sn.heading() != UP:
                sn.setheading(DOWN)

    def move_left(self):
        """Changes the heading of the snake chunks to LEFT"""
        for sn in self.snake_body:
            if sn.heading() != RIGHT:
                sn.setheading(LEFT)

    def move_right(self):
        """Changes the heading of the snake chunks to RIGHT"""
        for sn in self.snake_body:
            if sn.heading() != LEFT:
                sn.setheading(RIGHT)

    def move(self):
        """Moves the snake's head forward and changes each other chunk's position to the preceding chunk position"""
        # Use a loop with the snake body starting from last chunk in the body
        for i in reversed(self.snake_body): #self.snake_body[::-1]:
            if self.snake_body.index(i) == 0:
                i.forward(MOVE_DISTANCE)
            else:
                last_chunk = self.snake_body[self.snake_body.index(i) - 1]
                i.goto(last_chunk.xcor(), last_chunk.ycor())

    def game_over(self):
        """Resets the snake to the original size and resets its position on the screen"""
        for i in self.snake_body[3::]:
            self.snake_body.remove(i)
            i.clear()
            i.hideturtle()
        self.snake_body[0].setpos(x=0, y=0)