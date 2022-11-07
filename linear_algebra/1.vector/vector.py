from numpy import array as vector


def ex1():
    o = vector([0, 0])
    p1 = vector([0, -4])
    p2 = vector([-3, 1])
    q = vector([2, 3])
    q1 = vector([2, -1])
    q2 = vector([-1, 4])

    print('vector OQ =', q-o)
    print('vector P1Q1 =', q1-p1)
    print('vector P2Q2 =', q2-p2)



def ex2():
    x = vector([1, 2])
    y = vector([-2, 4])

    print('x+y=', x+y)
    print('x-y=', x-y)
    print('-2*x=', -2*x)


def ex3():
    o = vector([0, 0, 0])
    p1 = vector([0, -4, 2])
    p2 = vector([-3, 1, 0])
    q = vector([2, 3, 4])
    q1 = vector([2, -1, 6])
    q2 = vector([-1, 4, 4])

    print('vector OQ =', q-o)
    print('vector P1Q1 =', q1-p1)
    print('vector P2Q2 =', q2-p2)


def ex4():
    x = vector([1, 2, -3, 4])
    y = vector([-2, 4, 1, 0])

    print('vector x+y =', x+y)
    print('vector x-y =', x-y)
    print('vector -2x =', -2*x)


def ex5():
    x = vector([1, 2, -3, 4])
    y = vector([-2, 4, 1, 0])
    z = vector([5, -2, 3, -7])

    print('vector 2x-3y+z =', 2*x-3*y+z)




ex5()