def threeLargestElement(arr):
    first_arr = arr[0]
    second_arr = arr[1]
    third_arr = arr[2]
    for num in arr:
        if num > first_arr:
            third_arr = second_arr
            second_arr = first_arr
            first_arr = num
        elif num > second_arr:
            third_arr = second_arr
            second_arr = num
        elif num > third_arr:
            third_arr = num
    return [first_arr,second_arr,third_arr]
Result = threeLargestElement([10, 4, 3, 65, 9, 21])
print(Result)