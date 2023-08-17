# # # # #String are immutalble it means it cannot be edit but list and dictionary are mutable which can be edited like we did in java
# # # # #List is always defined in square bracket and can store any type of value eg. a=[3,4.4,'hi']
# # # #
# # # # # #list
# # # # # a=[4,5.5,'70']
# # # # # #edit of value which lie in 2 index
# # # # # a[2]=10
# # # # # print(a,type(a))
# # # #
# # # # # # Lists are mutable objects
# # # # # list1 = [1, 2, 3]
# # # # # list1.append("hi")  # Modifies the original list in-place
# # # # # print(list1)  # Output: [1, 2, 3, 4]
# # # #
# # # # l=[1,2,3,4,5,6,7]
# # # # print(l[-1::-1])  #print in bacward dirxn
# # # # print(l[1:])   #print from index 1 to all elements till last
# # # # print(l[3],l[5])  #printing only index 3 and 5 separately
# # #
# # # #clear
# # # l=["Banana","apple","guava","grapes"]
# # # print(l.clear())
# # #
# # # #remove
# # # fruits = ['apple', 'banana', 'orange']
# # # fruits.remove('banana')  #removing banana from teh list
# # # print(fruits)
# # #
# # # #pop
# # # fruits = ['apple', 'banana', 'orange']
# # # removed_fruit = fruits.pop(1)   #calling fruits wich is in index 1
# # # print(fruits)
# # # print(removed_fruit)
# # #
# # #
# # # #del
# # # fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango']
# # # del fruits[1:4]  #delete fruits fro index 1 to 4
# # # print(fruits)
# # #
# # #
# # # #count
# # # fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'apple']
# # # apple_count = fruits.count('orange')
# # # print(apple_count)
# # #
# # #
# # # #max, min
# # # l=[1,2,3,4,5,6,7,8,9]
# # # p=max(l)
# # # print(p)
# # # q=min(l)
# # # print(q)
# # #
# #
# #
# # #sort
# # l=[1,2,3,45,5,2,3,43]
# # l.sort()
# # print(l)
# #
# # numbers = [5, 2, 8, 1, 9]
# # numbers.sort()
# # print(numbers)
# #
# # #reverse sort
# numbers = [5, 2, 8, 1, 9]
# # numbers.sort(reverse=True)
# # print(numbers)
#
# numbers.reverse()
# print(numbers)


#zip
a=[2,3,4,5,6,7]
b=[3,4,5,6,7,8]
for a,b in zip(a,b):  #combining two lists in one
    print(a,b)


#converting string to list
a="hi my name is simrika"
b=a.split(";")  #to convert in a string
b=a.split()     #to covert on a list
print(b)