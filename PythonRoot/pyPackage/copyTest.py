import copy
a = ['hello', [1, 2, 3]]
b = a
c = copy.copy(a)
d = copy.copy(a)
a.append(5)
a[1].append(4)
a[0] = 'world'
for index, value in enumerate(a):
    print('id a%d'%index, id(value), value)
for index, value in enumerate(b):
    print('id a%d'%index, id(value), value)
for index, value in enumerate(c):
    print('id a%d'%index, id(value), value)
for index, value in enumerate(d):
    print('id a%d'%index, id(value), value)
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))
