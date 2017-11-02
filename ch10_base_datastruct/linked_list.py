class BinaryNode(object):
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right


class LinkedListNode(BinaryNode):
    @property
    def prev(self):
        return self.left

    @prev.setter
    def prev(self, value):
        self.left = value

    @property
    def next(self):
        return self.right

    @next.setter
    def next(self, value):
        self.right = value


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.nil = LinkedListNode()
        self.nil.prev = self.nil
        self.nil.next = self.nil

    @property
    def isEmpty(self):
        return self.nil.next == None

    def append(self, key):
        """ Append a node that has the key to linked list. """
        self.insert(key, len(self))

    def _validate_index(predicate = lambda x, y: x < y):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if not predicate(args[1], len(args[0])):
                    raise IndexError
                return func(*args, **kwargs)
            return wrapper
        return decorator

    def insert(self, key, position=0):
        """ Inset a node that has the key into specific position. """
        if position > len(self) or position < 0:
            raise  IndexError

        curr = self.nil

        for _ in range(0, position):
            curr = curr.next

        new_node = LinkedListNode(key=key)

        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

        self.length += 1


    def __len__(self):
        return self.length

    @_validate_index()
    def __setitem__(self, index, key):
        """ Set item for linked list, if key equal to length of linked list, a new node will be append. """
        curr = self.nil

        for i in range(0, index + 1):
            curr = curr.next

        curr.key = key

    @_validate_index()
    def __getitem__(self, index):
        """ Get an item by index. """
        curr = self.nil

        for i in range(0, index + 1):
            curr = curr.next

        return curr.key

    @_validate_index()
    def __delitem__(self, index):
        """ Remove an item by index. """
        curr = self.nil

        for i in range(0, index):
            curr = curr.next

        curr.next = curr.next.next
        curr.next.prev = curr

    def __str__(self):
        return "<" + ", ".join([str(x) for x in self]) + ">"

    def __contains__(self, item):
        for x in self:
            if item == x: return True
        else:
            return False
