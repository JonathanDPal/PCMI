from general_use import gcd
from FastModularExponentiation import fme


def pminus1(N, a, ub, inc):
    """
    Args:
        N (int): Integer to be factored
        a (int): The number to be exponentiated (should be a small number).
        ub (int): The upper bound on our exponentiation
        inc (int): How often to compute the gcd.
    Returns:
        d (int): a factor of N, hopefully nontrivial. If 1 or N is returned, then perhaps try a different value for "a".
    """
    iteration = 0
    d = 1
    for j in range(2, ub + 1):
        iteration += 1
        if iteration % inc == 0:
            d = gcd(a - 1, N)
            if 1 < d < N:
                break
            elif d == N:
                break
        a = fme(a, j, N)
        if a == 0 or a == 1:
            break
    return d


if __name__ == "__main__":
    import sys
    N, a, ub, inc = [int(x) for x in sys.argv[1:5]]
    d = pminus1(N, a, ub, inc)
    if d == 1:
        print("d = 1 returned.")
    elif d == N:
        print("d = N returned")
    else:
        d2 = int(N / d)
        assert N == d * d2
        print(f"{N} = {d} * {d2}")
