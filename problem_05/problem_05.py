import numpy as np


def move_crates9001(crates, operation):
    number, out_stack, in_stack = operation
    index = len(crates[out_stack - 1]) - number
    crates[in_stack - 1] += crates[out_stack - 1][index:]
    crates[out_stack - 1] = crates[out_stack - 1][:index]
    return crates


def move_crates(crates, operation):
    number, out_stack, in_stack = operation
    for i in range(number):
        crates[in_stack - 1].append(crates[out_stack - 1].pop())
    return crates


def get_stacks(string_stacks, max_value):
    stacks = []
    for string in string_stacks:
        stack = []
        for i in range(1, len(string), 4):
            if string[i] != '\n':
                stack.append(string[i])
        for i in range(len(stack), max_value):
            stack.append(' ')
        stacks.append(stack)
    res = np.flip(np.transpose(stacks), axis=1).tolist()
    for i in range(len(res)):
        while ' ' in res[i]:
            res[i].pop()
    return res


def display_stack(stacks):
    i = 1
    for stack in stacks:
        print(i, stack)
        i += 1
    print()


def get_message(stacks):
    message = ''
    for stack in stacks:
        message += stack[-1]
    return message


def solve(f, crate_function):
    crates = []
    line = f.readline()
    string_stacks = []
    while line[1] != '1':
        string_stacks.append(line)
        line = f.readline()
    max_value = int(line.split()[-1])
    stacks = get_stacks(string_stacks, max_value)
    f.readline()
    for line in f.readlines():
        operation = [int(digit) for digit in str.split(line) if digit.isdigit()]
        stacks = crate_function(stacks, operation)
    return get_message(stacks)


def main():
    with open('inputs.txt', 'r') as f:
        print(solve(f, move_crates))
        f.seek(0)
        print(solve(f, move_crates9001))


if __name__ == '__main__':
    main()
