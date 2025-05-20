from string import punctuation
from random import randrange, shuffle, randint
from math import factorial

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b

def is_multiple(n, m):
    return True if m != 0 and n%m == 0 else False

def is_even(k):
    even_nums = {'0','2','4','6','8'}
    return True if str(k)[-1] in even_nums  else False

def minmax(data):
    if len(data) > 0:
        min = data[0]
        max = min
        for num in data:
            if num < min:
                min = num
            elif num > max:
                max = num
        return min,max
    else:
        return

def sum_sqrs(n):
    if n >= 0:
        sum = 0
        for i in range(1,n):
            sum += i*i
        return sum

def com_sum_sqrs(n):
    if n >= 0:
        return sum(i*i for i in range(1,n))

def sum_odd_sqrs(n):
    sum = 0
    for i in range(1,n,2):
        sum += i*i
    return sum

def com_sum_odd_sqrs(n):
    return sum(i*i for i in range(1,n,2))

def check(data: str = 'hello') -> bool:
    n = len(data)
    for j in range(n):
        k = j - n
        if data[j] != data[k]:
            return False
    return True

def special_list():
    return [i for i in range(8,-9,-2)]

def binary_nums_list(n,m):
    return [1<<i for i in range(n,m)]

def my_choice_function(seq):
    return seq[randrange(len(seq))]

