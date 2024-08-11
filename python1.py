"""
v = s/t
v= ความเร็ว (m/s)
s = ระยะทาง (m)
t = เวลา(s)
"""
print("Hello World!!!")


x = 5           # integer
y = "Hey Brus"   # String
print(x,y)

x = str(3)
y = int(5)
z = float(7)
print (type(x), type(y), type(z))


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAY = "Jhon"
MY_VAR = "Jhon"
# 2my_var = "John"
# my-var = "John"
# my var = "John"

# Camel Case
myVariableName = "Jhon"
# Pascal Case
MyVariableName = "Jhon"
# Snake Case
my_variable_name = "Jhon"

"""
#
# Part: Pyphon String
#
"""

y = """
1 Hey Brus
2 Hey Brus
3 Hey Brus
"""
print(y)


x = "Hey Brus"
print(x[2])
print(len(x))
print("Hey" in x)
print("What'sup" not in x)
print(x.upper())
print(x.lower())

print(x.replace("Brus", "Sis"))
print(x.split(" "))

a = "Apple"
b = "Company"
print(a + " " + b)

print = 20
word = f"Price: {'price'=:.2f}"
print(word)