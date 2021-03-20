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
    return stack[-1]


if __name__ == '__main__':
    s = create_stack()
    push(s, 3)
    push(s, 5)
    push(s, 8)
    print("Popped: ", pop(s))
    print("Print stack: ", s)
    print("Peek: ", top(s))


