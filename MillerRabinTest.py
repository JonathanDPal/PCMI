from general_use import randomsubset, gcd


def mrt(N, I=100):
    """
    Runs the Miller-Rabin Test to test whether a number is likely to be prime.
    ---
    Args:
        N (int): The number to be tested for primailty.
        I: How many potential witnesses to test. If I >= N-1, then it only N-1 potential witnesses will be used,
        since this is sufficient to know with certainty whether the number is prime.
    Returns:
        True if number is prime, False if number is composite.
    """
    if N % 2 == 0:
        return True
    Q = (N - 1) / 2
    k = 1
    while Q % 2 == 0:
        k += 1
        Q /= 2
    prime = True
    if I >= N:
        candidates = [x for x in range(2, N)]
    else:
        candidates = randomsubset(2, N-1, I)
    for cd in candidates:
        if gcd(cd, N) < N:
            prime = False
            break
        cd = (cd ** Q) % N
        if cd == 1 or cd == -1:
            continue
        else:
            success = True
            for _ in range(k-1):
                cd = (cd ** 2) % N
                if cd == -1:
                    success = False
                    break
            if success:
                prime = False
                break
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
