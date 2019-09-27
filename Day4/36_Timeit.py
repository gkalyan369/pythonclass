import timeit

t = timeit.timeit('''
cubes = []
for n in range(100):
    cubes.append(n ** 3)
''', number=10000)

print(t)

t = timeit.timeit('[n ** 3 for n in range(100)]', number=10000)
print(t)

t = timeit.timeit('map(lambda n: n ** 3, range(100))', number=10000)
print(t)
