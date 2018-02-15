# every time we called generator, it yields or results one value


def sq_num(num):
    result = []
    for i in num:
        result.append(i*i)
    return result


print(sq_num([1,2,3,4,5]))

sq_num1 = [x*x for x in [1,2,3,4,5]]
print(sq_num1)


def sq_num3(num):
    for i in num:
        yield i*i


print(sq_num3([1,2,3,4,5]))
sq = sq_num3([1,2,3,4,5])
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))

for i in sq:
    print(i)


sq1 = (x*x for x in [1,2,3,4,5])  # --> generator
print(list(sq1))