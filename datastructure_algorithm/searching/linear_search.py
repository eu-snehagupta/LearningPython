def linear_search(array, data):
    for i in range(len(array)):
        if array[i] == data:
            return i
    return -1


if __name__ == "__main__":
    input_array = [4, 5, 8, 9, 2]
    print(linear_search(input_array, 9))