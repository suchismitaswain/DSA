class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def height(node):

    if node is None:
        return 0

    if ((node.left and node.left.right == node) and
                (node.right and node.right.left == node)):
        return 1

    return 1 + max(height(node.left), height(node.right))
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)       
    root.right.right = Node(6)      
    root.left.left.left = Node(7)  
 
    
    first = root.left.left.left
    second = root.left.right
    third = root.right.right
 
    first.left = third
    first.right = second
 
    second.left = first
    second.right = third
 
    third.left = second
    third.right = first
 
    print('The height of the binary tree is', height(root))
 