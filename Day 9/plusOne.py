# program to demonstrate the addition of 1 to a given array
def plusOne(digits):
    string = " "
    for digit in digits:
        string += str(digit)
    number = int(string)+1
    ans = []
    for digit in str(number):
        ans.append(int(digit))
    return ans 
result = plusOne([1,2,3])
print(result)