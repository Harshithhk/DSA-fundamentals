class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class QueueLinked:
    def __init__(self):
        self._first = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._first = newest
        else:
            self._rear._next = newest

        self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is Empty")
            return
        e = self._first._element
        self._first = self._first._next
        self._size -= 1
        if self.isempty():
            self._rear = None
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


Q = QueueLinked()
Q.enqueue(1)
Q.enqueue(2)
Q.display()


Q.dequeue()
Q.display()

print(Q.first())

Q.dequeue()
Q.dequeue()
print(Q.first())

Q.display()
