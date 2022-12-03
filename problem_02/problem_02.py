def solve1():
    combinations = {('AY', 'BZ', 'CX'): 6, ('AX', 'BY', 'CZ'): 3}
    score_select = dict(X=1, Y=2, Z=3)
    return get_total_score(combinations, score_select)


def solve2():
    combinations = {('AY', 'BX', 'CZ'): 1, ('AZ', 'BY', 'CX'): 2, ('AX', 'BZ', 'CY'): 3}
    score_outcome = dict(X=0, Y=3, Z=6)
    return get_total_score(combinations, score_outcome)


def get_total_score(combinations, score_outcome):
    with open('inputs.txt', 'r') as f:
        score = 0
        for combination in f.readlines():
            combination = combination.replace('\n', '')
            combination = combination.split(' ')
            score += score_outcome[combination[1]]
            score += get_score(''.join(combination), combinations)
    return score


def get_score(combination, tests: dict):
    for key_combination, score in tests.items():
        if combination in key_combination:
            return score
    return 0


if __name__ == '__main__':
    print(solve1())
    print(solve2())
