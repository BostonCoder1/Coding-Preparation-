# create data structure
# pass value
# iteration

# create data structure

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


# do recursivley

def getSumrecurr(head):
    if head is None:
        return
    current = head.val
    sum += current
    getSumrecurr(head.next)

# itterative version
def getsum(head):
   sum = 0
   current = head
   while current is not None:
       sum += current.val
       current = current.next

   return sum

def main():
    a = Node(1)
    b = Node(3)
    c = Node(4)

    a.next = c
    c.next = b
    print(getsum(a))

if __name__ == '__main__':
    main()


    
