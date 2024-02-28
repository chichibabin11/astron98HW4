# takes list and returns copy of list with duplicate values removed
def lis(input):
    new_list = list(set(input))
    return new_list

x = [1,2,2,3,4,5,5,6]
print(lis(x))