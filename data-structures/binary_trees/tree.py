class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        """Search for a specific node in a tree using binary search.
           Uses recursion
        Rules:
        :param target: the node to be searched
        :return: the target node
        """

        if self.data == target:
            print("Found it")
            return self

        if self.left and self.data > target:
            print(f"left: {self.data}")
            return self.left.search(target)

        if self.right and self.data < target:
            print(f"right:{self.data}")
            return self.right.search(target)

        print("Value is not in tree")

    def transverse_pre_order(self):
        print(self.data)
        if self.left:
            self.left.transverse_pre_order()
        if self.right:
            self.right.transverse_pre_order()

    def transverse_in_order(self):
        if self.left:
            self.left.transverse_pre_order()
        print(self.data)
        if self.right:
            self.right.transverse_pre_order()

    def transverse_post_order(self):
        if self.left:
            self.left.transverse_pre_order()
        if self.right:
            self.right.transverse_pre_order()
        print(self.data)

    def height(self, h=0):
        left_height = self.left.height(h+1) if self.left else h
        right_height = self.right.height(h+1) if self.right else h

        return max(left_height, right_height)

    def get_nodes_at_depth(self, depth, nodes=[]):
        if nodes is None:
            nodes = []
        if depth == 0:
            nodes.append(self.data)
            return nodes
        if self.left:
            self.left.get_nodes_at_depth(depth-1, nodes)
        if self.right:
            self.right.get_nodes_at_depth(depth-1, nodes)
        return nodes


class Tree:
    def __init__(self, root, name=""):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def transverse_pre_order(self):
        return self.root.transverse_pre_order()

    def transverse_in_order(self):
        return self.root.transverse_in_order()

    def transverse_post_order(self):
        return self.root.transverse_post_order()

    def height(self):
        return self.root.height()

    def get_nodes_at_depth(self, depth):
        return self.root.get_nodes_at_depth(depth)
