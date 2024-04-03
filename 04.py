stored_args = None
stored_values = None

def memoize(f):

    def mem_f(*args):
        global stored_args
        if stored_args == args:
            global stored_values
            return stored_values
        stored_args  = args
        stored_values = [f(x) for x in args]

    return mem_f

def negate(b: bool): # функция с побочным эффектом

    global log
    log += 'log updated '
    return not b

log = ''
negate(True)
negate(True)
print(log) #зафиксирована история 2-х вызовов >log updated log updated 

log = ''
mem_negate = memoize(negate)
mem_negate(True)
mem_negate(True)
print(log) #зафиксирован только последний вызов >log updated

def pure_negate(b: bool, log: str):
    return (not b, log + 'log updated ')

log = ''
log1 = pure_negate(True, 'str 1 ')
log2 = pure_negate(True, 'str 2 ') # нужно хранить много переменных
print(log1[1])
print(log2[1])

def negate_inform(b: bool): # функция без побочного эффекта
    return (not b, 'log updated ')

def to_upper(s: str) -> str:
    return ''.join(list(map(lambda x: x.upper(), s)))

def to_words(s: str) -> list:
    return s.split()

def to_upper_msg(s: str) -> tuple: # чистая функция с лог-сообщением
    return (''.join(list(map(lambda x: x.upper(), s))), 'to_upper_msg ')

def to_words_msg(s: str) -> tuple:
    return (s.split(), 'to_words_msg ')

def combine(s: str): # композиция чистых функций
    uppered = to_upper_msg(s)
    splited = to_words_msg(uppered[0])
    return (splited[0], uppered[1] + splited[1])

print(combine('Hello, world!'))

def combine_template(func1, func2): # композиция как функция высшего порядка
    
    def wrapper(*args, **kwargs):
        res_1 = func1(*args, **kwargs)
        res_2 = func2(res_1[0])
        return (res_2[0], res_1[1] + res_2[1])
    
    return wrapper

my_combine = combine_template(to_upper_msg, to_words_msg) 
assert my_combine('Hello, world!') == combine('Hello, world!') # проверка соответствия композиции и шаблона композиции

def identity(s): # морфизм в себя
    return (s, '')

my_combine = combine_template(my_combine, identity)  # проверка морфизма в себя
print(my_combine('Hello, world!'))
assert my_combine('Hello, world!') == combine('Hello, world!')

def to_lower_msg(s: str) -> tuple: # чистая функция с лог-сообщением для дополнительной проверки
    return (''.join(list(map(lambda x: x.lower(), s))), 'to_lower_msg ')

my_combine = combine_template(my_combine, to_lower_msg) # композиция работает
print(my_combine('Hello, world!'))
