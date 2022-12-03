def solve1(inputs):
    score = 0
    for rucksack in inputs.readlines():
        rucksack = rucksack.replace('\n', '')
        mid_length = int(len(rucksack)/2)
        error_letter = list(set(rucksack[:mid_length]) & set(rucksack[mid_length:]))[0]
        score += get_priority(error_letter)
    return score


def solve2(inputs):
    score = 0
    acc = []
    for rucksack in inputs.readlines():
        rucksack = rucksack.replace('\n', '')
        acc.append(rucksack)
        if len(acc) == 3:
            badge = (set(acc[0]) & set(acc[1]) & set(acc[2])).pop()
            score += get_priority(badge)
            acc = []
    return score


def get_priority(letter):
    if letter.isupper():
        return ord(letter)-38
    return ord(letter)-96


def main():
    with open('inputs.txt', 'r') as f:
        print(solve1(f))
        f.seek(0)
        print(solve2(f))


if __name__ == '__main__':
    main()
