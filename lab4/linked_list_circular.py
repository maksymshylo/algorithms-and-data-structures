from dataclasses import dataclass


@dataclass
class Node:
    key: int | None = None
    next: "Node | None" = None


class LinkedListCircular:
    """Circular linked list buffer implementation."""

    def __init__(self):
        self.head = None
        self.tail = None

    def len(self) -> int:
        length = 0
        if self.head is not None:
            new_node = self.head
            length += 1
            while new_node.next is not self.head:
                new_node = new_node.next
                length += 1
        return length

    def add(self, key):
        new_node = Node(key)

        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def show(self):
        if self.head is None:
            print("Your queue is empty")
            return

        print("Your queue now is:")
        new_node = self.head
        while new_node is not self.tail:
            print(new_node.key)
            new_node = new_node.next
        print(self.tail.key)

    def show_first(self):
        if self.head is not None:
            print("The first element of queue is:", self.head.key)
        else:
            print("The queue is empty")

    def remove(self):
        if self.head is None:
            print("The queue is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head


def main():
    ll = LinkedListCircular()

    for i in range(0, 11):
        ll.add(i)

    ll.show()
    print("The size of your queue now is:", ll.len())
    ll.show_first()

    print("Removing the first element of queue:")
    ll.remove()

    ll.show()
    ll.show_first()


if __name__ == "__main__":
    main()
