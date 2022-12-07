class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = -1
        self.sub_dir = []
        self.leaves = []

    def add_leaf(self, leaf):
        self.leaves.append(leaf)

    def add_sub_dir(self, sub_dir):
        self.sub_dir.append(sub_dir)

    def get_sub_dir(self, name):
        for sub_dir in self.sub_dir:
            if sub_dir.name == name:
                return sub_dir
        return None

    def get_leaf(self, name):
        for leaf in self.leaves:
            if leaf.name == name:
                return leaf
        return None

    def get_parent(self):
        return self.parent

    def str_dir(self, depth=0):
        offset = depth*2*' '
        res = f'{offset}- {self.name} (dir, size={self.size if self.size != -1 else "Unknown"})\n'
        for leaf in self.leaves:
            res += f'{offset}  - {leaf.get_name()} (file, size={leaf.get_size()})\n'
        for sub_dir in self.sub_dir:
            res += sub_dir.str_dir(depth+1)
        return res

    def compute_size(self):
        self.size = 0
        for leaf in self.leaves:
            self.size += leaf.get_size()
        for sub_dir in self.sub_dir:
            self.size += sub_dir.compute_size()
        return self.size

    def less_than(self, amount):
        size = self.size if self.size <= amount else 0
        self.compute_size()
        for sub_dir in self.sub_dir:
            size += sub_dir.less_than(amount)
        return size

    def get_size(self):
        return self.size

    def find_closest(self, target):
        if self.size < target:
            return None
        else:
            choices = [self.size]
            for sub_dir in self.sub_dir:
                closest = sub_dir.find_closest(target)
                if closest is not None:
                    choices.append(closest)
            return min(choices)


class Leaf:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name
