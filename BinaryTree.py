class Node:
    value = 0
    left = None
    right = None

    def __init__(self, value):
        self.value = value


class Tree:
    root = None

    def __init__(self, rootval):
        self.root = rootval

    def addNode(self, nodeToAdd, root):
        if nodeToAdd.value <= root.value:
            if root.left is None:
                root.left = nodeToAdd
            else:
                self.addNode(nodeToAdd, root.left)
        else:
            if root.right is None:
                root.right = nodeToAdd
            else:
                self.addNode(nodeToAdd, root.right)

    def removeNode(nodeToRemove):
        print "placeholder"

    def preorder(self, root):
        if root is None:
            return
        print root.value
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.preorder(root.left)
        print root.value
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        print root.value


def main():
    listNodes = [Node(10), Node(12), Node(13), Node(9), Node(16), Node(22),
                 Node(99), Node(101), Node(22), Node(1), Node(33), Node(2),
                 Node(3), Node(4), Node(5), Node(22), Node(55), Node(6)]

    tree = Tree(listNodes[0])
    for i in range(1, len(listNodes)):
        tree.addNode(listNodes[i], tree.root)

    print "Preorder\n"
    print "----------"
    tree.preorder(tree.root)
    print "----------"
    print "Inorder\n"
    print "----------"
    tree.inorder(tree.root)
    print "----------"
    print "Postorder\n"
    print "----------"
    tree.postorder(tree.root)
    print "----------"

main()
