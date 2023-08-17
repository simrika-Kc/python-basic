# #tuples are immutable datatypes which are defined in small bracket and is faster than lists
# p=(4,3.3,'2+3j')
# print(type(p))


my_tuple = (1, 2, 3, 4, 5)
# Iterate over the tuple and access index and value
for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")
