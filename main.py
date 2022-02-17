import random

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
