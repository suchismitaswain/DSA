class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def remove_nth_from_end(head, N):
  
    length = 0
    curr = head
    while curr is not None:
        length += 1
        curr = curr.next

    target = length - N + 1

   
    if target == 1:
        return head.next

    curr = head
    for _ in range(target - 2):
        curr = curr.next

    curr.next = curr.next.next

    return head

def print_list(node):
    curr = node;
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
  
  
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    N = 2  
    head = remove_nth_from_end(head, N)

    print_list(head)