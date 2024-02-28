# Part 1: create a variable that list out 0 to 50
create_list = list(range(0,51))
print(create_list)

# Part 2: a function that takes in a list and give square of each number in list
"""

lis = [2,3,4]
square (lis) #square is not defined in this 
>>>[4,9,16]

"""
def square_list(input):
    squared_list = [y**2 for y in input]
    return squared_list
lis = [2,3,4]
squared_lis = square_list(lis) #instead of square_list(input), write square_list(lis) because that's the name of the new list
print(squared_lis)

# Part 3 : Combine listA and listB then return new list containing only odd integers from both lists in sorted order
"""
def odd_list(listA,listB):
    listC = listA + listB
    def odd_number(listC):
        for num in listC:
            if (num % 2 != 0):
                return odd_number
#result return as none

"""

def odd_list(listA,listB):
    listC = listA + listB
    odd_numbers = []
    for num in listC:
        if (num % 2 != 0):
            odd_numbers.append(num)
    return odd_numbers

listA = list(range(1,11))
listB = list(range(20,31))

result = odd_list(listA,listB)
print(result)
            
    