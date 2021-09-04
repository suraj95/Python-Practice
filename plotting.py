import matplotlib.pyplot as plt

# Line graph

x_values = [0,1,2,3,4,5]
squares = [0,1,4,9,16,25]

plt.plot(x_values,squares)
plt.show()

# Scatter plot

x_values = list(range(1000))
squares = [x**2 for x in x_values]

plt.scatter(x_values,squares)
plt.title("Squares of numbers from 0-999", fontsize = 24)
plt.xlabel("Numbers", fontsize = 18)
plt.ylabel("Squares", fontsize = 18)
plt.show()