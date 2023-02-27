class Stack:
    def __init__(self):
        self.items = []

    @property
    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Tree:
    def __init__(self, name=None, parent=None, level=0):
        self.parent = parent
        self.name = name
        self.isLeaf = True
        self.level = level

    def add_chile(self, name):
        Tree(name, self.name, self.level + 1)
        self.isLeaf = False



stack = Stack()
stack.push('Red')
stack.push('Green')
stack.push('Blue')
stack.push('Yellow')
print(stack.pop())
print(stack.isEmpty)

queue = Queue()
queue.enqueue('Red')
queue.enqueue('Green')
queue.enqueue('Blue')
queue.enqueue('Yellow')
print(queue.size())
print(queue.dequeue())
print(queue.dequeue())

del stack, queue