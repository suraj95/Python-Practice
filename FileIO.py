
# Reading a file and storing its lines

filename = 'Text_files/Input_file.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)

# Writing to a file

filename = 'Text_files/Output_file.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming\n")

# Appending to a file

with open(filename, 'a') as file_object:
	file_object.write("I love making games")
