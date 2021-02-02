import sys


def most_likely_outcomes(n, m):
    array_of_no_of_faces = [n, m]
    array_of_no_of_faces.sort()     # in order to get the lowest to highest value
    for i in range(array_of_no_of_faces[0] + 1, array_of_no_of_faces[1] + 2):
        print(i)


if __name__ == '__main__':
    for inputLine in sys.stdin:
        input_data = inputLine.split()
        number_of_faces_dice1 = int(input_data[0])
        number_of_faces_dice2 = int(input_data[1])
        most_likely_outcomes(number_of_faces_dice1, number_of_faces_dice2)
