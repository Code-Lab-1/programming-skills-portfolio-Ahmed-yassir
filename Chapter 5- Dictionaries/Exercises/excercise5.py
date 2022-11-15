pets= []
pet = {
    'animal type': 'python',
    'name': 'Hashim',
    'owner': 'Kane',
    'weight': 41,
    'eats': 'bugs',
}
pets.append(pet)
pet = {
    'animal type': 'chicken',
    'name': 'rose',
    'owner': 'mark',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'jake',
    'owner': 'Ali',
    'weight': 33,
    'eats': 'shoes',
}
pets.append(pet)
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))