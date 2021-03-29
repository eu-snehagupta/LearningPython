import sys


def solution(array):
    sum_ = 0
    max_sum = -sys.maxsize
    for i in range(4):
        for j in range(4):
            sum_ = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] \
                   + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
            if max_sum < sum_:
                max_sum = sum_
    return max_sum


if __name__ == '__main__':
    input_data = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(solution(input_data))