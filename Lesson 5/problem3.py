from turtle import*

toht = Turtle()

toht.color('blue')
toht.pensize(5)
toht.speed(9)
toht.shape('turtle')

for x in range(6):
	toht.forward(50)
	toht.left(60)

mainloop()
