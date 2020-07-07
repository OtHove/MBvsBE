class Node:

    label = list()
    parents = list()

    def __init__(self, label, parents=[]):
        self.label = label
        self.parents = parents

    def set_label(self, label):
        self.label = label

    def set_parents(self, parents):
        self.parents = parents

    def get_label(self):
        return self.label

    def get_parents(self):
        return self.parents
