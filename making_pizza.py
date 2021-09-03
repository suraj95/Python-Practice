import pizza

pizza.make_pizza('medium','pepperoni')
pizza.make_pizza('medium','pepperoni','bacon','mushroom','onion')


import pizza as p

p.make_pizza('large','pepperoni')
p.make_pizza('large','pepperoni','bacon','mushroom','onion')

from pizza import make_pizza as mp 

mp('small','chicken')
mp('small','paneer','capsicum','onion')



