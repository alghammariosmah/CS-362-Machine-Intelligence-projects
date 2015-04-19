"""
# Stack structure to use in DFS.

# Usage:

s = Stack()
s.push(1)
s.push(2)
s.push(3)

while not s.isEmpty():
	print s.pop()

# will print:
# 3
# 2
# 1

"""
class Stack:
    myList = []

    def push(self, newItem):
        self.myList.append(newItem)

    def pop(self):
        return self.myList.pop()

    def isEmpty(self):
        return len(self.myList) == 0
