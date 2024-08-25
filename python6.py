"""
#
# Part: Python Function
#
"""
def myFunction():
    i = 1
    while i <=5:
        print("Hello World ", i)
        i+=1
myFunction()
myFunction()

def myName(name):
    print("My name is ", name)
myName("BOOM")
myName("Fun")


def myFullName(first_name = "Unkown", Last_name = "Forger"):
    print("My name is " + first_name + " " + Last_name)
myFullName("Boom")
myFullName("Boom", "Forger")
myFullName("Yor", "Forger")
myFullName(Last_name = "forger", first_name="Boom")

def myFruit(fruits):
    for fruit in fruits:
        print(fruits)
fruits = ["Apple", "Banana", "Coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))