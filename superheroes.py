
# Reads superheroes.json (in this folder)
import json

with open('superheroes.json','r') as f:
  superheroes = json.load(f)

#print(superheroes)

# create an empty array called powers
powers = []

# Loop thorough the members of the squad, and append the powers of each to the powers array.
members = superheroes['members']
for member in members:
	this_members_powers = member['powers']
	powers.append(this_members_powers)

# Prints those powers to the terminal
print(powers)