from .binary_search_tree import BinarySearchTreeNode, BinarySearchTree


class RedBlackTreeNode(BinarySearchTreeNode):
    """ Node of red-black tree. """
    BLACK = 0
    RED = 1

    def __init__(self, color=BLACK, *args, **kwargs):
        super(BinarySearchTreeNode, self).__init__(*args, **kwargs)
        self.color = RedBlackTreeNode.BLACK

    def left_rotate(self):
        if self.parent:
            if self.parent.left == self:
                self.parent.left = self.right
            elif self.parent.right == self:
                self.parent.right = self.right

        self.right.parent = self.parent

        right = self.right

        self.right.left.parent = self
        self.right = right.left

        right.left = self
        self.parent = right

    def right_rotate(self):
        if self.parent:
            if self.parent.left == self:
                self.parent.left = self.left
            elif self.parent.right == self:
                self.parent.right = self.left

        self.left.parent = self.parent

        left = self.left

        self.left.right.parent = self
        self.left = left.right

        left.right = self
        self.parent = left


class RedBlackTree(BinarySearchTree):
    Node = RedBlackTreeNode
