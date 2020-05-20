
def solution(input,target):
    lenght = len(input)
    for i in range(0, lenght):
        if input[i] + input[i + 1] == target:
            return i, i+1
        else:
            i = i+1

if __name__ == "__main__":
    input = [0, 1, 2, 7, 11, 15]
    target = 9
    indice1, indice2 = solution(input, target)
    print(indice1, indice2)
