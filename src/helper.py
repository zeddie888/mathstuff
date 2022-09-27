from math import *
import string

ALPHABET = list(string.ascii_uppercase)

def C(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

def P(n, k):
    return factorial(n) / factorial(n-k)


def multi(n, *ks):
    divBy = 1
    for k in ks:
        divBy *= factorial(k)
    return factorial(n) / divBy


def quad(a, b, c):
    divBy = 2*a
    foo = sqrt(b**2 - 4*a*c)
    res1 = (-b - foo) / divBy
    res2 = (-b + foo) / divBy
    return (res1, res2)
