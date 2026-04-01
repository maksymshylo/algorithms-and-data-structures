class Queue:
    """Queue implementation."""

    def __init__(self, max: int):
        self.items = []
        self.max = max

    def is_empty(self):
        if len(self.items) == 0:
            print("The Queue is empty!")
        else:
            print("The Queue is NOT empty!")

    def is_full(self):
        if len(self.items) == self.max:
            print("The Queue is FULL!")
        else:
            print("The Queue is NOT FULL")

    def add(self, item):
        if len(self.items) < self.max:
            self.items.insert(0, item)
        else:
            print("Queue is full, cannot add any new value!")

    def show_first(self):
        if len(self.items) == 0:
            print("Queue is EMPTY!")
        else:
            print("The first item is: ", self.items[-1])

    def remove(self):
        if len(self.items) == 0:
            print("Queue is empty, nothing to pop!")
        else:
            print("Deleting item: ", self.items[-1])
            self.items.remove(self.items[-1])

    def show(self):
        for items in self.items:
            print(items)
        print("Length of the Queue is:", len(self.items))


def main():
    q = Queue(10)
    for i in range(0, 4):
        q.add(i)
    print(" ")
    q.show()
    print(" ")
    q.show_first()
    print(" ")
    q.remove()
    print(" ")
    q.show()
    print(" ")
    q.show_First()


if __name__ == "__main__":
    main()
