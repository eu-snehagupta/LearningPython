def count_substring(string, sub_string):
    occurences = 0
    while len(string) > len(sub_string):
        if string.find(sub_string) != -1:
            occurences = occurences + 1
            string = string[string.find(sub_string)+1:]
        else:
            break
    return occurences


if __name__ == '__main__':
    # count = count_substring("ABCDCDC", "CDC")
    count = count_substring("ABCDCDCABCDCDC", "CDC")
    print(count)