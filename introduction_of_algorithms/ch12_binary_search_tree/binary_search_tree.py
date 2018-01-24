from introduction_of_algorithms.ch10_base_datastruct import BinaryNode
from introduction_of_algorithms.util.constant import *

class TernaryNode(BinaryNode):
    def __init__(self, key=None, left=NIL, right=NIL, parent=NIL):
        super(TernaryNode, self).__init__(key=key, left=left, right=right)
        self.parent = NIL


class TreeNode(TernaryNode):
    """ General node of tree. """
    pass


class BinaryTreeNode(TreeNode):
    """ TreeNode of BinaryTreeNode. """
    @property
    def min(self):
        """ Return the most left node. """
        node = self

        while node.left:
            node = node.left

        return node

    @property
    def max(self):
        """ Return the most right node. """
        node = self

        while node.right:
            node = node.right

        return node

    @property
    def next(self):
        """ Return successor of a node. """
        node = self

        if node.right:
            return self.right.min

        parent = node.parent

        while parent and node:
            if parent.left == node:
                return parent
            node = parent
            parent = parent.parent

        return NIL

    @property
    def prev(self):
        """ Return predecessor of a node. """
        node = self

        if node.left:
            return self.left.max

        parent = node.parent

        while parent and node:
            if parent.right == node:
                return parent
            node = parent
            parent = parent.parent

        return NIL


class BinarySearchTree(TernaryNode):
    def __init__(self):
        self.root = NIL

    def insert(self, k):
        """ Insert a key into binary search tree. """
        new_node = BinaryTreeNode(key=k)

        if not self.root:
            self.root = new_node
            return

        curr = self.root

        while True:
            if k <= curr.key and curr.left:
                curr = curr.left
            elif k <= curr.key and not curr.left:
                curr.left = new_node
                new_node.parent = curr
                break
            elif k >= curr.key and curr.right:
                curr = curr.right
            elif k >= curr.key and not curr.right:
                curr.right = new_node
                new_node.parent = curr

                break

    def search(self, k):
        """ Find the node containe key k. """
        if not self.root: return NIL

        curr = self.root
        while curr:
            if k == curr.key:
                return curr
            elif k < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        else:
            return NIL

    def pop(self, k):
        """ Remove a node contains key k from binary search tree, if success return it. """
        node = self.search(k)
        if not node: return NIL

        print(node.parent)

    def __str__(self):
        return "<" + ", ".join([str(x) for x in self])+ ">"

    def __contains__(self, k):
        """ If binary search contain k. """
        pass

    @staticmethod
    def _iter_sub_tree(root):
        if not root: return

        for x in BinarySearchTree._iter_sub_tree(root.left): yield x
        yield root.key
        for x in BinarySearchTree._iter_sub_tree(root.right): yield x

    def __iter__(self):
        for x in BinarySearchTree._iter_sub_tree(self.root): yield x
