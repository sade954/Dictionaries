#Creating a Dictionary
ages = { 'Candace': 37, 'Daniel': 31, 'Kayleigh': 25 }
ages
{ 'Candace': 37, 'Daniel': 31, 'Kayleigh': 25 }

#Indexing a Dictionary
ages['Candace']
37
#Adding to a Dictionary
ages['Derek'] = 38
Type ages { 'Candace': 37, 'Daniel': 31, 'Kayleigh': 25, 'Derek': 38 }

#Reassigning a value for a dictionary
ages['Candace'] = 37
Type ages
{ 'Candace': 37, 'Daniel': 31, 'Kayleigh': 25, 'Derek': 38 }

#Using a dict class
weights = dict(Candace=156, Daniel=240, Kayleigh= 125)
Type weights
{Candace=156, Daniel=240, Kayleigh= 125}

#Using a tuple in a dict class
colors = dict(['Candace', 'Olive Green'), ('Daniel', 'Blue'), ('Kayleigh', 'Black')])
Type colors
{'Candace': 'Olive Green', 'Daniel': 'Blue' 'Kayleigh': 'Black'}

#Using the keys method for a dictionary
ages = {'Candace:' 37, 'Kayleigh': 25}
ages.keys()
dict_keys(['Candace', 'Kayleigh'])

#Giving the list back the keys
list(ages.keys())
['Candace', 'Kayleigh']

#Creating dict values
ages.values()
dict.values([37, 25])

#Creating dict items
ages.item()
dict_items([('Candace', 37), ('Kayleigh', 25)])
list(ages.items()) to create a lits
[('Candace', 37), ('Kayleigh', 25)]
