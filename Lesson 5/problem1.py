from turtle import*

toht = Turtle()

toht.color('blue')
toht.pensize(5)
toht.speed(9)
toht.shape('turtle')

for x in range(3):
	toht.forward(60)
	toht.left(120)
	toht.forward(60)

mainloop()