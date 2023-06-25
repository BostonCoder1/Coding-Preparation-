# create Node structure
# create a Node a,b,c,d
# connect Node
# traverse Node 
# Find Node

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def findNode(head,target):
   
    current = head

    while current is not None:
        if(target==current.val):
            return True
        current = current.next
        
    return False
def findNoderecur(head,target):
    if head is None:
        return False
   
    if head.val == target:
        return True
    return findNoderecur(head.next,target)


def main():

    a = Node('a')
    b = Node('b')
    c= Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    print(findNode(a,'c'))
    print(findNoderecur(a,'b'))

if __name__== "__main__":
    main()




