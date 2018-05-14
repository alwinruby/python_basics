# 1) Given the following dictionary:
#
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
# Try to do the followings:
#
# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# Use .sort() the items in the list stored under the 'backpack' key. (keep in mind that .sort() is a function associated with a list.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key, this should result in the gold containing the value 550.

# Task 1.
inventory = {
        'gold' : 500,
        'pouch' : ['flint', 'twine', 'gemstone'],
        'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }

#Using the update function update({"key":value}) value in this case is a list of strings
inventory.update({'pocket':['seashell', 'strange berry','lint']})
print(inventory)

print("\n")

#Using the sort() function on the list of items in backpack
print("Before sort: ",inventory['backpack'])
inventory['backpack'].sort()
print("After sort: ",inventory['backpack'])

print("\n")


#Using .remove() removes an item from the list matching the value passed in.
print("Before remove: ",inventory['backpack'])
inventory['backpack'].remove('dagger')
print("After remove: ",inventory['backpack'])

print("\n")

#Adding 50 to gold in the dictionary
print("Before adding 50 to gold: ",inventory['gold'])

#You can access a value using dictionary['key']
#Once you access the value you can do anything with it.
#You can then overwrite the value of the key by
# dictionary['key'] = new value
inventory['gold'] = inventory['gold'] + 50

print("After adding 50 to gold: ",inventory['gold'])
