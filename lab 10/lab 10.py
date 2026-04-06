#Задание 1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Задание 2
root = Node(20)
root.left = Node(10)
root.right = Node(30)

root.left.left = Node(5)
root.left.right = Node(15)

root.right.left = Node(25)
root.right.right = Node(35)

print("Корень:", root.value)
print("Левый потомок:", root.left.value)
print("Правый потомок:", root.right.value)

#Задание 3
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

#Задание 4
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

#Задание 5
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

#Задание 6
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

#Задание 7
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

#Задание 8
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

#Задание 9
def search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    return search(node.left, value) or search(node.right, value)

#Задание 10
root = Node(20)
root.left = Node(10)
root.right = Node(30)

root.left.left = Node(5)
root.left.right = Node(15)

root.right.left = Node(25)
root.right.right = Node(35)

print("Preorder:")
preorder(root)
print("\n")

print("Inorder:")
inorder(root)
print("\n")

print("Postorder:")
postorder(root)
print("\n")

print("Количество узлов:", count_nodes(root))
print("Количество листьев:", count_leaves(root))
print("Высота дерева:", tree_height(root))

print("Поиск 15:", search(root, 15))
print("Поиск 100:", search(root, 100))
