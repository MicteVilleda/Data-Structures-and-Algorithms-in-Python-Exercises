from abc import ABCMeta, abstractmethod
from time import localtime, monotonic
from random import randint

""" R-2.1 Three life-critical software applications could be bank apps, text messages apps and search engines apps.
    R-2.2 Some software apps like Amazon or AliExpress could have a lot o losses if their software apps don't achieve adaptability.
    R-2.3 I'll describe the text area component where I think it could encapsulate methods like GetText or SetAlign. """

# R-2.4


class Flower:
    def __init__(self, name='Sunflower', num_petals=23, price=3.0) -> None:
        self._name = name
        self._num_petals = num_petals
        self._price = price
        return

    def _get_name(self) -> str:
        return self._name

    def get_num_petals(self) -> int:
        return self._num_petals

    def get_price(self) -> float:
        return self._price

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def set_num_petals(self, new_num: int) -> None:
        self._num = new_num

    def set_price(self, new_price: float) -> None:
        self._price = new_price


# R-2.5, R-2.6 and R-2.7
class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0) -> None:
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def _set_balance(self, amount):
        self._balance += amount

    def get_customer(self) -> str:
        return self._customer

    def get_bank(self) -> str:
        return self._bank

    def get_account(self) -> str:
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price) -> bool:
        if not isinstance(price, (int, float)):
            raise TypeError('You must enter a number value, not a string.')
        else:
            if self._balance + price > self._limit:
                return False
            else:
                self._balance += price
                return True

    def make_payment(self, amount) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError('You must enter a number value, not a string.')
        if amount < 0:
            raise ValueError('You cannot enter negative values.')
        else:
            self._set_balance(-amount)


# R-2.8
# wallet = []

# wallet.append(CreditCard('Leyla Villeda','BBVA','4123 6245 8213 6287', 2500))
# wallet.append(CreditCard('Leyla Villeda','HSBC','3345 8406 9137 5467', 3500))
# wallet.append(CreditCard('Leyla Villeda','NU','9435 9137 5684 6385', 5000))

# for val in range(1, 17):
#     val *= 100
#     if not wallet[0].charge(val):
#         print(f'This is the first card that go over its limit: {wallet[0].get_bank()}')
#         break
#     if not wallet[1].charge(val*2):
#         print(f'This is the first card that go over its limit: {wallet[1].get_bank()}')
#         break
#     if not wallet[2].charge(val*3):
#         print(f'This is the first card that go over its limit: {wallet[2].get_bank()}')
#         break


# R-2.9, R-2.10, R-2.12, R-2.13, R-2.14, R-2.24
class Vector:
    def __init__(self, n) -> None:
        if isinstance(n, int):
            self._coords = [0]*n
        elif hasattr(n, '__getitem__'):
            self._coords = []
            for i in range(len(n)):
                if isinstance(n[i], int):
                    self._coords.append(n[i])
                else:
                    self._coords.append(0)

    def __len__(self) -> int:
        return len(self._coords)

    def __getitem__(self, index):
        return self._coords[index]

    def __setitem__(self, index, val) -> None:
        self._coords[index] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')

        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = self[i] + other[i]

        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        if not isinstance(other, Vector):
            raise TypeError('Argument must be another Vector')

        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = self[i] - other[i]

        return result

    def __mul__(self, multiplier):
        if isinstance(multiplier, Vector):
            result = 0

            for i in range(len(self)):
                product = self[i] * multiplier[i]
                result += product

            return result
        elif isinstance(multiplier, (int, float)):
            result = Vector(len(self))

            for i in range(len(self)):
                result[i] = self[i] * multiplier

            return result
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: '{type(multiplier).__name__}' and '{type(self).__name__}'")

    def __rmul__(self, multiplier):
        return self.__mul__(multiplier)

    def __neg__(self):
        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = -self[i]

        return result

    def __eq__(self, other) -> bool:
        return self._coords == other._coords

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        return f'<{str(self._coords)[1:-1]}>'


""" R-2.11 Due the polymorphism, our vector class can take a sequence wich has a length
    and index accesses to have the addition behavior as if the 2 values were vectors.
    However, if we want to use the syntax v=[1,2,3,4]+u we need to implement the reflective
    dunder method __radd__.

    R-2.16 First, in our arithmetic formula, we calculate a range value substracting the
    stop argument with the start argument, then we consider the influence of the step
    intervalue adding the substraction between the step argument and the constant 1, to
    finish we divide that with the step argument, wich we can interpretate that division
    as how many times the step intervalue fits in our range value.
    We use the max function to avoid negative numbers as a result."""


