# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
import operator


def countBits(n):
    binary = bin(n)
    return binary.count('1')


# https://www.codewars.com/kata/square-every-digit/train/python
def square_digits(num):
    # Better
    # return int(''.join(str(int(c)**2) for c in str(num)))
    string = str(num)
    result = ''
    for c in string:
        digit = int(c)
        result += str(digit**2)
    return int(result)


# https://www.codewars.com/kata/find-the-odd-int/train/python
def find_it(seq):
    # Better
    # return reduce(operator.xor, xs)
    result = 0
    for i in seq:
        result ^= i
    return result


# https://www.codewars.com/kata/equal-sides-of-an-array/train/python
def find_even_index(arr):
    # Better
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


# https://www.codewars.com/kata/ones-and-zeros/train/python
def binary_array_to_number(arr):
    # Better
    # return int("".join(map(str, arr)), 2)
    binary = ''
    for i in arr:
        binary += str(i)
    return int(binary, 2)


# https://www.codewars.com/kata/decode-the-morse-code/train/python
def decodeMorse(morse_code):
    # Better
    # return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
    result = ''
    words = morse_code.strip().split('   ')
    for w in words:
        chars = w.split(' ')
        for c in chars:
            result += MORSE_CODE[c]
        result += ' '
    return result[:-1]


# https://www.codewars.com/kata/iq-test/train/python
def iq_test(numbers):
    # Better
    # e = [int(i) % 2 == 0 for i in numbers.split()]
    # return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
    even, odd = -1, -1
    list = [int(n) for n in numbers.split(' ')]
    for i, n in enumerate(list):
        if n % 2 == 0:
            if even != -1 and odd != -1:
                return odd + 1
            even = i
        if n % 2 == 1:
            if odd != -1 and even != -1:
                return even + 1
            odd = i
    return len(list)


# https://www.codewars.com/kata/playing-with-digits/train/python
def dig_pow(n, p):
    s = sum([int(d) ** (p + i) for i, d in enumerate(str(n))])
    return s/n if s % n == 0 else -1


# https://www.codewars.com/kata/simple-encryption-number-1-alternating-split/train/python
def decrypt(encrypted_text, n):
    # Better
    # half = len(text) // 2
    # arr = list(text)
    # for _ in range(n):
    #     arr[1::2], arr[::2] = arr[:half], arr[half:]
    # return ''.join(arr)

    # ndx = len(text) // 2
    # for i in range(n):
    #     a = text[:ndx]
    #     b = text[ndx:]
    #     text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    # return text
    if encrypted_text == None:
        return encrypted_text
    l = len(encrypted_text)
    for i in range(n):
        result = ''
        odds = encrypted_text[:l//2]
        evens = encrypted_text[l//2:]
        for odd, even in zip(odds, evens):
            result += even + odd
        if l % 2 == 1:
            result += evens[-1]
        encrypted_text = result
    return encrypted_text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2]+text[::2]
    return text


# https://www.codewars.com/kata/write-number-in-expanded-form/train/python
def expanded_form(num):
    list = []
    string = str(num)
    for i, d in enumerate(string):
        if d != '0':
            list.append(str(int(d) * 10 ** (len(string)-i)))
    return ' + '.join(list)


# https://www.codewars.com/kata/calculating-with-functions/train/python
# Better
# id_ = lambda x: x
# number = lambda x: lambda f=id_: f(x)
# zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
# plus = lambda x: lambda y: y + x
# minus = lambda x: lambda y: y - x
# times = lambda x: lambda y: y * x
# divided_by = lambda x: lambda y: y / x


def zero(): return t[0](0, t[1]) if t else 0


def one(): return t[0](1, t[1]) if t else 1


def two(): return t[0](2, t[1]) if t else 2


def three(): return t[0](3, t[1]) if t else 3


def four(): return t[0](4, t[1]) if t else 4


def five(t=None): return t[0](5, t[1]) if t else 5


def six(t=None): return t[0](6, t[1]) if t else 6


def seven(): return t[0](7, t[1]) if t else 7


def eight(): return t[0](8, t[1]) if t else 8


def nine(): return t[0](9, t[1]) if t else 9


def plus(n):
    return operator.add, n


def minus(n):
    return operator.sub, n


def times(n):
    return operator.mul, n


def divided_by(n):
    return operator.floordiv, n


# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/train/python
def namelist(names):
    str = ', '.join(d['name'] for d in names)
    str = str[::-1].replace(',', '& ', 1)
    return str[::-1]


# https://www.codewars.com/kata/dubstep/train/python
def song_decoder(song):
    list = song.split('WUB')
    return ' '.join(s for s in list if s != '')


# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
def find_missing_letter(chars):
    # Better
    # next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
    ords = [ord(c) for c in chars]
    for i in range(1, len(ords)):
        if ords[0] + i != ords[i]:
            return chr(ords[i] - 1)


# https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python
def domain_name(url):
    # Better
    # return url.split("//")[-1].split("www.")[-1].split(".")[0]
    # return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
    list = url.split('//')
    if len(list) > 1:
        url = list[1]
    else:
        url = list[0]
    url.split('/')[0]
    list = url.split('www.')
    if len(list) > 1:
        url = list[1]
    else:
        url = list[0]
    return url.split('.')[0]


# https://www.codewars.com/kata/valid-parentheses/train/python
def valid_parentheses(string):
    # Better
    # cnt = 0
    # for char in string:
    #     if char == '(': cnt += 1
    #     if char == ')': cnt -= 1
    #     if cnt < 0: return False
    # return True if cnt == 0 else False
    stack = []
    for c in string:
        if c == '(':
            stack.append(c)
        if c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    if len(stack) != 0:
        return False
    return True


# https://www.codewars.com/kata/sudoku-solution-validator/train/python
def validSolution(board):
    # Better
    # blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    # return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)
    # What the fuck???
    flags = []
    for i in range(9):
        flags.append(False)
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    value = board[3 * i + x][3 * j + y]
                    if value == 0:
                        return False
                    flags[value - 1] = True
            for k in range(9):
                if flags[k] == False:
                    return False
                flags[k] = False
    for i in range(9):
        for j in range(9):
            flags[board[i][j] - 1] = True
        for k in range(9):
            if flags[k] == False:
                return False
            flags[k] = False
    for i in range(9):
        for j in range(9):
            flags[board[j][i] - 1] = True
        for k in range(9):
            if flags[k] == False:
                return False
            flags[k] = False
    return True
