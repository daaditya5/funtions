def outer_fun1():
    message = 'hi'

    def inner_fun1():
        print(message)

    return inner_fun1()


outer_fun1()


def outer_fun2():
    message = 'hello'

    def inner_fun2():
        print(message)

    return inner_fun2


outer_fun2()
f = outer_fun2()  # f is function, in order to execute, we have to give ()
f()
f()
f()


def outer_fun3(msg):
    message = msg

    def inner_fun3():
        print(message)

    return inner_fun3


g = outer_fun3('sukesh')
h = outer_fun3('kumar')
g()
h()