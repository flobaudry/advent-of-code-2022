from Rope import BigRope

def solve(inputs, size):
    big_rope = BigRope(size)
    for line in inputs.readlines():
        direction, number = line.split(' ')
        for _ in range(int(number)):
            big_rope.move(direction)
    return len(set(big_rope.get_last_history()))

def main():
    with open('inputs.txt', 'r') as f:
        print(solve(f, 2))
        f.seek(0)
        print(solve(f, 10))


if __name__ == '__main__':
    main()
