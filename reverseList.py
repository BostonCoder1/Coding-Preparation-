# create Node structure
# pass value to node structure
# connect a Node
# reverse the node list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# a->b->C->d
# None<-a b->c ->d
def getReverse(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

   




def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    print(getReverse(a))


if __name__ == '__main__':
    main()
