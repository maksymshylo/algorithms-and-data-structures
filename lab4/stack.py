class Stack:
    """Stack implementation."""

    def __init__(self, max: int):
        self.items = []
        self.max = max

    def is_empty(self):
        if len(self.items) == 0:
            print("The stack is empty!")
        else:
            print("The stack is NOT empty!")

    def is_full(self):
        if len(self.items) == self.max:
            print("The stack is FULL!")
        else:
            print("The stack is NOT FULL")

    def push(self, item):
        if len(self.items) < self.max:
            self.items.append(item)
        else:
            print("Stack is full, cannot add any new value!")

    def show_last(self):
        if len(self.items) == 0:
            print("Stack is EMPTY!")
        else:
            print("The last item is: ", self.items[-1])

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty, nothing to pop!")
        else:
            print("Deleting item: ", self.items[-1])
            self.items.remove(self.items[-1])

    def show(self):
        for _items in reversed(self.items):
            print(_items)
        print("Length of the stack is:", len(self.items))


def main():
    s = Stack(11)
    s.is_empty()
    for i in range(0, 7):
        s.push(i)
    s.show()
    print(" ")
    s.pop()
    s.show()


if __name__ == "__main__":
    main()
