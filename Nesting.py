
users = []

new_user = {
	'last': 'fermi',
	'first': 'enrico',
	'username': 'efermi'}

users.append(new_user)

for user_dict in users:
	for k,v in user_dict.items():
		print(k+": "+v)
	print("\n")

users = [ 
	{ 
		'last': 'fermi', 
		'first': 'enrico', 
		'username': 'efermi', 
	}, 
	{ 
		'last': 'curie', 
		'first': 'marie', 
		'username': 'mcurie'
	}
]

for user_dict in users:
	for k,v in user_dict.items():
		print(k+": "+v)
	print("\n")

fav_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell']
}

for name,languages in fav_languages.items():
	print(name+":")
	for lang in languages:
		print("-"+lang)


users = {
	'aeinstein': 
		{ 
			'first': 'albert', 
			'last': 'einstein', 
			'location': 'princeton' 
		}, 
	'mcurie': 
		{ 
			'first': 'marie', 
			'last': 'curie', 
			'location': 'paris'
		}
}

for username, user_dict in users.items():
	print("\n Username: "+username)
	full_name = user_dict['first'] + " " + user_dict['last']
	location = user_dict['location']

	print("Full name: " + full_name.title())
	print("location: " + location.title())


from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages['jen']= ['python','ruby']
fav_languages['sarah']=['c']
fav_languages['edward']= ['ruby','go']
fav_languages['phil']= ['python','haskell']

for name,languages in fav_languages.items():
	print(name+":")
	for lang in languages:
		print("-"+lang)