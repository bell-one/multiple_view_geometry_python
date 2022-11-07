from numpy import array as vector
import numpy.linalg as linalg


def ex1():
    ## 점 P1(2, -1, 3)을 지나고, 벡터 v=(-3,2,4)에 평행한 직성의 방정식은 다음 세가지로 나타낼 수 있다.
    ## 1 벡터방정식
    p1 = vector([2, -1, 3])
    v = vector([-3, 2, 4])
    t = 1
    s1 = p1 + t*v

    ## 2 매개변수 방정식
    x = p1[0] - t * v[0]
    y = p1[1] - t * v[1]
    z = p1[2] - t * v[2]

    ## 3 대칭방정식
    ## x-p1[0]/v[0] = y-p1[1]/v[1] = z-p1[2]/v[2]


def ex2():
    ## 두점 P(1, 1, -2), Q(4, -1, 0)을 지나는 직선의 매개변수 방정식을 구하라.
    p = vector([1, 1, -2])
    q = vector([4, -1, 0])
    pq = q - p
    t = 1
    x = p[0] + t * pq[0]
    y = p[1] + t * pq[1]
    z = p[2] + t * pq[2]


## 평면방정식

## 법선벡터와 한 점
## R^3에서 p(x0, y0, z0)을 지나고 n(a, b, c)에 수직인 평면은?
## 평면의위 점 x, y, z에 대해
## n@(x-x0, y-y0, z-z0) = 0   수직 --> 내적 0
## ax + by + cz = ax0 + bx0 + cz0

## 벡터방정식
## W 위 점 x0, 과 상수배 아닌 v1, v2가 있으면
## x - x0 = t1v1 + t2v2

## 매개방정식
## X=(x,y,z) X0=(x0, y0, z0) v1=(a1, b1, c1) v2=(a2, b2, c2)
## X = X0 + t1v1 + t2v2
## x = x0 + t1a1 + t2a2
## y = x0 + t1b1 + t2b2
## z = x0 + t1c1 + t2c2


def ex3():
    ## 세점 P(4, -3, 1), Q(6, -4, 7), R(1, 2, 2)를 지나는 평면의 벡터방정식과 매개방정식을 구하여라
    p = vector([4, -3, 1])
    q = vector([6, -4, 7])
    r = vector([1, 2, 2])
    ## x-x0 = t1v1 + t2v2
    t1 = 1
    t2 = 1
    v1 = q-p
    v2 = r-p
    x = p[0] + t1*v1[0] + t2*v2[0]
    y = p[1] + t1*v1[1] + t2*v2[1]
    z = p[2] + t1*v1[2] + t2*v2[2]


def ex4():
    ## x=(2, -1, 3), y=(4, -1, 2)에 대하여 x 위로의 y의 정사영 projxy와 x에 수직인 y의 벡터성분 w 를 구하여라
    x = vector([2, -1, 3])
    y = vector([4, -1, 2])
    projxy = x@y / linalg.norm(x) / linalg.norm(x) * x
    ##projxy = x@y / (x@x) * x
    w = y - projxy
    print(projxy)
    print(w)


def ex5():
    ##점 P(3, -1, 2)에서 평면 x+3y-2z-6=0 에 이르는 거리 D 를 구하여라
    p = vector([3, -1, 2])
    n = vector([1, 3, -2])
    ## 평면과 p의 거리 벡터 v
    ## v = op0 - op1 (p1 은 평면의 한 점)
    ## v = (3-x1, -1-y1, 2-z1)
    ## projnv = v@n / norm(n)^2 * n
    ## v@n = 3-x1 + (-1-y1)*3 + (2-z1)*-2
    ## v@n = -x1 - 3y1 + 2z1 - 4 = -6-4 = -10
    projnv = -10 / linalg.norm(n) / linalg.norm(n) * n

    d = linalg.norm(projnv)
    print(projnv)
    print(d)


ex5()
