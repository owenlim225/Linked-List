# Limosnero, Sherwin P.
# J2S
# Activity #1M - Linked List module 3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printList(self):
        printMoko = self.head
        while printMoko is not None:
            print(printMoko.data)
            printMoko = printMoko.next
            
    def athead(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode
    
    def atend(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode
        
    def inpos(self, newElement, position):
        newNode = Node(newElement)
        if (position <= 1):
            print("\nposition should be >= 1")
        elif (position == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position-1):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("List is null.")

        

list1 = linkedlist()
list1.head = Node("Data")
e2 = Node("Structure")
e3 = Node("Python")

list1.head.next = e2
e2.next = e3

position = int(input("\nWhere to insert Data, please indicate position number: "))
data ="Stack"

list1.athead("Welcome To")
list1.atend("LinkedList")
list1.inpos(data, position)
list1.printList()
