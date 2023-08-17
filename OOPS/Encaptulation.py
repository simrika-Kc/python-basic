# # class Encap:
# #     def __init__(self):
# #         self._name=""
# #
# #     def getname(self):
# #         return self._name
# #
# #     def setname(self,name):
# #         self._name=name
# #
# # object=Encap()
# # object.setname("simrika")
# # roman=object.getname()
# # print(roman)
# #
# #
#
# class Encaptulation:
#     def __init__(self):
#         self._love=""  #using underscore in the varaible means it is private not public
#
#     def getlove(self):
#         return self._love
#     def setlove(self,love):
#         self._love=love
#
# obj=Encaptulation()
# obj.setlove("love is : hello")
# hi=obj.getlove()
# print(hi)


import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="level4c"
)

