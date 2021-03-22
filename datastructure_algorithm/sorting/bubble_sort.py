def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length):
        for j in range(array_length-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
    return array


def bubble_sorting(array):
    array_length = len(array)
    for i in range(array_length):
        swapped = False     # improves the algorithm for cases when the input array is already sorted.
        for j in range(array_length-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                print(array)
        if not swapped:
            break
    return array


if __name__ == '__main__':
    input_array = [0, 2, 4, 5, 8]
    bubble_sorting(input_array)
    for element in input_array:
        print(element, end= " ")