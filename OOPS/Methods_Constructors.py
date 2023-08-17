class MethodConstructor:
    def __init__(self, name, age):  #these are the constructor under () this
        self.name = name
        self.age = age

    def engine(self):   #method
        print("hello engine")
        print(f"my name is {self.name} {self.age}")
    def selfengine(self):
        print("hi selfengine")

# Creating an instance of the Method class
methodEngine = MethodConstructor("simrika", "kc")

# Calling the engine() and selfengine() methods
methodEngine.engine()
methodEngine.selfengine()



