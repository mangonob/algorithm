from introduction_of_algorithms.ch10_base_datastruct import BinaryNode
from introduction_of_algorithms.util.constant import *

import weakref


class TernaryNode(BinaryNode):
    def __init__(self, parent=NIL, *args, **kwargs):
        super(TernaryNode, self).__init__(*args, **kwargs)
        self.weak_parent = NIL

    @property
    def parent(self):
        return self.weak_parent and self.weak_parent()

    @parent.setter
    def parent(self, parent):
        self.weak_parent = parent and weakref.ref(parent)


class TreeNode(TernaryNode):
    """ General node of tree. """

    def pick(self):
        if not self.parent: return

        if self.parent.left == self:
            self.parent.left = NIL
        elif self.parent.right == self:
            self.parent.right = NIL

        self.parent = NIL


class BinarySearchTreeNode(TreeNode):
    """ TreeNode of BinarySearchTreeNode. """

    # def __del__(self):
    #     print("DEL " + str(self))

    def __str__(self):
        return "<%s: (%s (%s)  %s)>" % (self.parent and self.parent.key or "/ ", self.left and self.left.key or "/ ", self.key, self.right and self.right.key or "/ ")

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
    LEFT = 0
    RIGHT = 1

    Node = BinarySearchTreeNode

    def __init__(self):
        self.nil = self.__class__.Node()
        self._size = 0

    def insert(self, k):
        """ Insert a key into binary search tree. """
        new_node = self.__class__.Node(key=k)

        if self.is_empty:
            self.nil.left = new_node
            new_node.parent = self.nil
            self.size += 1
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

        self.size += 1

    @property
    def root(self):
        return self.nil.left

    @property
    def is_empty(self):
        return not self.root

    @property
    def minimum(self):
        if self.is_empty: return NIL
        return self.root.min

    @property
    def maximum(self):
        if self.is_empty: return NIL
        return self.root.max

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def search(self, k):
        """ Find the node containe key k. """
        if self.is_empty: return NIL

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

    def refactor(self, node, to):
        def remove_sub_tree(root):
            p = root.parent

            direction = None
            if root == p.left:
                direction = BinarySearchTree.LEFT
                p.left = NIL
            else:
                direction = BinarySearchTree.RIGHT
                p.right = NIL

            root.parent = NIL
            return p, direction

        if not node: return

        p, direction = remove_sub_tree(node)
        if not to: return

        remove_sub_tree(to)

        to.parent = p

        if direction == BinarySearchTree.LEFT:
            p.left = to
        elif direction == BinarySearchTree.RIGHT:
            p.right = to

    def remove(self, k):
        """ Remove a node contains key k from binary search tree, if success return it. """
        node = self.search(k)
        if not node:
            raise KeyError() # Can't remove a key that not exist.

        if not node.left:
            self.refactor(node, node.right)
        elif not node.right:
            self.refactor(node, node.left)
        else:
            m = node.right.min
            if m.right:
                self.refactor(m, m.right)

            m.pick()

            if node.parent.left == node:
                node.parent.left = m
            if node.parent.right == node:
                node.parent.right = m

            m.parent = node.parent
            m.left = node.left
            m.right = node.right
            if m.left: m.left.parent = m
            if m.right: m.right.parent = m

        self.size -= 1

    def __str__(self):
        return "<" + ", ".join([str(x) for x in self])+ ">"

    def __contains__(self, k):
        """ If binary search contain k. """
        pass

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        pass

    def __iter__(self):
        if self.is_empty: return

        node = self.minimum

        while node and node != self.nil:
            yield node.key
            node = node.next

