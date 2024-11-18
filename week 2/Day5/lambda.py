def freak(x):
    print("Hello", x[0], x[1])
    return x[0]


x = [(11, "chaitanya"),(2, "kamalesh")]
x = sorted(x, key = freak)
#x = sorted(x, key= lambda y : y[0])
print(x)