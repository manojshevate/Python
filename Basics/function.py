# functions


# Basic function which will print Hello world to console
def say_hello():
    print "Hello World!"

say_hello()


# Function with arguments
def add(a, b):
    return a + b

print add(3, 4)


# Lets clear the local and global variable concept
v1 = 10
v2 = 11


def global_local(v1):
    global v2
    print v1, v2
    v1 = 20
    v2 = 20
    print v1,v2

global_local(v1)
print v1, v2


# function with Default arguments
def default_arguments(name="Manoj"):
    print "Hello {}!".format(name)

default_arguments()
default_arguments("India")


# Function with keyword arguments
def keyword_arguments(initial=10, *numbers, **keywords):
    count = initial
    for i in numbers:
        count += i

    for keyword in keywords:
        count += keywords[keyword]

    return count


print keyword_arguments()
print keyword_arguments(40,10,20,c=16,a=14)