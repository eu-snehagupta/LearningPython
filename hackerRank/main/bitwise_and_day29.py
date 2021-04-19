def bitwiseAnd(N, K):
    max_bitwise = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            if max_bitwise < (i & j) < K:
                max_bitwise = i & j
    return max_bitwise


if __name__ == '__main__':
    print(bitwiseAnd(5, 2))
