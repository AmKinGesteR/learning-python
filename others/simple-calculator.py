a = input(str('Select First Number ? '))
a2 = int(a)

b = input(str('Select Second Number ? '))
b2 = int(b)

c = input(str('Select Numbers\n  1 - Zarb\n  2 - Taghsim\n  3 - Jam\n  4 - Menha\n ==> '))

if c == '1' :
    d = a2 * b2
    print(d)

if c == '2' :
    e = a2 / b2
    print(e)

if c == '3' :
    f = a2 + b2
    print(f)

if c == '4' :
    g = a2 - b2
    print(g)