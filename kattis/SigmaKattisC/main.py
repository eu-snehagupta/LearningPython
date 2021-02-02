import sys
from itertools import chain, combinations


def find_possible_set(iterable):
    new_iterable = []
    for i in iterable:
        if not(i in new_iterable):
            new_iterable.append(i)
    return chain.from_iterable(combinations(new_iterable, r) for r in range(len(new_iterable)+1))


def find_xor_sum(combination):
    x_sum = combination[0]
    for i in range(1, len(combination)):
        x_sum = x_sum ^ combination[i]
    return x_sum


def find_xor_of_possible_subset(number_list):
    xor_sum_list = []
    subsets = []
    for i, item in enumerate(find_possible_set(number_list)):
        if len(item) > 1:
            subsets.append(item)
    for each_combination in subsets:
        xor_sum_list.append(find_xor_sum(list(each_combination)))
    return xor_sum_list


def find_max_xor_sum(list_of_numbers):
    list_of_xor_sum = find_xor_of_possible_subset(list_of_numbers)
    return max(list_of_xor_sum)
    #return max(list_of_numbers)


if __name__ == '__main__':
    inputFile = open("sample.in", "r")
    input_data = inputFile.readlines()
    # input_data = sys.stdin.readlines()
    input_list = input_data[1]
    input_list = list(map(int, input_list.split()))
    print(find_max_xor_sum(input_list))
