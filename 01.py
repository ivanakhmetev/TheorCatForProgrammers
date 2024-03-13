
def id(a):
    return a

def compose(f, g):
    return lambda x: f(g(x))

def add_2(a):
    return a + 2

def mult_2(a):
    return a * 2

a = compose(add_2, mult_2)
assert a(2) == 6
a = compose(add_2, id)
assert a(2) == 4
a = compose(id, add_2)
assert a(2) == 4
