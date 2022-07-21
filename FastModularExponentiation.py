def fme(A, B, C):
    answer = 1
    lastpower = A % C

    binarystr = "{0:b}".format(B)

    for k in range(-1, -1 * (len(binarystr) + 1), -1):
        if binarystr[k] == '1':
            answer = (lastpower * answer) % C
        lastpower = (lastpower ** 2) % C

    return answer


if __name__ == '__main__':
    import sys
    a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    print(fme(a, b, c))