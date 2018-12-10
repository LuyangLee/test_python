def triangles(max):
    n = 1
    l = [[1]]
    while n <= max:
        print(l)
        n += 1
        if n == 2:
            l.append([1,1])
            print(l)
            n += 1
        nl = [1]
        for i in range(len(l[n - 2]) - 1):
            nl.append(l[n-2][i] + l[n-2][i + 1])
        nl.append(1)
        l.append(nl)
        print(l)

class Sample:
    def __enter__(self):
        print("entry")
        return 6
    def __exit__(self, type, value, path):
        print('type',type)
        print('value',value)
        print('path',path)
# with Sample() as e:
#     print("jieguo",0/0)


    