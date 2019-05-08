first = "Sasha"
last = "Grichuk"
age = 38

print(first)
print(last)

print(first + " " + last)

print("My name is %s %s. I am %d yeats old" % (first, last, age))

print("String is %d symbols length long." % len(first))

xlist = list()
xlist.append(first)
xlist.append(last)

print(xlist)
counter = 1
for line in xlist:
    line_length = len(line)+1
    for i in range(line_length):
        print(line[0:i])






