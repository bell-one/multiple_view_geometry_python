from numpy import array as vector


def ex1():
    ## R^2의 점 P(0, -4) P2(-3,1) Q(2,3), Q1(2,-1), Q2(-1,4)에 대해 OQ, P1Q1, P2Q2를 성분으로 표시하라
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
    ## R^2의 벡터 x =[1, 2], y = [-2, 4] 에 대하여 x+y, x-y, (-2)x를 구하여라
    x = vector([1, 2])
    y = vector([-2, 4])

    print('x+y=', x+y)
    print('x-y=', x-y)
    print('-2*x=', -2*x)


def ex3():
    ## R^3의 점 P1(0, -4, 2), P2(-3, 1, 0), Q(2, 3, 4), Q1(2, -1, 6), Q2(-1, 4, 4)에 대하여 OQ, P1Q1, P2Q2를 성분으로 표시하라
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
    ## R^4의 벡터 x=[1, 2, -3, 4], y = [-2, 4, 1, 0] 에 대하여 x+y, x-y, (-2)x를 구하여라.
    x = vector([1, 2, -3, 4])
    y = vector([-2, 4, 1, 0])

    print('vector x+y =', x+y)
    print('vector x-y =', x-y)
    print('vector -2x =', -2*x)


def ex5():
    ## R^4의 벡터 x=[1, 2, -3, 4], y = [-2, 4, 1, 0], z = [5, -2, 3, -7] 에 대하여 2x-3y+z를 구하여라.
    x = vector([1, 2, -3, 4])
    y = vector([-2, 4, 1, 0])
    z = vector([5, -2, 3, -7])

    print('vector 2x-3y+z =', 2*x-3*y+z)




ex5()