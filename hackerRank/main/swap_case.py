def swap_case(s):
    swapped = ""
    for element in s:
        if element.isupper():
            swapped = swapped + element.lower()
        elif element.islower():
            swapped = swapped + element.upper()
        else:
            swapped = swapped + element
    return swapped


if __name__ == '__main__':
    s = "HackerRank.com presents"
    result = swap_case(s)
    print(result)
