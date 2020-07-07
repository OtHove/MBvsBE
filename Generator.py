from Node import Node
from Network import Network
import random


class Generator:

    @staticmethod
    def create(amount, arity):
        network = []
        for i in range(0, amount):
            Generator.add_node(network, arity)
        return Network(network)

    @staticmethod
    def add_node(network, arity):
        p_number = min(arity, len(network))
        parents = random.choices(network, k=p_number)
        label = []
        if len(parents) == 0:
            label.append({})
        for node in parents:
            if len(label) <= 1:
                label.append({node: 0})
                label.append({node: 1})
            else:
                for j in range(0, len(label)):
                    label[j][node] = 0
                    temp_label = {}
                    for key in label[j]:
                        temp_label[key] = label[j][key]
                    temp_label[node] = 1
                    label.append(temp_label)
        for row in label:
            row["label"] = random.random()
        node = Node(label, parents)
        network.append(node)
