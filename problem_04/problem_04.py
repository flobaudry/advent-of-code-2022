def overlap(elves):
    return elves[0][0] <= elves[1][1] and elves[1][0] <= elves[0][1]


def is_contain(elf1, elf2):
    return elf1[0] <= elf2[0] and elf2[1] <= elf1[1]


def intersect(elves):
    res = False
    for i in range(2):
        res = res or is_contain(elves[i % 2], elves[(i + 1) % 2])
    return res


def solve(inputs, test_function):
    pairs = 0
    for line in inputs.readlines():
        elves = line.split(',')
        for i in range(2):
            elves[i] = [int(x) for x in elves[i].split('-')]
        if test_function(elves):
            pairs += 1
    return pairs


def main():
    with open('inputs.txt', 'r') as f:
        print(solve(f, intersect))
        f.seek(0)
        print(solve(f, overlap))


if __name__ == '__main__':
    main()