def reverse_intlist(int_list):
    for i in range(len(int_list)//2):
        int_list[i], int_list[-i-1] = int_list[-i-1], int_list[i]
    return int_list

def is_there_odd_prod(seq):
    odd_numbers = {i for i in seq if not is_even(i)}
    return True if len(odd_numbers) >=2 else False

def are_different(seq):
    return len(seq) != len(set(seq))

def scale(data, factor):
    for val in data:
        val *= factor
    return data

def binary_nums_list2(n,m):
    return[i*(i+1) for i in range(n,m)]
# --- This is my aproach ---
# def fun(n,m):
#     l=[n]
#     for i in range(n+1,m):
#         l.append(n+(2*i))
#         n=n+(2*i)
#     return l

def alphabet():
    return[chr(i) for i in range(97,123)]

def my_own_shuffle(data):
    n=len(data)
    for i in range(n):
        ri = randint(0,n-1)
        data[i], data[ri] = data[ri], data[i]
    return

def reverse_lines():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    for line in range(len(lines)-1,-1,-1):
        print(lines[line])

def dot_product(a,b):
    return [a[i]*b[i] for i in range(len(a))]

# ---- This is the book aproach. ----
# def array_product(a: List[int], b: List[int]) -> List[int]:
#     return [i * j for i, j in zip(a, b)]

def index_out(seq):
    try:
        seq[len(seq)]
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")

def count_vowels(line):
    num_vow=0
    vowels={'a','e','i','o','u'}
    for letter in line:
        if letter.lower() in vowels:
            num_vow+=1
    return num_vow

# ---- This is the book aproach. ----
# def get_vowels(data: str) -> int:
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return len([i for i in data.lower() if i in vowels])

def remove_punctuation(sentence):
    new_sen = [
        letter for letter in sentence
        if ord('a') <= ord(letter.lower()) <= ord('z') or letter == ' '
        ]
    return "".join(new_sen)

def can_use_informula():
    a,b,c = input("Introduce your numbers like 'a,b,c: '").split(",")

    operators = '+-*/'
    for op in operators:
        if eval(f'{a}{op}{b}') == int(c):
            return True
    for op in operators:
        if int(a) == eval(f'{b}{op}{c}'):
            return True
    return False

def factors(n): # generator that computes factors
    k=1
    nums=[]
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            nums.append(k)
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k

    for i in range(len(nums)-1,-1,-1):
        yield n//nums[i]

def norm(v:list, p:int):
    eu_norm=0
    for num in v:
        eu_norm += num**p
    return eu_norm**(1/p)

def possible_out(chars:list):
    result = []
    # fac=1
    # for i in range(1,len(chars)+1):
    #     fac *= i
    p1=len(chars)-1
    p2=p1-1
    for i in range(factorial(len(chars))):
        if p2 >= 0:
            chars[p2], chars[p1] = chars[p1], chars[p2]
            result.append("".join(chars))
            p2 -= 1
        else:
            p2=p1-1
            chars[p2], chars[p1] = chars[p1], chars[p2]
            result.append("".join(chars))
            p2 -= 1
    return result

def divided_by_two(num: int):
    times=0
    while num >= 2:
        num/=2
        times+=1
    return times

def make_change(payment: int, charge: int):
    diff=payment-charge
    change = [1000,500,200,100,50,20,10,5,2,1,]
    result = []
    if diff > 0:
        for den in change:
            if diff//den >= 1:
                result.append((str(den), diff//den))
                diff -= (diff//den)*den
    return result

# This is my first attempt about making a basic calculator
# The aproach is poor and the code a little unclear but functional -LMVA ₍^. .^₎⟆-
def basic_calculator(inp):
    chars=[]
    last_op='+'
    char_l=[]
    i=0
    while i < len(inp):
        if ord('0') <= ord(inp[i]) <= ord('9') or inp[i]=='.':
            char_l.append(inp[i])
        elif inp[i] == '(':
            current_pos=i+1
            while inp[i] != ')': i+=1
            if last_op == '+' and char_l:
                chars.append(float("".join(char_l)) * basic_calculator(inp[current_pos:i]))
                char_l=[]
            elif last_op == '-' and char_l:
                chars.append(-(float("".join(char_l)) * basic_calculator(inp[current_pos:i])))
                char_l=[]
            elif last_op == '+':
                chars.append(basic_calculator(inp[current_pos:i]))
            elif last_op == '-':
                chars.append(-basic_calculator(inp[current_pos:i]))             
        elif inp[i] == '+' or inp[i] == '-':
            if last_op == '+' and char_l:
                chars.append(float("".join(char_l)))
                char_l=[]
            elif last_op == '-' and char_l:
                chars.append(-float("".join(char_l)))
                char_l=[]
            last_op=inp[i]
        elif inp[i] != ')':
            if last_op == '+' and char_l:
                chars.append(float("".join(char_l)))
                char_l=[]
            elif last_op == '-' and char_l:
                chars.append(-float("".join(char_l)))
                char_l=[]
            last_op='+'
            chars.append(inp[i])
        i+=1
    if last_op == '+' and char_l:
        chars.append(float("".join(char_l)))
    elif last_op == '-' and char_l:
        chars.append(-float("".join(char_l)))
    only_nums=[]
    i=0
    while i < len(chars):
        if type(chars[i]) == float:
            only_nums.append(chars[i])
            i+=1
        else:
            last_num=only_nums[-1]
            only_nums.pop()
            while chars[i] == '*' or chars[i] == '/':
                if chars[i] == '*':
                    last_num*=chars[i+1]
                else:
                    last_num/=chars[i+1]
                if i<len(chars)-2:
                    i+=2
                else:
                    i=len(chars)
                    break
            only_nums.append(last_num)
    return sum(only_nums)

# This is the first improvement by gemini, it made the code clearer and it has better 
# logic implementations but it isn't capable to solve cases like "(1-2)3" -LMVA ₍^. .^₎⟆-
def basic_calculator_v2(inp):
    def evaluate(expression):
        values = []
        operators = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                num_str = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                values.append(float(num_str))
                i -= 1
            elif expression[i] in ['+', '-']:
                while operators and operators[-1] in ['+', '-']:
                    op = operators.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(apply_op(val1, val2, op))
                operators.append(expression[i])
            elif expression[i] in ['*', '/']:
                while operators and operators[-1] in ['*', '/']:
                    op = operators.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(apply_op(val1, val2, op))
                operators.append(expression[i])
            elif expression[i] == '(':
                balance = 1
                start = i + 1
                while balance > 0:
                    i += 1
                    if i >= len(expression):
                        raise ValueError("Paréntesis desbalanceados")
                    if expression[i] == '(':
                        balance += 1
                    elif expression[i] == ')':
                        balance -= 1
                values.append(evaluate(expression[start:i]))
            i += 1

        while operators:
            op = operators.pop()
            val2 = values.pop()
            val1 = values.pop()
            values.append(apply_op(val1, val2, op))

        return values[0]

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("División por cero")
            return a / b
        return 0

    cleaned_inp = "".join(inp.split())
    return evaluate(cleaned_inp)

# The next function was made by the improvements of gemini and my own corrections
# gemini wasn't capable to solve cases like "(2)2" so I changed it -LMVA ₍^. .^₎⟆-
def basic_calculator_v5(inp):
    def evaluate(expression):
        values = []
        operators = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isdigit() or char == '.':
                num_str = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                values.append(float(num_str))
                i -= 1 
            elif char in ['+', '-']:
                if not values or expression[i-1] == '(':
                    values.append(0.0)
                while operators and operators[-1] in ['+', '-']:
                    op = operators.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(apply_op(val1, val2, op))
                operators.append(char)
            elif char in ['*', '/']:
                while operators and operators[-1] in ['*', '/']:
                    op = operators.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(apply_op(val1, val2, op))
                operators.append(char)
            elif char == '(':
                if i > 0 and (expression[i-1].isdigit()):
                    operators.append('*')
                balance = 1
                start = i + 1
                while balance > 0:
                    i += 1
                    if i >= len(expression):
                        raise ValueError("Paréntesis desbalanceados")
                    if expression[i] == '(':
                        balance += 1
                    elif expression[i] == ')':
                        balance -= 1
                values.append(evaluate(expression[start:i]))
                i -= 1 # I implemented  this line to return the index where we have a ")" char
            elif char == ')':
                # I added this block of code to handle implicit multiplication expressions like "(1+2)2"
                if i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '('):
                    operators.append('*')
            i += 1

        while operators:
            op = operators.pop()
            val2 = values.pop()
            val1 = values.pop()
            values.append(apply_op(val1, val2, op))

        return values[0]

    def apply_op(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("División por cero")
            return a / b
        return 0

    cleaned_inp = "".join(inp.split())
    return evaluate(cleaned_inp)

def birthday_paradox(n):
    def calculate_rand_monthsday(n):
        if (n%2 != 0 and n < 8) or (n%2 == 0 and n > 7):
            return randint(1,31)
        elif n == 2:
            return randint(1,29)        
        else:
            return randint(1,30)

    birthday_dates = set()

    for peaople in range(n):
        month = randint(1,12)
        day = calculate_rand_monthsday(month)

        if (month, day) in birthday_dates:
            return True
        else:
            birthday_dates.add((month, day))
            
    return False

def word_counter(line:str):
    words={}
    word=[]

    for char in line:
        char=char.lower()

        if 97 <= ord(char) <= 122:
            word.append(char)            
        elif char == ' ' and word:
            word = "".join(word)
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
            word = []

    return words






    


