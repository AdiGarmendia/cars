#Create an empty set named showroom.
showroom = set()

#Add four of your favorite car model names to the set.
showroom.add("GT40")
showroom.add("GTO Judge")
showroom.add("NSX")
showroom.add("GTR")

# Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("GT40")

# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)
# Using update(), add two more car models to your showroom with another set.
showroom.update(["911", "Thunderbird"])
print(showroom)
# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("911")
print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars 
# has approached you about buying the entire inventory. In the new set, add some different cars, 
# but also add a few that are the same as in the showroom set.
junkyard = {"Sierra", "GTR", "Bug", "NSX"}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print(junkyard.intersection(showroom))

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into 
# your showroom.
new_showroom = showroom.union(junkyard)
print(new_showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not
#  want in your showroom.
new_showroom.discard("Bug")
print(new_showroom)