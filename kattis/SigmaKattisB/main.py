import sys
import math


def factorial(number):
    return math.factorial(number)


# returns total count of letter in each word per line,
# also returns the list of the individual count of repeated letters
# e.g count_letters("Programming") will return 6 and [2,2,2] as r,g,m are repeated twice.
def count_letters(input_data):
    letter_dictionary = {}
    list_repetition = []
    total_letter_count = 0
    for letter in input_data:
        if letter != "\n":
            total_letter_count += 1
            if letter in letter_dictionary.keys():
                letter_dictionary[letter] = letter_dictionary.get(letter) + 1
            else:
                letter_dictionary[letter] = 1

    for repetition in letter_dictionary.values():   # letter_dictionary.values() will also contain value 1
        if repetition != 1:                         # for non repeated letter, which need to be trimmed out.
            list_repetition.append(repetition)
    return total_letter_count, list_repetition


def anagram(total, repetition_list):    # using the mathematical formula
    factorial_of_total_letters = factorial(total)
    factorial_of_repeated_letters = 1
    for each_repeated_letter in repetition_list:
        factorial_of_repeated_letters = factorial_of_repeated_letters * factorial(each_repeated_letter)
    return int(factorial_of_total_letters//factorial_of_repeated_letters)  # // to manage the division of large number


if __name__ == '__main__':
    for inputLine in sys.stdin:
        total_letters, list_no_of_repetition = count_letters(inputLine)
        print(anagram(total_letters, list_no_of_repetition))