# R-2.18
class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer


class FibonacciProg(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._current, self._prev = self._current + self._prev, self._current

# prog = FibonacciProg(2,2)
# for i in range(8):
#     print(next(prog))


""" R-2.20 First, trying to track a bug in a deep heritance tree could be harder, furthermore, each
    super() call has a high cost becase we have a large super() calls chain"""


# R-2.22, R-2.23
class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self):
        return len(self)

    @abstractmethod
    def __getitem__(self, j):
        for i in range(len(self)):
            if self[i] == j:
                return self[i]

    def __eq__(self, val):
        for i in range(len(self)):
            if val != self[i]:
                return False
        return True

    def __lt__(self, sq):
        return True if len(self) < len(sq) else False

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('Value not in sequence')

    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
            return k


# R-2.26
class ReversedSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = 0

    def __next__(self):
        self._k -= 1
        if self._k > -(len(self._seq)+1):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


# R-2.27
class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('Step cannot be 0')

        if not stop:
            start, stop = 0, start

        self._lenght = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._stop = stop
        self._step = step

    def __len__(self) -> int:
        return self._lenght

    def __getitem__(self, index) -> int:
        if index < 0:
            index += self._lenght

        if not 0 <= index < self._lenght:
            raise IndexError('Index out of range')

        return self._start + index * self._step

    def __contains__(self, value):
        if self._start <= value < self._stop:
            return True if (value - self._start) % self._step == 0 else False
        else:
            return False


# R-2.28, R-2.29, R-2.30
class PredatoryCreditClass(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr, balance=0) -> None:
        super().__init__(customer, bank, acnt, limit, balance)
        self._apr = apr
        self._monthly_charges = 0
        self._monthly_payment = balance * 0.03
        self._collection_date = 15
        self._current_month = localtime().tm_mon if localtime(
        ).tm_mday < 15 else localtime().tm_mon + 1
        self._running = True

    def charge(self, price):
        succes = super.charge(price)
        if not succes:
            self._set_balance(5)

        if self._monthly_charges > 10:
            self._set_balance(1)

        self._monthly_charges += 1
        return succes

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

    def check_date(self):
        if localtime().tm_mday > 15 and localtime().tm_mon == self._current_month and self._monthly_charges > 0:
            self._set_balance(50)

    def charge_monthly_payment(self, amount):
        self._monthly_charges -= amount


# R-2.31
class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(''.join(f'{str(next(self))} ' for i in range(n)))

class DifferenceProg(Progression):
    def __init__(self, first = 2, second= 200):
        super().__init__(first)
        self._prev = first + second

    def _advance(self):
        self._current, self._prev = abs(self._prev - self._current), self._current

class RootProg(Progression):
    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        self._current = pow(self._current, 0.5)


# R-2.33
def derive_monomial(monomial, variable):
    constants = [1]
    has_variable = False
    exponent = 1
    result = ''

    i = 0
    num_str = ''
    while i < len(monomial):
        if monomial[i] == variable:
            has_variable = True
            if num_str:
                constants.append(int(num_str))
                num_str = ''
            i += len(variable) + 1
            break

        elif monomial[i] == '^':
            if num_str:
                constants.append(int(num_str))
                num_str = ''
            i += 1
            break

        elif 48 <= ord(monomial[i]) <= 57 or monomial[i] == '.':
            num_str += monomial[i]

        else:
            if num_str:
                constants.append(int(num_str))
                num_str = ''
            constants.append(monomial[i])

        i += 1

    while i < len(monomial):
        if 48 <= ord(monomial[i]) <= 57:
            num_str += monomial[i]
        elif monomial[i] == variable:
            has_variable = True
            num_str += monomial[i]
        i += 1

    if num_str:
        if variable in num_str:
            exponent = num_str
        else:
            exponent = int(num_str)

    if not has_variable:
        return '0'

    if exponent == 1:
        if len(constants) > 1:
            return ''.join(str(constants[i]) for i in range(1, len(constants)))
        else:
            return constants[0]
    else:
        if isinstance(exponent, int):
            constants[0] *= exponent
            exponent -= 1
            if len(constants) > 1:
                if isinstance(constants[1], int):
                    constants[1] *= constants[0]
                    constant = ''.join(str(constants[i])
                                       for i in range(1, len(constants)))
                    return f'{constant}{variable}^{exponent}' if exponent > 1 else f'{constant}{variable}'
                else:
                    constant = ''.join(str(constants[i])
                                       for i in range(len(constants)))
                    return f'{constant}{variable}^{exponent}' if exponent > 1 else f'{constant}{variable}'
            else:
                return f'{constants[0]}{variable}^{exponent}' if exponent > 1 else f'{constants[0]}{variable}'

