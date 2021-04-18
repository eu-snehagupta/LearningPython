def library_fine_calculator(returned_date, due_date):
    if returned_date[2] > due_date[2]:
        return 10000
    elif returned_date[1] > due_date[1] and returned_date[2] == due_date[2]:
        return 500 * (returned_date[1] - due_date[1])
    elif returned_date[0] > due_date[0] and returned_date[2] == due_date[2] and returned_date[1] == due_date[1]:
        return 15 * (returned_date[0] - due_date[0])
    return 0


if __name__ == '__main__':
    # returned_date = list(map(int, input().split(" ")))
    # due_date = due_date = list(map(int, input().split(" ")))

    returned_date = [9, 6, 2015]
    due_date = [6, 6, 2015]

    print(library_fine_calculator(returned_date, due_date))