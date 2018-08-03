class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.next

    def getCount(self):
        temp = self.cur_node  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    def search(self, x):
        t=self.cur_node
        if t != None:
            while t.next != None:
                if t.data == x:
                    return t
                t = t.next
            if t.data == x:
                return t
        return None


ll = linked_list()
x=int(input("Enter the number of elements for linked list:"))
for i in range(x):
    z=input("Enter the element:")
    ll.add_node(z)
ll.list_print()
search=(input("Enter the value to be searched:"))
print(ll.search(search))


        







