# In linear search the list will not be sorted
def linearsearch(list,value):
    position = 0
    while (position<=len(list)):
        if list[position] == value:
            return position
        position += 1
    
    return -1
list = [12,43,23,10]
value = 5
print("Returning the position of the value :",linearsearch(list,value))




