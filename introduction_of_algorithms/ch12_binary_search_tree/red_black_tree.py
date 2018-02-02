from .binary_search_tree import BinarySearchTreeNode, BinarySearchTree


class RedBlackTreeNode(BinarySearchTreeNode):
    """ Node of red-black tree. """
    BLACK = 1
    RED = 2

    def __init__(self, color=RED, *args, **kwargs):
        super(BinarySearchTreeNode, self).__init__(*args, **kwargs)
        self.color = color

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

    @property
    def is_red(self):
        return self.color == RedBlackTreeNode.RED

    @property
    def is_black(self):
        return self.color == RedBlackTreeNode.BLACK

    def __str__(self):
        return "(%s, %s%s>%s, %s)" % (self.left.key, self.parent.key or "", "=" if self.is_red else "-", self.key, self.right.key)


class RedBlackTree(BinarySearchTree):
    Node = RedBlackTreeNode
