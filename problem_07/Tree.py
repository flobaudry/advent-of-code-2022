class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
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
        offset =  depth*2*' '
        res = f'{offset}- {self.name} (dir)\n'
        for leaf in self.leaves:
            res += f'{offset}  - {leaf.get_name()} (file, size={leaf.get_size()})\n'
        for sub_dir in self.sub_dir:
            res += sub_dir.str_dir(depth+1)
        return res


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