def derive_polynomial(polynomial):
    polynomial = polynomial.replace(" ","")

    monomial_str = ''
    variable = ''

    j = 2
    while polynomial[j] != ')':
        variable += polynomial[j]
        j += 1
    j += 2

    result = [f'f\'({variable})=']

    while j <= len(polynomial):
        if j == len(polynomial):
            last_monomial = derive_monomial(monomial_str, variable)

            if last_monomial == '0':
                result.pop()
            else:
                result.append(last_monomial)
                monomial_str = ''

        elif polynomial[j] == '+' or polynomial[j] == '-':
            if monomial_str:
                last_monomial = derive_monomial(monomial_str, variable)
                if last_monomial == '0':
                    result.pop()
                else:
                    result.append(last_monomial)
                    monomial_str = ''
            result.append(polynomial[j])
        else:
            monomial_str += polynomial[j]

        j += 1

    return ''.join(result)

# print(derive_polynomial('P(x)=3x^2-5x+7'))
# print(derive_polynomial('Q(y)=y^4+2y^3-y^2+8y-1'))
# print(derive_polynomial('R(z)=1/2z^3-4'))
# print(derive_polynomial('S(a)=-6a^5+10a^4-2a^3+7a^2-3a+9'))
# print(derive_polynomial('T(b)=√3b^2+πb'))


# R-2.34
def barchart(per):
    if isinstance(per, (int, float)):
        if abs(per) <= 100:
            per = abs(per)
        else:
            raise ValueError('The percentage value must be in a range of 0 to 100')
    else:
        raise TypeError(f'\'{type(per).__name__}\' object cannot be interpreted as an number')

    out = []
    for i in range(0,101):
        if i < per or per == 100:
            out.append('■')
        elif 0 < i - per < 1:
            out.append('□')
        elif i % 20 == 0:
            out.append('|')
        else:
            out.append(' ')
    return ''.join(out)

