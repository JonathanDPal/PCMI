from FastModularExponentiation import fme
import math


def bsgs(A, B, C):
    """
    solving DLP for A^x = B (mod C) with big steps, little steps. "A" needs to be a generator for the group.
    """
    N = math.floor(math.sqrt(C)) + 1
    refs = [A]
    for _ in range(N - 1):
        refs.append(fme(refs[-1], 2, C))
    AinverseN = fme(fme(A, C - 2, C), N, C)  # works because of Fermat's Little Theorem, although I may experiment to
    # see if Extended Euclidean Algorithm is faster
    prod = B
    x1 = 0
    found = False
    while not found:
        for k, ref in enumerate(refs):
            if prod == ref:
                x0 = k + 1  # since 0-based indexing
                found = True
                break
        if not found:
            prod = (prod * AinverseN) % C
            x1 += 1
        if x1 >= N:
            raise Exception("answer not found")
    return (N * x1) + x0


if __name__ == '__main__':
    import sys
    a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    print(bsgs(a, b, c))
