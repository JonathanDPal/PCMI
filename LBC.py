def LBCencryption(m, pk, rbound):
    """
    Args:
        m (int): Either 0 or 1.
        pk (iterable): Needs to have x0 as first entry.
        rbound (int): Such that -rbound <= r <= rbound for encryption to be successful.
    """
    from secrets import randbelow
    r = randbelow(rbound * 2 + 1) - rbound
    bn = [randbelow(2) for _ in range(len(pk) - 1)]  # which elements of public key to use (if 1 use, if 0, don't use)
    S = [pk[i + 1] for i in range(len(pk) - 1) if bn[i] == 1]  # excluding x0 from being in S
    return modifiedremainder(m + 2 * sum(S) + 2 * r, pk[0])


def LBCdecryption(c, p):
    from general_use import modifiedremainder
    return modifiedremainder(c, p) % 2
