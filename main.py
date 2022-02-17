import random
#
# class utility:
#     def __init__(self):
#         pass
#
#     def generateTestArray(self):
#         a = []
#         for i in range(10000):
#             a.append(random.randint(0, 10000))
#         return a
#

@profile
def SCAN(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                print(i, " - ", j)
                print('SCAN Duplicate Element', a[i])
                return
            else:
                continue
    return


# def STOR(a):
#     n = len(a)
#     print('n', n)
#     b = [0] * 1001
#     for i in range(n):
#         print('test', b[a[i]], i)
#         if b[a[i]] == 1:
#             print("meet duplicate when i = ", i)
#             print('STOR Duplicate Element', a[i])
#             print(b, len(b))
#         else:
#             b[a[i]] = 1
@profile
def STOR(a):
    n = len(a)
    b = []
    for i in a:
        if i not in b:
            b.append(i)
        else:
            print('STOR Duplicate Element', i)
            print('finished', b)

def generateArray():
    arr = list(range(1, 1001))
    arr.append(random.randint(0, 1000))

    random.shuffle(arr)
    return arr


array_a = generateArray()


SCAN(array_a)
STOR(array_a)
