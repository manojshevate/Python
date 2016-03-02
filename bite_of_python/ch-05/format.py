age = 27
name = "Manoj"

print "name: {0}, Age: {1}".format(name,age)

# Numbers are optional
print "name: {}, Age: {}".format(name,age)

# Keyword based formating
print "name: {name}, Age: {age}".format(age = age,name =name)

# decimal (.) precision of 3 for float '0.333'
print '{0:.3f}'.format(1.0/3)
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print '{0:_^11}'.format('hello')


'''This is a multi-line string. This is the first line.
Basics
39
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''