import textwrap


def wrap(string, max_width):
    wrapped_string = ""
    current_width = max_width
    for element in string:
        if current_width > 0:
            # print(element,end="")
            wrapped_string = wrapped_string + element
            current_width = current_width - 1
        else:
            # print("\n" +element)
            wrapped_string = wrapped_string + "\n" + element
            current_width = max_width - 1
    return wrapped_string


if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    print(wrap(string, max_width))