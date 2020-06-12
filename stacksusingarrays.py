class Stack():

    def __init__(self):
        self.data = {}
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def push(self,item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        del self.data[self.length-1]
        self.length -= 1
        return self.data

    def peek(self):
        return self.data[self.length-1]

m = Stack()
m.push(10)
m.push(11)
m.push(12)
m.push(13)
m.push(14)
m.pop()
print(m.peek())
print(m)