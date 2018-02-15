def square(x):
    return x * x


def cube(x):
    return x * x * x


def my_map(func, list_values):
    result = []
    for i in list_values:
        result.append(func(i))
    return result


my_squares = my_map(square, [1, 2, 3, 4, 5])
print(my_squares)

my_cubes = my_map(cube, [1, 2, 3, 4, 5])
print(my_cubes)

square            # it won't execute, we add parenthesis (), it will execute
square(5)         # it doesn't print because, function is just returning value
print(square(5))  # it prints because, we are printing returning value

f = square(5)
print(square)   # it prints function location
print(f)        # it prints returning value

g = square      # --> 'g' is first call function
print(square)   # square and g, both are functions
print(g)
print(g(5))
