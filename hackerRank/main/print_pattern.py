# def print_pattern():
#     for i in range(1, 4):
#         for j in range(i, i+1):
#             print("*"*j)

def print_pattern():
    for i, j in zip(range(2, -1, -1), range(1, 6, 2)):
        print(" "*i + "*"*j)


if __name__ == "__main__":
    print_pattern()


    #  *
    # ***
    #*****