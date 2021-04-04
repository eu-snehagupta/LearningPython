
# params: plan_array
# return: path_stack
# description: dirReduc method takes plan_array(type: list) and computes the optimised list of direction.
# TO-DO: Would have preferred dir_reduce as the function name. But on changing dirReduc to dir_reduce, getting error as dirReduc is being called in hidden test cases.

def dirReduc(plan_array):
    direction_map = {"NORTH":"SOUTH", "EAST":"WEST", "SOUTH":"NORTH", "WEST":"EAST"}
    path_stack = [] # maintains the optimised list of direction
    for element in plan_array:
        if len(path_stack) == 0:
            path_stack.append(element)
        elif element in direction_map:
            # find the last element in the stack and its value in direction_map
            # if the value is equal to the current element, then pop out the needless direction otherwise keep appending to the stack
            if direction_map[path_stack[-1]] == element:
                path_stack.pop()
            else:
                path_stack.append(element)
    return path_stack

if __name__ == '__main__':
    array = ["NORTH","WEST","EAST","EAST"]
    print(dirReduc(array))
