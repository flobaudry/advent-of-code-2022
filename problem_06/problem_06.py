def unique(subseq):
    for i in range(len(subseq)):
        if subseq[i] in subseq[:i]:
            return False
    return True


def solve(f, code_length):
    line = f.readline()
    for i in range(len(line)-code_length):
        subseq = line[i:i+code_length]
        if unique(subseq):
            return i+code_length
    return -1

def main():
    with open('inputs.txt', 'r') as f:
        print(solve(f, 4))
        f.seek(0)
        print(solve(f, 14))


if __name__ == '__main__':
    main()
