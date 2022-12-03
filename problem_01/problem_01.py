def get_calories():
    with open('inputs.txt', 'r') as f:
        inputs = f.read()
        elves = inputs.split('\n\n')
        elves_tot = [sum([int(calories) for calories in elf.split('\n')]) for elf in elves]
        return elves_tot


def solve1():
    return max(get_calories())


def solve2():
    calories = get_calories()
    calories.sort()
    calories.reverse()
    return sum(calories[:3])


print(solve1())
print(solve2())
