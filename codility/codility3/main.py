def add_list_elements(list_of_integer, no_of_element):
    total_sum = 0
    for i in range(no_of_element):
        total_sum += list_of_integer[i]
    return total_sum


def get_first_odd_element(list_of_integer):
    for element in list_of_integer:
        if element % 2 != 0:
            return element
        else:
            return -1


def get_first_even_element(list_of_integer):
    for element in list_of_integer:
        if element % 2 == 0:
            return element
        else:
            return -1


def solution(A, K):
    if len(A) < K or len(A) == 0 or K <= 0:
        return -1  # to handle situation where K is greater than no of integers in the lists

    A.sort(reverse=True)
    even_list = []
    odd_list = []
    for i in A:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    if len(even_list) == 0 and K % 2 != 0:
        return -1       # to handle the list of odd integers

    if len(A) == K:
        if len(odd_list) % 2 == 0:
            return add_list_elements(A, K)
        else:
            return -1   # to handle the list of length = K with odd occurrence of odd numbers in the list

    if len(odd_list) <= 1:
        return add_list_elements(even_list, K)  # to handle the list of even integers or list with just 1 element as odd

    max_sum = add_list_elements(A, K)
    if max_sum % 2 == 0:
        return max_sum
    else:
        if A[K-1] % 2 == 0:
            another_element = get_first_odd_element(A[K:])
            if another_element == -1:
                return -1
            else:
                return add_list_elements(A, K-1) + another_element
        else:
            another_element = get_first_even_element(A[K:])
            if another_element == -1:
                return -1
            else:
                return add_list_elements(A, K - 1) + another_element


if __name__ == '__main__':
    input_data = [2, 3, 3, 5, 5]
    print(solution(input_data, 3))