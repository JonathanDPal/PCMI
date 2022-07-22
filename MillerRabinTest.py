from general_use import randomsubset, gcd
from FastModularExponentiation import fme


def mrt(N, I=100):
    """
    Runs the Miller-Rabin Test to test whether a number is likely to be prime.
    ---
    Args:
        N (int): The number to be tested for primailty.
        I: How many potential witnesses to test. If I >= N-1, then it only N-1 potential witnesses will be used,
        since this is sufficient to know with certainty whether the number is prime.
    Returns:
        True if number is likely to be prime, False if number is (definitely) composite.
    """
    if N % 2 == 0:
        return False
    Q = (N - 1) / 2
    k = 1
    while Q % 2 == 0:
        k += 1
        Q /= 2
    Q = int(Q)
    if I >= N:
        candidates = [x for x in range(2, N)]
    else:
        candidates = randomsubset(2, N-1, I)
    prime = True
    success = False
    for cd in candidates:
        if 1 < gcd(cd, N) < N:
            prime = False
            break
        cd = fme(cd, Q, N)
        if cd == 1 or cd == (N - 1):
            continue
        else:
            success = True
            for _ in range(1, k):
                cd = (cd ** 2) % N
                if cd == (N - 1):
                    success = False
                    break
            if not success:
                break
    if success:
        prime = False
    return prime


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    if len(sys.argv) == 3:
        i = int(sys.argv[2])
        isprime = mrt(n, i)
    else:
        isprime = mrt(n)
    if isprime:
        print("prime")
    else:
        print("composite")
