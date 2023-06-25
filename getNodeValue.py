# create Node structure
# pass value to Node structure
# make a node Connection 
# create a function to traverse Node and find the Index 

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def findIndex(head,target):
    current = head
    index = -1
    idx = 0
    while current is not None:
        if current.val == target:
            return idx
        current = current.next
        idx = idx+1
    return index

def findIndexRecurr(head,target, index = 0):
  
    if head is None:
        return -1
    if head.val == target:
        return index
    return findIndexRecurr(head.next,target,index = index+1)

        

def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    print(findIndex(a,'c'))
    print (findIndexRecurr(a,'e'))

if __name__ =='__main__':
    main()
