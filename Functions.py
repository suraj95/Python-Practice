

def greet_user():
	"""Display a welcome message"""
	print("Hello!")

def greet_user_personalized(username):
	"""Display a personalized welcome message"""
	print("Hello "+username+"!")


def make_pizza(topping='bacon'):
	"""Make a single-topping pizza"""
	print("Have a "+topping+" pizza!")

def add_numbers(x,y):
	"""Add two numbers and return the sum"""
	return x + y



greet_user()

greet_user_personalized("suraj")

make_pizza()
make_pizza('pepperoni')


sum = add_numbers(3,4)
print(sum)