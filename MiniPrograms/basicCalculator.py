number = 0
total = 0
for i in range(40):
    print i+1
    number = int(raw_input("> "))
    total = total + number
    print "Total so far ", total

print total
