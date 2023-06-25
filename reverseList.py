# create Node structure
# pass value to node structure
# connect a Node 
# reverse the node list 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# a-> b -> c -> d
def getReverse(head):
    prev = None
    current = head    #a
    while current is not None:
        temp = current.next   # temp = b
        current.next = prev
        prev = current
        current = temp
    return prev.val




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


