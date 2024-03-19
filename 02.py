import time
import random

stored_args = None
stored_values = None
random.seed(100)

def memoize(f):

    def mem_f(*args):
        global stored_args
        if stored_args == args:
            global stored_values
            return stored_values
        stored_args  = args
        stored_values = [f(x) for x in args]

    return mem_f

def _f(x):
    return [x ** i for i in range(x)]

def f_time(f, x):
    a = memoize(f)
    start_1 = time.time()
    res1 = a(x)
    end_1 = time.time()
    start_2 = time.time()
    res_2 = a(x)
    end_2 = time.time()
    print(end_1 - start_1)
    print(end_2 - start_2)
    res_3 = a(x)
    assert res_2 == res_3


def _random(x):
    return [random.randint(0, x) ** i for i in range(x)]
    

f_time(_f, 10000) #1
f_time(_random, 10001) #3

def _not(x: bool):
    return not x

def _identity(x: bool):
    return x

def _false(x: bool):
    return False

def _true(x: bool): #4
    return True 
