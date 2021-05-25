def bitwiseAnd(N, K):
    for k in range(K - 1, 0, -1):
        for i in range(1, N):
            for j in range(i+1, N+1):
                if (i & j) == k:
                    return k
    return 0

if __name__ == '__main__':
    print(bitwiseAnd(5, 2))
