from Node import Node


class Network:

    nodes = list()

    def __init__(self, nodes):
        self.nodes = nodes

    def set_nodes(self, nodes):
        self.nodes = nodes

    def get_network(self):
        return self.nodes

    def add_node(self, node):
        self.nodes.append(node)
