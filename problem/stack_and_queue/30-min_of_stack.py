class MinStack():
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, node):
        self.stack.append(node)

        if self.min_stack==[] or node < self.min():
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min())

    def pop(self):
        if self.stack==[] or self.min_stack==[]:
            return None

        self.stack.pop()
        self.min_stack.pop()

    def min(self):
        return self.min_stack[-1]

if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.push(4)
    min_stack.push(2)
    min_stack.push(1)
    min_stack.pop()
    min_stack.pop()
    min_stack.push(0)
    print(min_stack.min())
