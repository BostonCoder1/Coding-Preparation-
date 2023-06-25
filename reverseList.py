# create Node structure
# pass value to node structure
# connect a Node 
# reverse the node list 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# a->b->None 
# b->a->None
def getReverse(head):
    prev = None
    current = head
    while current is not None:
        next = current.next  #b
        current.next = prev  # None
        prev = current       # a
        current = next       # b




def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    print(getReverse(a))
if __name__ =='__main__':
    main()


