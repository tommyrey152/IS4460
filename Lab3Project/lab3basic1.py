# This is my first comment for lab3

#____________________________________________________________________________________________________________

#Literals 

c = "Captain "
s = "Spock"
print(c + s)

sink = 3.4 
shower = 4.2
print(sink * shower)



print("")
print("")
#____________________________________________________________________________________________________________

# String and Variable + f String

meal = "dessert"
cookie = "snickerdoodle"
eaten = 12

print(f"The best {meal} is the {cookie}")
print(f"Today I have eaten {eaten}")


print("")
print("")
#____________________________________________________________________________________________________________

#Converting between types and substrings

pi = 3.14159265358979323846
food = "pie"

print("I really love ", food, "but people often get confused and think I mean", (str(pi)[0:4]), "but I don't like math very much")



print("")
print("")
#____________________________________________________________________________________________________________
# A, B  function

AA = 5
bb = 3
print(bb)
print(AA)
print(bb*AA)

print("")
print("")
#____________________________________________________________________________________________________________
# Say Hello Function

print("Hello World!")

print("")
print("")
#____________________________________________________________________________________________________________
# Boolean

h = True
l = False

x = 5
y = 2

boolean = x < y
print(boolean)

print("")
print("")
#____________________________________________________________________________________________________________

def addTwoNumbers(a,b):
  print(a+b)
  print(b)
  print(a)
  return
addTwoNumbers(4,1)
print(addTwoNumbers(10,10))
print(addTwoNumbers(a=2,b=10))


print("")
print("")
#____________________________________________________________________________________________________________

name = "saul"

def sayHello(name):
  name = "walter"
  print(name)


print(name)
sayHello(name)


print("")
print("")
#____________________________________________________________________________________________________________
#Precedence

g = 10
g = 101
g = g + g

print(g)
