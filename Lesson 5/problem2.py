from turtle import*

toht = Turtle()

toht.color('blue')
toht.pensize(5)
toht.speed(9)
toht.shape('turtle')


for x in range(3):
	toht.forward(80)
	toht.left(120)


for x in range(12):
	for x in range(3):
		toht.forward(80)
		toht.left(120)
	toht.left(30)
	



mainloop()