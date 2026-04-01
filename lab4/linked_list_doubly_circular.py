from dataclasses import dataclass


@dataclass
class Node:
    key: int | None = None
    prev: "Node | None" = None
    next: "Node | None" = None


class LinkedListDoublyCircular:
    """Circular doubly linked list implementation."""

    def __init__(self, max_len: int):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.max_len = max_len

    def len(self) -> int:
        if self.head is None:
            return 0

        length = 1
        current = self.head
        while current.next is not self.head:
            current = current.next
            length += 1
        return length

    def add(self, key):
        if self.len() >= self.max_len:
            print("The circular queue is full!")
            return

        new_node = Node(key)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def remove(self):
        if self.head is None:
            print("The queue is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

    def show(self):
        if self.head is None:
            print("The queue is empty")
            return

        print("Your queue now is:")
        current = self.head
        while True:
            print(current.key)
            if current is self.tail:
                break
            current = current.next

        print("The max len of circular queue is:", self.max_len)

    def show_el(self):
        if self.head is None:
            print("The queue is empty")
            return

        print("The head.prev element of queue is:", self.head.prev.key)
        print("The tail.next element of queue is:", self.tail.next.key)

    def show_w_el(self):
        if self.head is None:
            print("The queue is empty")
            return

        try:
            k = int(input("Type element index (1-based): "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if k < 1 or k > self.len():
            print("Index out of range.")
            return

        current = self.head
        for _ in range(1, k):
            current = current.next

        print("The element:", current.key)


def main():
    a = LinkedListDoublyCircular(13)
    for i in range(14):
        a.add(i)

    a.show()
    a.remove()
    a.show()
    a.show_el()
    a.show_w_el()


if __name__ == "__main__":
    main()