def show_frequencies(text_file):
    if isinstance(text_file, str):
        try:
            with open(text_file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{text_file}' was not found.")
        except PermissionError:
            raise PermissionError(f"You don't have permissions to access the file: '{text_file}'")            
        except Exception as e:
            raise Exception(f"An unexpected error occured while opening the file: {e}")
            
    else:
        raise TypeError(f'\'{type(text_file).__name__}\' object cannot be interpreted as a file name')
    
    greater_freq = 0
    alph_chars = {}

    for i in text:
        i = i.lower()
        if i.isalpha():
            if i in alph_chars:
                alph_chars[i] += 1
            else:
                alph_chars[i] = 1

            if alph_chars[i] > greater_freq:
                greater_freq = alph_chars[i]

    if not alph_chars:
        print("The file doesn't have any alphabet character")
        return

    print('Bar chart plot ₍^. .^₎⟆')
    print('   ____________________________________________________________________________________________________')
    for char in alph_chars:
        percentage = (alph_chars[char] * 100) / greater_freq
        print(f'{char}: {barchart(percentage)}')

    interval = greater_freq/5
    gauge = 0
    rule = ['   ',]
    i=0
    while i <= 100:
        if i % 20 == 0:
            rule.append('|')
            rule.append(str(int(gauge)))
            i += 1 + len(str(int(gauge)))
            gauge += interval
        else:
            rule.append(' ')
            i += 1
    print('   |___________________|___________________|___________________|___________________|___________________|')
    print(''.join(rule))

# show_frequencies('tale.txt')
# show_frequencies('tale2.txt')


# R-2.35
class User:
    def __init__(self):
        self._packages = 0

    def check_packages(self):
        if self._packages:
            return self._packages
        else:
            return False

    def create_package(self):
        self._packages += 1
        print("Package created")

    def send_packages(self, num_pack=1):
        self._packages -= num_pack
        print("Package sent")

    def receive_packages(self, num_pack=1):
        self._packages += num_pack
        print("Package received")

    def read_packages(self, num_pack=1):
        self._packages -= num_pack
        print("Package read")

def internet_app(transmitter: User, receiver: User):
    cooldown = 4
    current_time = monotonic()
    last_time_pos = current_time

    while monotonic() - current_time < 15:
        if monotonic() - last_time_pos > cooldown:
            transmitter.create_package()
            last_time_pos = monotonic()

        if transmitter.check_packages():
            packages = transmitter.check_packages()
            transmitter.send_packages(packages)
            receiver.receive_packages(packages)

        if receiver.check_packages():
            receiver.read_packages()

# alice = User()
# bob = User()

# internet_app(alice, bob)


# R-2.36
class Bear:
    def __init__(self, position):
        self._pos = position

    def __str__(self):
        return "ฅ՞•ﻌ•՞ฅ"

    def __repr__(self):
        return "ฅ՞•ﻌ•՞ฅ"

    def move(self, step):
        self._pos += step
        return step

    def get_pos(self):
        return self._pos

class Fish:
    def __init__(self, position):
        self._pos = position
        self._alive = True

    def __str__(self):
        return ">(  °)"

    def __repr__(self):
        return ">(  °)"

    def move(self, step):
        self._pos += step
        return step

    def get_pos(self):
        return self._pos
    
    def die(self):
        self._alive = False

    def is_alive(self):
        return self._alive

def ecosystem(river_length: int):
    river = [None] * river_length
    number_of_animals = 0
    num_of_fishes = 0
    num_of_bears = 0
    animals = set()
    # run = True

    for slot in range(river_length):
        possible_option = randint(1, 5)

        if possible_option == 1:
            river[slot] = Bear(slot)
            animals.add(river[slot])
            number_of_animals += 1
            num_of_bears += 1

        elif possible_option == 2:
            river[slot] = Fish(slot)
            animals.add(river[slot])
            number_of_animals += 1
            num_of_fishes += 1

    print(f'{river}\nNumber of animals {number_of_animals}\n')

    while  number_of_animals > 1 and number_of_animals < river_length:
        for animal in animals.copy():
            step = randint(-1, 1)
            if step:
                last_pos = animal.get_pos()
                animal.move(step)
            else:
                continue

            if animal.get_pos() == river_length or animal.get_pos() < 0:
                animal.move(-step)
                continue

            if isinstance(animal, Fish) and animal.is_alive():
                if isinstance(river[animal.get_pos()], Fish):
                    animal.move(-step)

                    while True:
                        i = randint(0, river_length - 1)
                        if not river[i]:
                            break

                    river[i] = Fish(i)
                    animals.add(river[i])
                    number_of_animals += 1
                    num_of_fishes += 1
                    print(f"A fish was born from {animal.get_pos()}")

                elif isinstance(river[animal.get_pos()], Bear):
                    print("A fish jumped into a bear's mouth")
                    river[last_pos] = None
                    animals.remove(animal)
                    number_of_animals -= 1
                    num_of_fishes -= 1

                else:
                    river[last_pos], river[animal.get_pos()] = river[animal.get_pos()], river[last_pos]

            elif isinstance(animal, Bear):
                if isinstance(river[animal.get_pos()], Fish):
                    print("A bear chased a fish")
                    animals.remove(river[animal.get_pos()])
                    river[animal.get_pos()] = river[animal.get_pos()].die()
                    river[last_pos], river[animal.get_pos()] = river[animal.get_pos()], river[last_pos]
                    number_of_animals -= 1
                    num_of_fishes -= 1                
                
                elif isinstance(river[animal.get_pos()], Bear):
                    animal.move(-step)

                    while True:
                        i = randint(0, river_length - 1)
                        if not river[i]:
                            break

                    river[i] = Bear(i)
                    animals.add(river[i])
                    number_of_animals += 1
                    num_of_bears += 1
                    print(f"A bear was born from {animal.get_pos()}")
                
                else:
                    river[last_pos], river[animal.get_pos()] = river[animal.get_pos()], river[last_pos]

            if number_of_animals <= 1 or number_of_animals >= river_length:
                break

        print(f'{river}\nNumber of animals {number_of_animals}\n')

    print(f'This is the ecosystem at the end:')
    print(river)
    print(f"Number of animals {number_of_animals}")
    print(f"Number of fishes {num_of_fishes}")
    print(f"Number of bears {num_of_bears}")

# ecosystem(10000)

for i in range(100):
    print(f'{i} ----------------------------------START-------------------------------')
    ecosystem(10)

