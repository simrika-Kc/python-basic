class A:
    def displayA(self):
     print("hello simrika")


class B(A):  #single inheritance
    def displayB(self):
     print("hii roman!!")


class c(B):  # multilevel inheritance
    def displayc(self):
        print("i love you!!")

class d(A,B,c):  # multilevel inheritance  but it only works after
    # removing inheritation fron above functions i mean every function
    # should me parent so we should remove A from B class and B from C class
    def displayD(self):
        print("i too love you!!")

object=d()
object.displayA()
object.displayB()
object.displayc()
object.displayD()