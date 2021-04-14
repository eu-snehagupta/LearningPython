import math


def is_prime(digit):
    if digit == 1:
        return False
    for i in range(2, int(math.sqrt(digit))+1):
        if digit % i == 0:
            return False
    return True


if __name__ == '__main__':
    data = [30, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 907]
    for i in range(len(data)):
        if is_prime(data[i]):
            print("Prime")
        else:
            print("Not prime")
