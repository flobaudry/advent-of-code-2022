class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_forest(inputs):
    forest = []
    for line in inputs.readlines():
        forest.append([int(x) for x in line if x.isdigit()])
    return forest


def find_trees(trees, i, j, res):
    max_value = -1
    if i is not None:
        max_value = -1
        for j in range(len(trees)):
            if trees[j] > max_value:
                res.add((i, j))
                max_value = trees[j]
        max_value = -1
        for j in range(len(trees)-1, -1, -1):
            if trees[j] > max_value:
                res.add((i, j))
                max_value = trees[j]
    else:
        max_value = -1
        for i in range(len(trees)):
            if trees[i] > max_value:
                res.add((i, j))
                max_value = trees[i]
        max_value = -1
        for i in range(len(trees)-1, -1, -1):
            if trees[i] > max_value:
                res.add((i, j))
                max_value = trees[i]

    return res


def print_forest(forest, res):
    lines = ""
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            if (i, j) in res:
                lines += bcolors.OKGREEN + str(forest[i][j]) + bcolors.ENDC
            else:
                lines += str(forest[i][j])
        lines += '\n'
    print(lines)


def solve1(inputs):
    forest = get_forest(inputs)
    res = set()
    for i in range(len(forest)):
        res = find_trees(forest[i], i, None, res)
    for j in range(len(forest[0])):
        trees_line = [x[j] for x in forest]
        res = find_trees(trees_line, None, j, res)
    print_forest(forest, res)
    return len(res)


def get_distance(line):
    current_val = line[0]
    distance = 1
    while distance < len(line)-1 and line[distance] < current_val:
        distance += 1
    return distance

def get_score(i, j, forest):
    score = 1
    line = [x[j] for x in forest]
    score *= get_distance(forest[i][j:])
    score *= get_distance(list(reversed(forest[i][:j+1])))
    score *= get_distance(line[i:])
    score *= get_distance(list(reversed(line[:i+1])))
    return score

def solve2(inputs):
    max_score = 0
    forest = get_forest(inputs)
    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[i])-1):
            score = get_score(i, j, forest)
            if score > max_score:
                max_score = score
                print(i, j, max_score)
    return max_score

def main():
    with open('inputs.txt', 'r') as f:
        print(solve1(f))
        f.seek(0)
        print(solve2(f))


if __name__ == '__main__':
    main()
