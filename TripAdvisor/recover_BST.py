import copy

prev = None

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if not root:
        return
    else:
        preOrder(root.left)
        preOrder(root.right)
        print root.data,
def inOrder(root):
    if not root:
        return
    else:
        inOrder(root.left)
        print root.data,
        inOrder(root.right)

def postOrder(root):
    if not root:
        return
    else:
        print root.data,
        postOrder(root.left)
        postOrder(root.right)


def correctBST(root):
    global prev
    if root:
        correctBST(root.left)
        if prev and root.data < prev.data:
            print root.data, "is smaller than",prev.data
        prev = root
        correctBST(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(20)
    prev = None
    correctBST(root)


2 5 8 10 20
2 5 20 10 8
