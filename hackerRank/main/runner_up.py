# if __name__ == "__main__":
#     input_array = [2,8]
#     input_array.sort()
#     runner_up = input_array[-1]
#     for i in range(len(input_array)-2,-1,-1):
#         if input_array[i] < runner_up:
#             runner_up = input_array[i]
#             break
#     print(runner_up)
if __name__ == "__main__":
    input_array = [2,8]
    runner_up = max(input_array)
    while max(input_array) == runner_up:
        input_array.remove(max(input_array))
    print(max(input_array))





