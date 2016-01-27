# Reverse Level order tree traversal

from BinaryTree import TreeNode


def reverseLevelOrderTraversal(root):
    S = []
    Q = []

    # add first node in queue as entry point
    Q.append(root)

    while len(Q) > 0:
        root = Q.pop(0)
        S.append(root)


        # If right node, add to queue
        # Right first, since we want to pop it later as comparred to left nodes
        if root.right_node:
            Q.append(root.right_node)

        # If left node, add to queue
        if root.left_node:
            Q.append(root.left_node)


    while len(S) > 0:
        root = S.pop()
        print root.data,


if __name__ == "__main__":
    bTree = TreeNode(1)
    bTree.left_node = TreeNode(2)
    bTree.right_node = TreeNode(3)
    bTree.left_node.left_node = TreeNode(4)
    bTree.left_node.right_node = TreeNode(5)
    bTree.right_node.left_node = TreeNode(6)
    bTree.left_node.left_node.left_node = TreeNode(12)

    print "Reverse Level order traversal: ",
    reverseLevelOrderTraversal(bTree)