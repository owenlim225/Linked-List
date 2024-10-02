# Limosnero, Sherwin P.
# J2S
# Activity #1M - Linked List module 3.1

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
        

class doublelinkedlist:
    def __init__(self):
        self.start_node = None
    
    
    def searchElement(self, searchValue):
       temp = self.headVal 
       found = 0
       i = 0

       if (temp != None):
           while (temp != None):
               i += 1
               if (temp.dataVal == searchValue):
                   found += 1
                   break
               temp = temp.nextVal
               
            if (found == 1):
                print(searchValue, "is found at index = ", i)
            else:
                print(searchValue, "is not found in the list.")
    
    
    def deleteNode(self, key):
        temp = self.head
        if (temp is not Node):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        
        prev.next = temp.next
        temp = None
    
    
    def insertToEmptyList(self, data):
        if self.start_node is None:
            newNode = Node(data)
            self.start_node = newNode
        else:
            print("\nThe list is empty.")
    
    
    def insertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            newNode = Node(data)
            self.start_node = newNode
            return
        n = self.start_node
        
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        newNode = Node(data)
        n.next = newNode
        newNode.prev = n
            
            
    # Delete the element from the start
    def deleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete.")        
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None
    
    def deleteAtEnd(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete.")        
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
        
    def display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print()
    
    
    
    

        

list1 = doublelinkedlist()
list1.headVal = Node("Data")
s2 = Node("Structure")
s3 = Node("Data")
s4 = Node("Mining")
s5 = Node("Data")
s6 = Node("Cleaning")
s7 = Node("Game")
s8 = Node("Development")

list1.headVal.nextVal = s2
s2.nextVal = s2
s3.nextVal = s3
s4.nextVal = s4
s5.nextVal = s5
s6.nextVal = s6 
s7.nextVal = s7
s8.nextVal = s8

list1.printList()
a = input("Search: ")

list1.searchElement(a)
