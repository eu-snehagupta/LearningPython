def binary_search(array, data):
    l= 0
    r = len(array) - 1
    while l <= r:
        m = l + (r - l) // 2
        if array[m] == data:
            return m
        elif array[m] < data:
            l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == "__main__":
    input_array = [ 2, 3, 4, 10, 40 ]
    print(binary_search(input_array, 40))
