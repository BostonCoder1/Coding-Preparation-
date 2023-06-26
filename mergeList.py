
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def mergeSort(list1,list2):
    dummy_head = Node(None)
    tail = dummy_head
    current1 = list1
    current2 = list2

    while current1 is not None and current2 is not None:
        if current1.val<current2.val:
            tail.next = current1
           
            current1 = current1.next
        else:
            tail.next = current2
    
            current2 = current2.next
        tail = tail.next
    

    if current1 is not None:
        tail.next = current1
        
    if current2 is not None:
        tail.next = current2
      

    current4 = dummy_head.next
    while current4 is not None:
       print(current4.val)
       current4 = current4.next



def main():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25
    # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
    mergeSort(a,q)

if __name__ =='__main__':
    main()

    