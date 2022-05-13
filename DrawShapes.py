#5-13-22
#Shapes Assignment
import turtle
window = turtle.Screen()
window.screensize(400, 400)
window.bgcolor('indigo')
window.title('Shapes')
turt = turtle.Turtle()
turt.shape("turtle")

def end ():
  turt.end_fill()

def draw(x,y, color):
  turt.penup()
  turt.goto(x, y)
  turt.pendown()
  turt.fillcolor(color)
  turt.begin_fill()

def cord(forward, right):
  turt.forward(forward)
  turt.right(right)

draw(80,80,'#FFFF00')
for i in range(6):
  cord(40, 60)
  #360/60 = 60
end()


#octagon
draw(-20, 20,'#90EE90' )
for i in range(8):
  cord(30, 45)
  #360/8 = 45 
end()

#triangle
draw(120, -110, '#FFC0CB')
turt.right(60)

for i in range(3):
  cord(70, 120)
    #320/3
end()
window.exitonclick()
