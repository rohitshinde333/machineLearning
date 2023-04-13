def even(x):
    return x % 2 == 0

def square(x):
    return x*x

def sumsqureeven(n):
    return sum(map(square,filter(even,range(n+1))))

print(sumsqureeven(10))