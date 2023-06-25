# create a linkedlist data structure
# create a data structure which has value and node.
# pass each node in the data structure.
# make a link by creating a function.

# create a data structure which has value and node.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# make a link by creating a function.
def linked_list_values(head):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output

def main():
    # pass each node in the data structure.
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    values = linked_list_values(a)
    print(values)  # Output: ['a', 'b', 'c', 'd']

if __name__ == '__main__':
    main()
