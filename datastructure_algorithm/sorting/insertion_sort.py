def insertion_sort(array):
    for i in range(len(array)-1):
        key = array[i+1]
        for j in reversed(range(i + 1)):
            if key < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array

def insertion_sorting(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

if __name__ == '__main__':
    input_array = [0, 5, 8, 4, 2]
    insertion_sort(input_array)
    for element in input_array:
        print(element, end= " ")