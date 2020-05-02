a = int(input('Введи число '))
b = int(input('Введи 2число '))
while True:
    if a <= b :
        print(a, end=' ')
        a += 1
    else:
        a = b
        break