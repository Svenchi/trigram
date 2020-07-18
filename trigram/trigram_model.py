from random import *

##TODO implement a version that takes up less space in memory,
## maybe a dictionary with probabilities of next word
class Node:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.children = []

    def add_child(self, node_child):
        if not self.model.has(node_child):
            self.model.add_node(node_child)
        self.children.append(node_child)

    def add_and_return_child_by_name(self, name):
        if self.model.name_in(name):
            child = self.model.get_node_by_name(name)
        else:
            child = Node(name, self.model)
        self.add_child(child)
        return child

    def get_random_child(self):
        if (len(self.children) == 0):
            return self.model.starting_node
        child_index = randint(0, len(self.children) - 1)
        return self.children[child_index]


class Trigram_model:
    ##TODO unhardcode starting node
    def __init__(self):
        self.starting_node = Node((".", "."), self)
        self.nodes = {(".", "."): self.starting_node}

    def start_build(self):
        return self.starting_node

    def has(self, node):
        return node.name in self.nodes

    def name_in(self, name):
        return name in self.nodes

    def get_node_by_name(self, name):
        return self.nodes[name]

    def add_node(self, node):
        self.nodes[node.name] = node