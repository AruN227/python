import time
import math

def calculate_time(func):

    def inner(*agrs, **kwargs):

        begin = time.time()

        func(*agrs, **kwargs)

        end = time.time()

        print("total time taken: ", func.__name__, end - begin)
    return inner

@calculate_time
def factorial(num):

    time.sleep(2) 
    print(math.factorial(num)) 

factorial(1)


def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(next(x)) # In Python 3, __next__() 
print(next(x))
print(next(x)) 