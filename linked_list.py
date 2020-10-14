class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        New_node = Node(data, None)
        if self.head is None:
            self.head = New_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = New_node

    def insert_list(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def middle_ele(self):
        fast = self.head
        slow = self.head
        if self.head is not None:
            while(fast is not None and fast.next is not None):
                slow = slow.next
                fast = fast.next.next
            print(slow.data)            

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llitr = " "
        while itr:
            llitr += str(itr.data) + "-->"
            itr = itr.next
        print(llitr)


ll = LinkedList()
ll.insert_list([2,1,4,3,6])
ll.print()
ll.middle_ele()
ll.print()
          


