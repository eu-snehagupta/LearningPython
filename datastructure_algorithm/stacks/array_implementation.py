from sys import maxsize


def create_stack():
    stack = []
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(str(item) + " pushed to the stack.")


def pop(stack):
    if is_empty(stack):
        return str(-maxsize - 1)
    return stack.pop()


def top(stack):
    if is_empty(stack):
        return str(-maxsize - 1)
    return stack[len(stack)-1]


if __name__ == '__main__':
    stack = create_stack()
    push(stack, 3)
    push(stack, 5)
    push(stack, 8)
    print(pop(stack))
    print(stack)

