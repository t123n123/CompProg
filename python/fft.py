from cmath import *
from math import *


class Polynomial:
    def __init__(self, coefs):
        self.coefs = coefs
        self.len = len(coefs)

    def eval(self, x):
        sum = 0
        exp = 1

        for coef in self.coefs:
            sum += coef * exp
            exp *= x

        return sum

    def resize(self, n):
        if n > self.len:
            self.coefs.extend([0] * (n - self.len))
            self.len = n

    def fft(self, invert):
        n = self.len

        if n == 1:
            return self.coefs.copy()

        a0 = []
        a1 = []
        for i in range(n):
            if i % 2 == 0:
                a0.append(self.coefs[i])
            else:
                a1.append(self.coefs[i])

        a0 = Polynomial(a0).fft(invert)
        a1 = Polynomial(a1).fft(invert)

        angle = (2 * acos(-1) / n) * (-1 if invert else 1)
        w = complex(0, 1)
        wn = complex(cos(angle), sin(angle))

        a = [0] * n
        for i in range(n // 2):
            a[i] = a0[i] + w * a1[i]
            a[i + (n // 2)] = a0[i] - w * a1[i]
            if invert:
                a[i] = a[i] / 2
                a[i + (n // 2)] = a[i + (n // 2)] / 2

            w = w * wn

        print(a0)
        print(a1)
        print(a)
        return a

    def __mul__(self, other):
        if type(other) == Polynomial:
            # resize polys to smallest pow of 2 > size of product
            msize = 1
            while msize < self.len + other.len:
                msize = msize << 1
            self.resize(msize)
            other.resize(msize)

            # FFT
            fa = self.fft(False)
            fb = other.fft(False)

            fp = [0] * msize
            for i in range(msize):
                fp[i] = fa[i] * fb[i]

            print(fp)
            prod = Polynomial(fp)
            prod = Polynomial(prod.fft(True))

            return prod


A = Polynomial([1, 1])
B = Polynomial([1, 1])

C = A * B

print(C.coefs)
