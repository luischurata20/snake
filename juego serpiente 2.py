from turtle import Screen, Turtle
import time
import random    #funcion declaración en Python  crear números aleatorios

segements = []

def up():
    if new_segment.heading() != 270:
        new_segment.setheading(90)
def down():
    if new_segment.heading() != 90:
        new_segment.setheading(270)
def left():
    if new_segment.heading() != 0:
        new_segment.setheading(180)
def right():
    if new_segment.heading() != 180:
        new_segment.setheading(0)

# Pantalla
screen = Screen()#se esta creando una pantalla
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)#animacion

# Serpiente
new_segment = Turtle("square")# se estacreando objete en forma cuadra
new_segment.color("white")
new_segment.penup() #para no dibujar nada en la pantalla
new_segment.goto(0, 0) #posicion
segements.append(new_segment)# para agregar nuevos segementos finales

# Comida
food = Turtle("circle") #objeto
food.color("blue")
food.penup()# no dejar huella
random_x = random.randint(-280, 280) #posicion aleatoria de la comida.rango
random_y = random.randint(-280, 280)
food.goto(random_x, random_y)

# Score
score = Turtle()
score.color("white")
score.penup()
score.goto(0, 265)
score.hideturtle()
score_board = 0
score.write(f"Score: {score_board}", align="center", font=("Arial", 24, "bold"))


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    # Detectar toque de comida
    if new_segment.distance(food) < 15:
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        food.goto(random_x, random_y)

        next_segment = Turtle("square")
        next_segment.color("white")
        next_segment.penup()
        segements.append(next_segment)

        # Actualizar puntuación
        score.clear()
        score_board = score_board + 1   #score_board += 1
        score.write(f"Score: {score_board}", align="center", font=("Arial", 24, "bold"))

    if len(segements) > 1:
        for i in range(len(segements) - 1, 0, -1):
            segements[i].goto(segements[i - 1].xcor(), segements[i - 1].ycor())
    new_segment.forward(20)

    #Detectar toque con paredes
    head = segements[0]
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        game_is_on = False
        score.goto(0, 0)
        score.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    #Detectar toque con serpiente
    for segment in segements:
        if segment == head:
            pass
        elif head.distance(segment) < 10:
            game_is_on = False
            score.goto(0, 0)
            score.write("GAME OVER", align="center", font=("Arial", 24, "bold"))



screen.exitonclick()