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

#function with default argument
def test(name, msg='hardcoded value'):
    print('hello',name,',', msg)

test('karthik')
test('kennedy','override the default value')

#passing string as argument
def stringsample(s):
    print(s)
    return
stringsample("welcome")
stringsample("string as argument")

#pass by reference , List arg passsing to fun
def listsample(l):
    print('inside the fun..',l)
    return

l=[10,20,30]
listsample(l)
print('outside fun..',l)

#pass by reference , List arg passsing to fun
def listsample(l):
    print('inside the fun..',l)
    return

#l=[10,20,30]
listsample([10,20,30,40])
print('outside fun..',l) #this time printing above value

#pass by reference , List arg passsing to fun
def listsample(l):
    l=[44,55,66]
    print('inside the fun..',l)
    return

l=[11,22,33]
listsample(l)
print('outside fun..',l)

#argument required
def stringsample(s):
    print(s)
    return
#stringsample() #arg req

#keyword arg
def stringsample(s):
    print(s)
    return;

stringsample(s="karthik kennedy")

#keyword arg
def stringsample(name,age):
    print('Name: ', name,',','Age: ',age)
    return;

stringsample(name="karthik kennedy",age=31)

#default arg
def printval(name,age=30):
    print('Name: ', name, ',', 'Age: ', age)
    return;

printval(name="karthik", age=32)
printval(name="sugi")

#arbitary argument
def show(*name):
    for names in name:
        print('hello ',name)

show('karthik','kennedy','sugi','ganesh')

#anonymous fun
sum=lambda arg1,arg2:arg1+arg2

print('sum of value ',sum(10,20))

#global vs local variable scope
total=0; #global variable
def sum(a1,a2):
    total=a1+a2;
    print('inside local',total)

sum(20,20)
print('outside ',total)

#recursive fun
def fact(n):
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))

num=5
print('factorial of ',num, 'is', fact(num))





