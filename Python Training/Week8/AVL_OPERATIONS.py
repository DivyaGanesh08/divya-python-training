
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    #  Get height
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    #  Get balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    #  Right rotation (LL case)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    #  Left rotation (RR case)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    #  Insert
    def insert(self, root, key):

        # Step 1: BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get balance
        balance = self.get_balance(root)

        # Step 4: Balance cases

        # LL
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    #  Get minimum node
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    #  Delete
    def delete(self, root, key):

        # Step 1: BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Node with 1 or 0 child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with 2 children
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Step 2: Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3: Get balance
        balance = self.get_balance(root)

        # Step 4: Balance cases

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    #  Search
    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    #  Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# =========================
#  Example Usage
# =========================

if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Insert values
    values = [10, 20, 30, 40, 50, 25]
    for v in values:
        root = avl.insert(root, v)

    print("Inorder Traversal:")
    avl.inorder(root)

    print("\nPreorder Traversal:")
    avl.preorder(root)

    # Search
    key = 25
    result = avl.search(root, key)
    print("\nSearch 25:", "Found" if result else "Not Found")

    # Delete
    root = avl.delete(root, 30)
    print("\nInorder after deleting 30:")
    avl.inorder(root)