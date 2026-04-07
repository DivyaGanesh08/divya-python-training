class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    # SEARCH
    def search(self, root, key):
        if root is None or root.value == key:
            return root

        if key < root.value:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # FIND MIN (for delete)
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # DELETE
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 2: Two children
            successor = self.find_min(root.right)
            root.value = successor.value
            root.right = self.delete(root.right, successor.value)

        return root

    # HEIGHT
    def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    # CHECK BALANCED
    def is_balanced(self, root):
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)


# ---------------- MAIN ----------------

bst = BST()

values = [10, 5, 15, 2, 7, 20]

for v in values:
    bst.root = bst.insert(bst.root, v)

# SEARCH
result = bst.search(bst.root, 7)
print("Found" if result else "Not Found")

# DELETE
bst.root = bst.delete(bst.root, 5)

# HEIGHT
print("Height:", bst.height(bst.root))

# BALANCED CHECK
print("Balanced:", bst.is_balanced(bst.root))