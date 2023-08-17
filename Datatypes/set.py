
#Set is immutable which is defined in curly bracket and cannot repeat elements i.e. it must have unique elements
#s={1,2,3,4,5,5,5,6}
#print(s,type(s))  #output:{1,2,3,4,5,6}

my_set = {1, 2, 3}  # Using curly braces
my_set = set([1, 2, 3])  # Using the set() constructor

my_set.add(4)  # Add a single element
my_set.update([5, 6])  # Add multiple elements from an iterable

my_set.remove(3)  # Remove an element by value (raises an error if the element is not found)
my_set.discard(3)  # Remove an element by value (no error if the element is not found)
my_set.pop()  # Remove and return an arbitrary element from the set
my_set.clear()  # Remove all elements from the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # Get the union of two sets
intersection_set = set1.intersection(set2)  # Get the intersection of two sets
difference_set = set1.difference(set2)  # Get the difference between two sets (elements in set1 but not in set2)
symmetric_difference_set = set1.symmetric_difference(set2)  # Get the symmetric difference of two sets (elements in either set, but not both)


if 1 in my_set:  # Check if an element is present in the set
    print("Element found!")


length = len(my_set)  # Get the number of elements in the set
for item in my_set:  # Iterate over the elements of the set
    print(item)
