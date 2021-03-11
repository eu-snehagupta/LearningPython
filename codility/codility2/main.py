def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            result = 1
    return result


if __name__ == '__main__':
    input_array = [100, 63, 1, 6, 2, 13]
    print(solution(100, 63, input_array))
