from numpy import array as vector
import numpy.linalg as linalg

def ex1():
    ##R^4의 벡터 x=(2, -1, 3, 2), y=(3, 2, 1, -4)에 대하여 다음이 성립한다.
    x = vector([2, -1, 3, 2])
    y = vector([3, 2, 1, -4])
    print(linalg.norm(x))
    print(linalg.norm(y))
    print(linalg.norm(x-y))


def ex2():
    ## ex1의 벡터 x, y에 대해 x@y를 구하여라
    x = vector([2, -1, 3, 2])
    y = vector([3, 2, 1, -4])
    print(x@y) ## inner product
    print(x[0] * y[0] + x[1] * y[1] + x[2] * y[2] + x[3] * y[3])


def ex3():
    ## R^4의 두 벡터 x=(1, 0, 1 ,1), y=(-1, 0, 0, 1)은 서로 직교함을 보여라
    ## x@y = ||x|| ||y|| cos(theta)
    x = vector([1, 0, 1, 1])
    y = vector([-1, 0, 0, 1])
    print(x@y) ## 내적이 0
    ##  --> 사잇각 cos(theta) == 0, theta == 90


def ex4():
    ## 예제 1의 벡터 x, y 에 대해 삼각 부등식이 성립함을 확인하라.
    ## 삼각부등식 ||x+y|| < ||x|| + ||y||
    x = vector([2, -1, 3, 2])
    y = vector([3, 2, 1, -4])

    norm_x = linalg.norm(x)
    norm_y = linalg.norm(y)
    norm_xy = linalg.norm(x+y)
    print(norm_xy <= norm_x+norm_y)




ex4()