from itertools import permutations


def countingValleys(steps, path):
    track_count = 0
    no_valley = 0
    in_valley = False
    for char in path:
        if char == "D":
            track_count -= 1
        else:
            track_count += 1
        if track_count < 0:
            in_valley = True
        if track_count == 0 and in_valley:
            no_valley += 1
            in_valley = False
    return no_valley


if __name__ == '__main__':
    print(countingValleys(12, "DDUUDDUDUUUD"))
