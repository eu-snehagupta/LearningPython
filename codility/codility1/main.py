# Correct this code by modifying at most 3 lines.
# def solution(A, X):
#     N = len(A)
#     if N == 0:
#         return -1
#     l = 0
#     r = N - 1
#     while l < r:
#         m = (l + r) // 2
#         if A[m] > X:
#             r = m - 1
#         else:
#             l = m
#     if A[l] == X:
#         return l
#     return -1


def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = m + 1
    l = (l+r)//2
    if A[l] == X:
        return l
    return -1


if __name__ == '__main__':
    input_data = [1,2,5,9,11]
    print(solution(input_data, 5))
