class DeQueueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def remove_first(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self._data.pop(0)

    def remove_last(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print("Queue is Empty")
            return
        return self._data[-1]


Q = DeQueueArray()
Q.add_last(1)
Q.add_last(2)
print(Q._data)


Q.remove_first()
print(Q._data)

print(Q.first())

Q.remove_first()
Q.remove_first()
print(Q.first())

print(Q._data)

Q.add_first(2)
Q.add_first(3)
Q.add_last(1)
print(Q.last())
print(Q._data)
