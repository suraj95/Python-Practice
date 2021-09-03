

class Dog():
	"""Represent a dog"""

	def __init__(self,name):
		"""Initialize dog object"""
		self.name = name

	def sit(self):
		"""Simulate sitting"""
		print(self.name + " is sitting.")


Peso = Dog('Peso')
Nala = Dog('Nala')

print(Peso.name+ " is a great dog!")
print(Nala.name+ " is a great dog!")

Peso.sit()
Nala.sit()

class SARDog(Dog):
	"""Represent a Search and Rescue Dog"""

	def __init__(self,name):
		"""Initialize the sardog"""
		super().__init__(name)

	def search(self):
		"""Simulate searching"""
		print(self.name + " is searching")


Willie = SARDog("Willie")

print(Willie.name+ " is a great dog!")
Willie.sit()
Willie.search()

