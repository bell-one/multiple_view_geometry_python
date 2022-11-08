from numpy import array as vector
import numpy.linalg as linalg

def q1():
    ## 다음의 주어진 두 점 P1 과 P2에 의해 정의되는 벡터 P1P2를 구하여라
    p1 = vector([5, -2 ,1])
    p2 = vector([2, 4, 2])
    p1p2 = p2 - p1
    print(p1p2)


def q2():
    ## 끝점이 (-1, -1, 2)인 벡터 x=(1, 1, 3)의 시작점은?
    x = vector([1, 1, 3])
    end = vector([-1, -1, 2])
    start = end - x
    print(start)


def q3():
    ## 벡터 u v, w  를 다음과 ㅏㅌ이 정의했을 때 다음의 벡터를 구하여라
    u = vector([-3, 1, 2, 4, 4])
    v = vector([4, 0, -8, 1, 2])
    w = vector([6, -1, -4, 3, -5])
    sol = (2*u - 7*w) - (8*v + u)
    print(sol)


def q4():
    ## 위에서와 같이 u, v, w가 주어졌을때 다음을 ㅂ만족하는 벡터 x를 구하여라
    u = vector([-3, 1, 2, 4, 4])
    v = vector([4, 0, -8, 1, 2])
    w = vector([6, -1, -4, 3, -5])
    x = (2*u - v - w) / 6
    print(x)


def q5():
    ## 두 벡터 x=(-1, -2, 3), y=(3, -2, -1)사이의 각을 theta라 할때 cos theta를 구하여라
    x = vector([-1, -2, 3])
    y = vector([3, -2, -1])
    costheta = x@y / linalg.norm(x) / linalg.norm(y)
    print(costheta)


def q6():
    ## 두점 P(-1, 2, 1), Q(-3, -4 , 5)사이의 거리를 구하여라
    p = vector([-1, 2, 1])
    q = vector([-3, -4 ,5])
    dist = linalg.norm(p - q)
    print(dist)

def q7():
    ## x=(a, 2, -1, a), y=(-a, -1, 3, 6)일때 x@y=0 을 만족하는 실수 a를 모두 구하여라
    ## x@y = -a^2 -2 -3 +6 a = 0
    ## a^2 -6a +5 = 0
    ## (a-1)(a-5)=0 a = 1, 5
    pass


def q8():
    ## 두점 P(-5, 1, 3), Q(2, -3, 4)를 지나는 직선의 방정식을 구하여라
    p = vector([-5, 1, 3])
    q = vector([2, -3 ,4])
    dir = q - p
    t = 1
    x = q[0] - dir[0] * t
    y = q[1] + dir[1] * t
    z = q[2] - dir[2] * t


def q9():
    ## 주어진 평면 z=-7x+y+4 에 수직인 법선벡터를 찾아라.
    normal_vector = vector([7, -1, 1])


def q10():
    ## x=(2, -1, 3)과 y=(4, -1, 2)일 때, y의 x상의 정사영 p와 y의 x에 수직인 벡터성분 w를 구하여라.
    x = vector([2, -1, 3])
    y = vector([4, -1, 2])

    projxy = (x@y)/(x@x)*x
    w = y-projxy


def p1():
    ## 크기와 방향이 각각 가은 벡터는 벡터로서는 같은 벡터이다. 그러나 공간에서 기울기가 같은 두개의 다른 직선은 방정식으로서는 어떤 관계인지 토론해 보아라
    ## bias 조정이 되면 같은 직성니 됨.
    pass


def p2():
    ## v1=(2/3, 1/3, 2/3)와 v2=(1/3, 2/3, -2/3)가 정규직교벡터임을 보이고 v1, v2, v3가 정규직교 벡터가 되는 세번째 벡터 v3를 구하여라
    pass


q10()