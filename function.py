from turtledemo import two_canvases

m = [4, 3, 6]


def modify(k):
    k.append(8)
    print(k)


modify(m)

f = [2, 4, 5, 1]


def replace(g):
    g = [5, 6, 3, 2]
    print(g)


replace(f)

f = [5, 6, 7, 8]


def replace_content(g):
    g[0] = 10
    g[1] = 20
    g[2] = 30
    print("g=", g)


print(f)
replace_content(f)


def f(d):
    return d


c = [6, 10, 16]

e = f(c)
print(c is e)


# sum of two number
def sum(x, y):
    "goint to add two numbers"
    s = x + y
    print("sum = ", s)


sum(10, 20)


# second example for sum of two method
def fun(x, y):
    print("x+y", x + y)
    return x + y


fun(20, 20)
print(fun(100, 100))


# third example for sum of two method

def sum(a, b):
    print(a + b)
    return a + b


def msg():
    print('hello')
    return


total = sum(10, 10)
print('printing outside', total)
msg()
print("rest of code")


# fibanooci serious
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


fib(2000)
print()


# function parameter
def greet(name):
    """sfdsfsdfsdfsdfs
    sdfsdfsdf
    sdfsdfs"""
    print('hello', name, 'welcome')


# function call
greet('karthik')

# Doc String
print(greet.__doc__)


# return statement programs
def absolute_value(n):
    if n >= 0:
        return n
    else:
        return -n


print(absolute_value(10))
print(absolute_value(-4))

#function with two argument
def twoarg(name,age):
    print('hello', name, ',' ,age)

twoarg('karthik',30)
