def decimal_to_binary(decimal_integer):
    return bin(decimal_integer).replace("0b", "")


def solution(binary_integer):
    count = 0
    max_count = 0
    for element in binary_integer:
        if element == "1":
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    return max_count


if __name__ == '__main__':
    n = int(input())
    binary_n = decimal_to_binary(n)
    print(solution(binary_n))