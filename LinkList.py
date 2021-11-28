class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class D_LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertatFirst(self, value):
        self.n = Node(value)
        i = self.head
        if i == None:
            self.head = self.n
            self.tail = self.n
        else:
            self.head.prev = self.n
            self.n.next = self.head
            self.head = self.n

    def InsertatLast(self, value):
        self.new_node = Node(value)
        i = self.head
        if i == None:
            self.head = self.new_node
            self.tail = self.new_node
        if i != None:
            self.tail.next = self.new_node
            self.new_node.prev = self.tail
            self.tail = self.new_node

    def DeleteatFirst(self):
        i = self.head
        if i is None:
            raise ("D_List is empty")
        else:
            i = i.next
            self.head = i
            i = None

    def DeleteatLast(self):
        i = self.tail
        if i is None:
            raise ("D_List is Empty")
        else:
            i = self.tail
            self.tail = self.tail.prev
            self.tail.next = None

    def Insertafter(self, element, value):
        i = self.head
        while i != None:
            if i.value == element:
                j = Node(value)
                k = i.next
                i.next = j
                j.prev = i

                j.next = k
                k.prev = j

                return j
            i = i.next

    def DeletebyValue(self, value):
        i = self.head
        while i != None:
            if i.value == value:
                j = i.prev
                k = i.next

                j.next = k
                k.prev = j
                i = None
                return self.head
            i = i.next

    def Print(self):
        i = self.head
        while i:
            print(i.value)
            i = i.next


D = D_LinkList()
D.InsertatFirst(1)
D.InsertatFirst(2)
D.InsertatFirst(3)
D.InsertatLast(4)
D.Insertafter(1, 5)
D.Print()
print("Delete methods")
D.DeleteatFirst()
D.DeleteatLast()
D.DeletebyValue(1)
D.Print()
