import time

# 1. one function as an argument in another

def demo(a):
  return a-1
  # creating another function that takes a function as an argument
def hi(func, a):
  res = func(a)
  return res

print(hi(demo, 8))
print("---End---")

# 2. one function being defined and executed withoin another function
# 3. that function can also be returned in the main functiona
# 4. using decorator funtion to run a function - the xyz function


def xyz():
  print("Hi, How are you")

def decoratorFunc(callbackFunc):
    # this function is to execute some code before and after the executing function
  def inner_function():
    print("Executing", callbackFunc.__name__, "function")
    callbackFunc()
    print("Finished executing")
  return inner_function # make sure you dont write () in front of the inner function

# this one is without decorator
print("--First way--")
xyz()

# this one is with the decorator
print("--Second way--")
ddfunc = decoratorFunc(xyz)
ddfunc()

# this is decorator using the @ symbol

@decoratorFunc
def printy():
  print("this is the printy function")

print("--Third way--")
printy()

print("---End---")

# 5. use argumented decorators

def divide_safe(callbackFunc):
  def inner_function(a,b):
    print("Dividing", a, "by", b)
    # check if b is 0
    if b == 0:
      print("cannot perform divsion")
      return
    return callbackFunc(a,b)
  return inner_function

# use decorator on a function
@divide_safe
def divideFunc(a,b):
  print(a/b)


divideFunc(5, 5)
divideFunc(5, 0)
print("---End---")


# 6. Chaining decorators

def decor1(callbackFunc):
  def inner_function(message):
    print('$'*20)
    callbackFunc(message)
    print('$'*20)
  return inner_function

def decor2(callbackFunc):
  def inner_function(message):
    print('&'*20)
    callbackFunc(message)
    print('&'*20)
  return inner_function

@decor1
@decor2
def abc(message):
  print(message)


abc("Hi Jesus loves you")
print("---End---")


# 7. class decorator

class Decorator:
  def __init__(self, func):
    self.function = func
  def __call__(self, *args, **kwargs):
    print("Hello Start")
    self.function(*args, **kwargs)
    print("Hello End")

@Decorator
def demoFunction1( name, msg ):
  print("{}, {}".format(msg, name))

demoFunction1("Daniel", "Jesus loves you")

print("---")

class Timer:
  def __init__(self, func):
    self.function = func
  def __call__(self, *args, **kwargs):
    startTime = time.time()
    func = self.function(*args, **kwargs)
    endTime = time.time()
    print("Execution took {} seconds".format(endTime - startTime))
    return func

@Timer
def demoFunction(timeDelay):
  print("wait {} seconds".format(timeDelay + 1))
  time.sleep(timeDelay)

demoFunction(2)
print("---")


class CheckError:
  def __init__(self, func):
    self.func = func
  def __call__(self, *args):
    if any([isinstance(i, str) for i in args]):
      print("Parameter must only be number !!")
      return
    else:
      return print(self.func(*args))

@CheckError
def add_numbers(*numbers):
  return sum(numbers)

add_numbers(1,2,3)
add_numbers(1,2,'3')

print("---End---")

# 8. Context Managers

# files = []
# for b in range(10000):
#   files.append(open('index.txt', 'w'))

class ContextManager():
  def  __init__(self):
    print("init method is called")
  def __enter__(self):
    print("self method is called")
  def __exit__(self, excType, excValue, excTraceback):
    print('called the exit method')
  
with ContextManager() as Manager:
  print("with statement block")

print("---")

class FileManager():
  def __init__(self, fName, fMode):
    self.name = fName
    self.mode = fMode
    self.file = None
  def __enter__(self):
    self.file = open(self.name, self.mode)
    return self.file
  def __exit__(self, excType, excValue, excTraceback):
    self.file.close()

with FileManager('index.txt', 'w') as f:
  f.write('sample')

print(f.closed)

print("---End---")


# 9. Generators

def fib(l):
  x, y = 0, 1
  # one by one yeild the next fibo
  while x < l:
    yield x
    x, y = y, x + y

m = fib(10)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print("--using for lop")

for j in fib(10):
  print(j)