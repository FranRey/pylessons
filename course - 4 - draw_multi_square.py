import turtle

def draw_square_with_angle(some_turtle, angle):
	some_turtle.right(angle)

	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

	some_turtle.left(angle)

def draw_squares():
	window = turtle.Screen()
	window.bgcolor("black")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("green")
	brad.speed(2)
	
	draw_square_with_angle(brad, angle)

	window.exitonclick()

draw_squares()
