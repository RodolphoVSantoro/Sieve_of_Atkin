from _thread import *
import time


def file_len(fname):
    a = 0
    with open(fname) as f:
        for a, l in enumerate(f):
            pass
    return a + 1


def ler(fname):
    t = file_len(fname)
    arq = open(fname, "r")
    for i in range(t):
        print(arq.readline())
    arq.close()


def nova_linha(fname, linha):
    arq = open(fname, "r")
    texto = arq.readlines()
    texto.append(str(linha) + "\n")
    arq.close()
    arq = open(fname, "w")
    arq.writelines(texto)
    arq.close()


def esvaziar(fname):
    arq = open(fname, "w")
    arq.write("")
    arq.close()


from math import sqrt, ceil, pow


class SieveOfAtkin:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.sieve = [False] * (self.limit + 1)

    def flip(self, prime):
        try:
            self.sieve[prime] = True if self.sieve[prime] == False else False
        except KeyError:
            pass

    def invalidate(self, prime):
        try:
            if self.sieve[prime] == True: self.sieve[prime] = False
        except KeyError:
            pass

    def isPrime(self, prime):
        try:
            return self.sieve[prime]
        except KeyError:
            return False

    def getPrimes(self):
        testingLimit = int(ceil(sqrt(self.limit)))

        for i in range(testingLimit):
            for j in range(testingLimit):
                # n = 4*i^2 + j^2
                n = 4 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
                    self.flip(n)

                # n = 3*i^2 + j^2
                n = 3 * int(pow(i, 2)) + int(pow(j, 2))
                if n <= self.limit and n % 12 == 7:
                    self.flip(n)

                # n = 3*i^2 - j^2
                n = 3 * int(pow(i, 2)) - int(pow(j, 2))
                if n <= self.limit and i > j and n % 12 == 11:
                    self.flip(n)

        for i in range(5, testingLimit):
            if self.isPrime(i):
                k = int(pow(i, 2))
                for j in range(k, self.limit, k):
                    self.invalidate(j)

        self.primes = [2, 3] + [x for x in range(len(self.sieve)) if self.isPrime(x) and x >= 5]
        return self.primes


esvaziar("primos.txt")
tempo_total = time.time()

soa = SieveOfAtkin(100000000)

arq = open("primos.txt", "w")
arq.writelines(str(soa.getPrimes()))
arq.close()
print("tempo total", (time.time() - tempo_total), "s")
