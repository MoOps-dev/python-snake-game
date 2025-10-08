import time
import food_class
import score_class
import snake_class
import turtle as t

score = score_class.Score()
snake = snake_class.Snake()
food = food_class.Food()

SCREEN = t.Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)
SCREEN.listen()
SCREEN.onkey(key="Up", fun=snake.move_up)
SCREEN.onkey(key="Left", fun=snake.move_left)
SCREEN.onkey(key="Down", fun=snake.move_down)
SCREEN.onkey(key="Right", fun=snake.move_right)

WINDOW_WIDTH = SCREEN.window_width()
WINDOW_HEIGHT = SCREEN.window_height()

game_is_on = False

def create_snake(chunks, new_part = False):
    global game_is_on
    if not new_part:
        snake.create_snake_part(chunks)
        food.spawn(WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20)
        SCREEN.update()
        game_is_on = True
    else:
        snake.create_snake_part(chunks, new_part)

create_snake(3)

while game_is_on:
    if food.is_visible() and snake.snake_body[0].distance(food) <= 15:
        food.spawn(WINDOW_WIDTH - 40, WINDOW_HEIGHT - 40)
        create_snake(1, True)
        score.increase_score()

    if snake.snake_body[0].xcor() >= 300 or snake.snake_body[0].xcor() <= -300 or snake.snake_body[0].ycor() <= -300 or snake.snake_body[0].ycor() >= 300:
        #game_is_on = False
        score.game_over()
        snake.game_over()

    for i in snake.snake_body[1:len(snake.snake_body)]:
        if i.distance(snake.snake_body[0]) < 10:
            #game_is_on = False
            score.game_over()
            snake.game_over()

    snake.move()

    SCREEN.update()
    time.sleep(0.2)


SCREEN.exitonclick()