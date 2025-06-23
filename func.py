import math
import numpy as np
from time import process_time
import plotly.graph_objects as go

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    digits = list(str(n))
    if digits == list(reversed(digits)):
        return True


def num_factors(n):
    factors = 2
    if n == 1:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors += 2
        if (n**0.5) % 1 == 0:
            factors -= 1
    return factors


def Sieve_Of_Eratosthenes(a):
    primes = [i for i in range(a + 1)]
    p = 2
    while p * p <= a:
        if primes[p] != 0:
            for i in range(p * p, a + 1, p):
                primes[i] = 0
        p += 1
    primes.remove(1)
    return primes


def time():
    print(process_time())

def polyeval(poly, x):
    value = 0
    for i in range(len(poly)):
        #print(i)
        value += poly[i]*math.pow(x, i)

    return value

def polydiff(poly):
    diff = []
    for i in range(1, len(poly) ):
        diff.append(poly[i]*i)
    return diff


def newt_raph(poly, initval, iters):
    diff = polydiff(poly)
    diff.reverse()
    poly.reverse()
    x = initval
    for i in range(0, iters):
        x = x - np.polyval(poly, x) / np.polyval(diff, x)
    return x


def lagrange(x, y):
    m = len(x)
    if len(y) != m:
        exit(1)
    coeff = np.zeros(m)

    temp = [1]

    for i in x:
        temp = np.polymul(temp, [1, -i])

    for i in range(m):
        a=1
        for j in range(m):
            if i != j:
                a = a * (x[i] - x[j])

        coeff = coeff + y[i]/a * np.polydiv(temp, [1, -x[i]])[0]

    return coeff


def poly_plot(coeff, x0, xf, n):
    x = np.linspace(x0, xf, n)
    p = np.poly1d(coeff)
    y = p(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=str(p)))
    fig.update_layout(title="Polynomial Plot", xaxis_title="x", yaxis_title="f(x)")
    fig.show()


