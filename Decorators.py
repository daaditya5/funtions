# decorator takes function as an argument and returns a function, which is waiting to execute


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper message executed this before {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func


def display1():
    print('display function ran')


decorator_display = decorator_func(display1)
decorator_display()


@decorator_func
def display2():
    print('display2 has run')
# this code similar as display2 = decorator_dunc(display2)


display2()


@decorator_func
def display_info(name, age):
    print('diaplay_info ran {} {}'.format(name, age))


display_info('Sukesh', 27)
