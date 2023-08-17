# # #dictionary are mutable and is defined in curly bracket
# # # Creating a dictionary
# # student = {
# #     "name": "John",
# #     "age": 20,
# #     "major": "Computer Science",
# #     "university": "ABC University"
# # }
#
# # # Accessing dictionary elements
# # print(student["name"])  # Output: John
# # print(student["age"])  # Output: 20
# # print(student["major"])  # Output: Computer Science
# # print(student["university"])  # Output: ABC University
#
# # # Modifying dictionary elements
# # student["age"] = 21
# # student["major"] = "Data Science"
# # print(student["age"])  # Output: 21
# # print(student["major"])  # Output: Data Science
#
# # # Adding new elements to the dictionary
# # student["year"] = 3
# # print(student["year"])  # Output: 3
#
# # # Checking if a key exists in the dictionary
# # print("name" in student)  # Output: True
# # print("address" in student)  # Output: False
#
# # # Removing an element from the dictionary
# # del student["university"]
# # print(student)  # Output: {'name': 'John', 'age': 21, 'major': 'Data Science', 'year': 3}
#
# #get
# d={
#     "name":"simrika",
#     "surname":"kc"
#
# }
# for a in d.keys(): #only focus on key i.e. name and surname
#     print(a)
# for b in d.items(): # for key and value both
#     print(b)
# for c in d.values(): #for only value i.e simrika and kc
#     print(c)
#
# for d in d.get("name"):
#     print(d)
#
# # pop
# fruits = {'apple':'hello', 'banana':'fine', 'orange':'omma'}
# #removed_fruit = fruits.pop('apple')   #deletting
# #print(fruits)
# #print(removed_fruit)
#
# #delete
# del fruits['apple']
# print(fruits)
#
#
# #dict will create dictionary
# d = dict(hello='hi',vy='sy') #this will make dictionary
# print(d)
#
# #updatae
# d.update({'hello':"sory"})
# print(d)
#
# #adding /inserting
# d['disc']="hello"
# print(d)
#
# #clear
# d.clear()
# print(d)
#


#nested dictionary
books={'php':{'course':'science','month':'3'},
'java':{'course':'math','month':'2'},
'puthon':{'course':'social','month':'1'},
       }
print(books)
print(books['php'])