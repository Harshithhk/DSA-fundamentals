class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class DeQueueLinked:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def add_first(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._last = newest
        else:
            newest._next = self._first

        self._first = newest
        self._size += 1

    def add_last(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._first = newest
        else:
            self._last._next = newest

        self._last = newest
        self._size += 1

    def remove_first(self):
        if self.isempty():
            print("Queue is Empty")
            return
        e = self._first._element
        self._first = self._first._next
        self._size -= 1
        if self.isempty():
            self._last = None
        return e

    def remove_last(self):
        if self.isempty():
            print("Queue is Empty")
            return
        p = self._first
        i = 1
        while i < self._size - 1:
            p = p._next
            i += 1

        e = p._next._element

        self._last = p
        self._last._next = None
        self._size -= 1

        return e

    def display(self):
        p = self._first
        while p:
            print(p._element, end="<--")
            p = p._next
        print()

    def first(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self._first._element

    def last(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self._last._element


Q = DeQueueLinked()
Q.add_last(1)
Q.add_last(2)
Q.display()


Q.remove_first()
Q.display()

print(Q.first())

Q.remove_first()
Q.remove_first()
print(Q.first())

Q.display()

Q.add_first(2)
Q.add_first(3)
Q.add_last(1)
print(Q.last())
Q.display()
