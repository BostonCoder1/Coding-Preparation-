# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def checkUnique(head):
    currentNode = head
    while currentNode is not None:
        if currentNode.val != head.val:
            return False
        currentNode = currentNode.next
        
    return True

def recurr(head, prev_val):
  if head is None:
    return True
  if head.val == prev_val:
    return True
  if head.val != prev_val:
     return False
  return recurr(head.next, head.val)



def main():
    a = Node(7)
    b = Node(7)
    c = Node(7)
    d = Node(7)
    
    a.next = b
    b.next = c
    c.next = d

    print(checkUnique(a))
    print(recurr(a,7))

if __name__ =='__main__':
    main()



