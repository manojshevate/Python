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
        # you can use continue instead of break to skip the current excecution
        break
    else:
        print "You Entered:", str


