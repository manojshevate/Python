# Control flow

for i in [1, 2, 3, 4, 5]:
    if i < 3:
        print "Low"
    elif i == 3:
        print "Mid"
    else:
        print "High"
else:
    print "Done with for loop!"

while True:
    str = raw_input("Enter string -")
    if str == 'quit':
        break
    else:
        print "You Entered:", str


