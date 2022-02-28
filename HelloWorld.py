"""
This is other comment
"""
#This is number
number = 3
print(number)
z = float(3)
print(z)
#This is string
content = "Hello, World!"
print(content)

print("Multi asign different content")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("Multi asign same content")
a = b = c = "Orange"
print(a)
print(b)
print(c)

print("Global function")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


print("if")
a = 33
b = 200
if b > a:
  print("b is greater than a")

print("While")
i = 1
while i < 6:
  print(i)
  i += 1

print("Foreach content:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("Function with arguments:")
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")