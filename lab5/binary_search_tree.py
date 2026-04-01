from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.twins = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print(f"Value {value} already exists in the tree")

    def print_tree(self, root=None, level=0):
        if root is None:
            root = self.root

        if root is None:
            print("There's no tree! Can't print tree")
            return

        if root.left_child is not None:
            self.print_tree(root.left_child, level + 1)

        print("   " * level, root.value)

        if root.right_child is not None:
            self.print_tree(root.right_child, level + 1)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, cur_node):
        if cur_node is None:
            return False
        if value == cur_node.value:
            return True
        if value < cur_node.value:
            return self._search(value, cur_node.left_child)
        return self._search(value, cur_node.right_child)

    def find(self, value):
        return self._find(value, self.root)

    def _find(self, value, cur_node):
        if cur_node is None:
            return None
        if value == cur_node.value:
            return cur_node
        if value < cur_node.value:
            return self._find(value, cur_node.left_child)
        return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left_child = self._delete(root.left_child, value)
        elif value > root.value:
            root.right_child = self._delete(root.right_child, value)
        else:
            if root.left_child is None:
                return root.right_child
            if root.right_child is None:
                return root.left_child

            successor = self._minimum(root.right_child)
            root.value = successor.value
            root.right_child = self._delete(root.right_child, successor.value)

        return root

    def _minimum(self, root):
        current = root
        while current.left_child is not None:
            current = current.left_child
        return current

    def post_ord(self, root):
        if root is None:
            return
        self.post_ord(root.left_child)
        self.post_ord(root.right_child)
        print(root.value)

    def count_twins(self, root, value):
        if root is None:
            return 0
        return (
            int(root.value == value)
            + self.count_twins(root.left_child, value)
            + self.count_twins(root.right_child, value)
        )

    def find_twins(self, root=None):
        if root is None:
            root = self.root

        if root is None:
            return

        self.twins = []
        self._collect_twins(root, set())

    def _collect_twins(self, root, seen_values):
        if root is None:
            return

        if root.value in seen_values:
            self.twins.append(root.value)
        else:
            seen_values.add(root.value)

        self._collect_twins(root.left_child, seen_values)
        self._collect_twins(root.right_child, seen_values)

    def erase_twins(self):
        while self.twins:
            value = self.twins.pop()
            self.delete_value(value)


def main():
    bst = BinarySearchTree()

    values = [10, 5, 15, 3, 7, 12, 18, 7, 10, 15]
    for value in values:
        bst.insert(value)

    print("Tree:")
    bst.print_tree()

    print("\nPostorder traversal:")
    bst.post_ord(bst.root)

    print("\nSearching:")
    print("Has 12?", bst.search(12))
    print("Has 99?", bst.search(99))

    print("\nDuplicates:")
    bst.find_twins()
    print(bst.twins)
    bst.erase_twins()

    print("\nTree after removing duplicates:")
    bst.print_tree()

    print("\nDeleting 10:")
    bst.delete_value(10)
    bst.print_tree()


if __name__ == "__main__":
    main()
