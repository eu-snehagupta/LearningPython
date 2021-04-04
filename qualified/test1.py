# params: input_string
# return: True/False
# description: A function that determines whether a string is an isogram. Assumes that an empty string is an isogram and ignores letter case

def is_isogram(input_string):
    input_string = input_string.lower()
    #returns True if the str contains unique character, otherwise False
    return len(set(input_string)) == len(input_string)   # set contains unique elements

if __name__ == '__main__':
    print(is_isogram("moOse"))
