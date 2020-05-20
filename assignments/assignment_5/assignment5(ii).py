#Task 2:
#Find the fourth highest  and second lowest number in below list-

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    grater_than = []
    less_than = []
    for items in sequence:
        if items > pivot:
            grater_than.append(items)
        else:
            less_than.append(items)
    return quick_sort(less_than) + [pivot] + quick_sort(grater_than)

if __name__ == "__main__":
    arr = [45, 67, 23, 43, 25, 45, 54, 89, 67, 56]
    sorted_arr = quick_sort(arr)
    print("Unsorted sequence: ", arr)
    print("Sorted sequence: ", sorted_arr)
    print("Fourth highest element: ", sorted_arr[len(arr)-3])
    print("Second lowest element: ", sorted_arr[1])