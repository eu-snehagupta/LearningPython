def selection_sort(array):
    for i in range(len(array)-1):
        minimum = min(array[i:])            # time complexity of min function is n
        minimum_index = array.index(minimum)
        array[i], array[minimum_index] = array[minimum_index], array[i]
    return array


if __name__ == '__main__':
    input_array = [0, 5, 8, 4, 2]
    selection_sort(input_array)
    for element in input_array:
        print(element, end= " ")

