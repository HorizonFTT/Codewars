# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def countBits(n):
    binary = bin(n)
    return binary.count('1')


# https://www.codewars.com/kata/square-every-digit/train/python
def square_digits(num):
    # return int(''.join(str(int(c)**2) for c in str(num)))
    string = str(num)
    result = ''
    for c in string:
        digit = int(c)
        result += str(digit**2)
    return int(result)


# https://www.codewars.com/kata/find-the-odd-int/train/python
def find_it(seq):
    # return reduce(operator.xor, xs)
    result = 0
    for i in seq:
        result ^= i
    return result


# https://www.codewars.com/kata/equal-sides-of-an-array/train/python
def find_even_index(arr):
    # left, right = 0, sum(arr)
    # for i, e in enumerate(arr):
    #     right -= e
    #     if left == right:
    #         return i
    #     left += e
    # return -1
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

