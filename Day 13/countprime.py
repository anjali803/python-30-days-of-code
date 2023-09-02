def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

def count_prime(n):
    count = 0
    for num in range(2,n):
        if is_prime(num):
            count += 1
    return count

input = 10
output = count_prime(input)
print(output)

