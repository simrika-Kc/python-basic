# # a='hello234'
# # print(a,type(a))
#
# # #this triple kot will print exactly same we wrote in it
# # #a='''hello babe
# # #my name is simrika kc'''
# # #print(a)
#
# # # Strings are immutable objects
# # string1 = "Hello"
# # string1 += " World"  # Creates a new string by concatenation
# # print(string1)  # Output: "Hello World"
#
#
# #iteration means Each character in the string is treated as an individual element and can be accessed one at a time.
# #w="welcome to wstube cube"
# #t=len(w)
# #for i in range(t):
#  #   print(w[i])
#
# #python string function
# w="welcome123"
# print(w.upper())
# print(w.lower())
# print(w.title())
# print(w.capitalize())
# print(w.find('u',5))  #starting from index 2
# print(w.index('e'))
# print(w.isalnum())
# print(w.isalpha())
# print(w.isdigit())

b=66
print(chr(b)) #char will change integer to string value

number='B'
print(ord(number)) #ord will change string to integer value


#string format
name='simrika'
surname='kc'
foramt="my name is {} and my surname is {}".format(name,surname)
print(foramt)

pi = 3.14159
formatted_pi = "The value of pi is approximately {:.2f}".format(pi)
print(formatted_pi)