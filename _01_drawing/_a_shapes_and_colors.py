import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
turt = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
turt.shape('turtle')
# Set your turtle's speed using .speed(2)
turt.speed(50000)
# Set your turtle's color using .color('green') and .pencolor('blue')
turt.color('blue')
turt.pencolor('blue')
# Move your turtle forward using .forward(100)
turt.forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
for i in range(3):
    turt.right(90)
    turt.forward(100)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
turt.goto(50,50)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
turt.begin_fill()
turt.circle(200,400)
turt.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
turt.goto(100,100)
#square
turt.begin_fill()
for i in range(4):
    turt.right(90)
    turt.forward(100)
turt.end_fill()
turt.goto(-180,-180)
#triangle
turt.color('red')
turt.begin_fill()
for i in range(3):
    turt.left(120)
    turt.forward(50)
turt.end_fill()
#octogon
turt.goto(100,-100)
turt.color('purple')
turt.begin_fill()
for i in range (8):
    turt.right(60)
    turt.forward(150)
turt.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
