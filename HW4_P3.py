# Part 1 : Using nested for loops print 5X5 2D list with number 1 to 25
x = []
count = 1
for j in range(5):
    row = []
    for i in range(5):
        row.append(count)
        count += 1
    x.append(row) #row is not defined
#initial list does not look 2D so I added the "for row in x"
for row in x:
    print(row)

"""
column = 2
row = 2
x = [[0 for i in range(row)] for j in range(column)]
trial code from stack exchange : https://stackoverflow.com/questions/35437028/understanding-creating-a-2d-list-with-nested-loops

"""

# Part 2 : Replace multiples of 3 with ? character from previous 2d list

x = []
count = 1
for j in range(5):
    row = []
    for i in range(5):
        if count % 3 == 0:
            row.append("?")
        else:
            row.append(count)
        count += 1 #wrong indentation for this line so initially it printed out 1 instead of a list or anything, I've changed the indent
    x.append(row)

for row in x:
    print(row) #indentation error after 'for' statement. Added indentation on the print and it was fixed
