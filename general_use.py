import random
from math import floor


def permgenerator(n):
    """
    Using Durstenfield's version of the Fisher-Yates Algorithm to generate a random permutation in linear time.
    """
    perm = [x for x in range(1, n + 1)]
    for i in range(n-1):
        j = random.randint(i, n-1)
        newi = perm[j]
        perm[j] = perm[i]
        perm[i] = newi
    return perm


def randomsubset(low, high, size):
    """
    Gives a random {size}-subset of integers in [{low}, {high}]
    """
    sset = list()
    if size > (high - low + 1):
        raise ValueError('Interval not large enough for size given.')
    while len(sset) < size:
        x = random.randrange(low, high + 1)
        if x not in sset:
            sset.append(x)
    return sset


def gcd(A, B):
    if A > B:
        a = A
        b = B
    else:
        a = B
        b = A
    r = a % b
    if r == 0:
        return b
    else:
        while r != 0:
            prevr = r
            r = b % r
            b = prevr
        return prevr


def modifiedremainder(value, base):
    remainder = value % base
    if remainder < (base / 2):
        return remainder
    else:
        return remainder - base


def isqrt(n):
    """
    Integer square root of n. Formally speaking, this is the floor of the square root of n.
    """
    guess = n // len('{0:b}'.format(n))
    low, high = 0, n
    while not guess ** 2 <= n < (guess + 1) ** 2:
        if guess ** 2 < n:
            low += 1
        else:
            high -= 1
        guess = (high - low) // 2
    return guess


def factorbase(N):
    N = int(N)
    nums = [num for num in range(2, N + 1)]
    fbase = []
    while len(nums) > 0:
        fbase.append(nums[0])
        nums = [num for num in nums if num % nums[0] != 0]
    return fbase
