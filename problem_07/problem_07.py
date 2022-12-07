from Tree import Dir, Leaf


def get_tree(f):
    file_system = Dir('/')
    working_directory = file_system
    for line in f.readlines():
        inputs = line.split()
        if inputs[0] == '$':
            if inputs[1] == 'cd':
                if inputs[2] == '/':
                    working_directory = file_system
                elif inputs[2] == '..':
                    working_directory = working_directory.get_parent()
                else:
                    working_directory = working_directory.get_sub_dir(inputs[2])
        else:
            if inputs[0] == 'dir':
                working_directory.add_sub_dir(Dir(inputs[1], working_directory))
            else:
                working_directory.add_leaf(Leaf(inputs[1], int(inputs[0])))
    return file_system


def solve1(f):
    file_system = get_tree(f)
    file_system.compute_size()
    return file_system.less_than(100000)


def find_closest(file_system, min_size):
    min_dir_size = 30000000


def solve2(f):
    file_system = get_tree(f)
    file_system.compute_size()
    target = 30000000 - (70000000 - file_system.get_size())
    return file_system.find_closest(target)


def main():
    with open('inputs.txt', 'r') as f:
        print(solve1(f))
        f.seek(0)
        print(solve2(f))


if __name__ == '__main__':
    main()
