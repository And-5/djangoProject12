# ls = [4, [7, 8], 6]
# _, [x_1, _], y = ls
# x_1, _ = x
# print(x_1)
# print(y)


ls_1 = [ (3, [9, 1]), [(23,43), [5, 4]] ]
x = 0
for i in ls_1:
    _, [x, _] = i
x += x
print(x)






# def simple(a):
#     found_numbs = 0
#     last_prime = 1
#     while found_numbs != a:
#         prime = True
#         for y in range(2, last_prime):
#             if last_prime % y == 0:
#                 prime = False
#                 break
#         if prime:
#             found_numbs += 1
#             yield last_prime
#         last_prime += 1


# generator =simple(10000)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


from functools import partial
#
#
# def fn(a, b, c, d):
#     return (a + b) / (c * d)
#
# fn2 = partial(fn, 9, 2)
#
# print(fn2)
# print(fn2(10, 4))