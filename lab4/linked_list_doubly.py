from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, key=None, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LinkedListDoubly:
    """Doubly linked list implementation."""

    def __init__(self):
        self.head = None
        self.tail = None

    def len(self) -> int:
        length = 0
        new_node = self.head
        while new_node is not None:
            length += 1
            new_node = new_node.next
        return length

    def add(self, key):
        new_node = Node(key, None, None)
        if self.head is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def show(self):
        print("Your queue now is: ")
        new_node = self.head
        while new_node is not None:
            print(new_node.key)
            new_node = new_node.next

    def show_first(self):
        if self.head is not None:
            print("The first element of queue is:", self.head.key)
        else:
            print("The queue is empty")

    def remove(self):
        if self.head is None:
            print("The queue is empty")
            return

        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None


def main():
    ll = LinkedListDoubly()

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
