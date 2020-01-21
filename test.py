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

# https://www.codewars.com/kata/best-travel/train/python


def choose_best_sum(t, k, ls):
    # fuck
    from itertools import combinations
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)


# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
def pig_it(text):
    return ' '.join((w + w[0] + 'ay')[1:] if w.isalpha() else w for w in text.split())


# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
def zeros(n):
    x = n//5
    return x+zeros(x) if x else 0


# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
def rot13(message):
    return ''.join(chr(ord('a')+(ord(c)-ord('a')+13) % 26) if c.islower() else chr(ord('A')+(ord(c)-ord('A')+13) % 26) if c.isupper() else c for c in message)


# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
def primeFactors(n):
    result = ''
    i = 2
    while n > 1:
        t = 0
        while n % i == 0:
            n //= i
            t += 1
        if t == 1:
            result += f'({i})'
        elif t > 1:
            result += f'({i}**{t})'
        t = 0
        i += 1
    return result


# # https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python
# def encode_rail_fence_cipher(string, n):
#     size = 2 * (n - 1)
#     list = []
#     for i in range(len(string) // size):
#         list.append(string[i*size:size*(i+1)])
#     list.append(string[-(len(string) % size):])
#     encoded = ''
#     for i in range(n):
#         for s in list:
#             if i < len(s):
#                 encoded += s[i]
#                 if i > 0 and i < size//2:
#                     encoded += s[-i]

#     return encoded


# def decode_rail_fence_cipher(string, n):
#     size = 2 * (n - 1)
#     decoded = ''
#     for i in range(len(string) // size + 1):
#         for j in range(size):
#             if j < size // 2 and i * size + j < len(string):
#                 decoded += string[i * size + j]
#             else:
#                 if i * size + size - j - 1 + j < len(string):
#                     decoded += string[i * size + size - j - 1]
#     return decoded


# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
def top_3_words(text):
    text = text.lower()
    times = {}
    n = len(text)
    i = 0
    while i != n:
        w = ''
        while i != n and not text[i].isalpha() and text[i] != '\'':
            i += 1
        flag = False
        while i != n and (text[i].isalpha() or text[i] == '\''):
            if text[i].isalpha():
                flag = True
            w += text[i]
            i += 1
        if not flag:
            continue
        if times.get(w) is None:
            times[w] = 0
        else:
            times[w] += 1
    return [e[0] for e in sorted(times.items(), key=lambda x: x[1], reverse=True)[:3]]


# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.lenOfKey = len(key)
        self.lenOfAlphabet = len(alphabet)

    def encode(self, text):
        result = ''
        for i in range(len(text)):
            shift = self.alphabet.find(self.key[i % self.lenOfKey])
            index = self.alphabet.find(text[i])
            if index != -1:
                result += self.alphabet[(index+shift) % self.lenOfAlphabet]
            else:
                result += text[i]
        return result

    def decode(self, text):
        result = ''
        for i in range(len(text)):
            shift = self.alphabet.find(self.key[i % self.lenOfKey])
            index = self.alphabet.find(text[i])
            if index != -1:
                result += self.alphabet[(index-shift) % self.lenOfAlphabet]
            else:
                result += text[i]
        return result


# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


def prime_list(n):
    result = []
    for i in primes():
        if i <= n:
            result.append(i)
        else:
            return result


def sum_for_list(lst):
    result = []
    l = prime_list(max([abs(i) for i in lst]))
    for p in l:
        s = 0
        flag = False
        for i in lst:
            if i % p == 0:
                s += i
                flag = True
        if flag:
            result.append([p, s])
    return result
