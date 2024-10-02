# Limosnero, Sherwin P.
# J2S
# Activity #1M - Linked List module 3.1

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.start_node = None

    def searchElement(self, searchValue):
        temp = self.start_node
        found = 0
        i = 0

        while temp is not None:
            i += 1
            if temp.item == searchValue:
                found += 1
                break
            temp = temp.next
            
        if found == 1:
            print(searchValue, "is found at index =", i)
        else:
            print(searchValue, "is not found in the list.")

    def deleteNode(self, key):
        temp = self.start_node
        if temp is None:
            return
        if temp.item == key:
            self.start_node = temp.next
            if self.start_node is not None:
                self.start_node.prev = None
            return
        while temp is not None:
            if temp.item == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return

        prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = prev
        temp = None

    def insertToEmptyList(self, data):
        if self.start_node is None:
            newNode = Node(data)
            self.start_node = newNode
        else:
            print("\nThe list is not empty.")

    def insertToEnd(self, data):
        if self.start_node is None:
            newNode = Node(data)
            self.start_node = newNode
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        newNode = Node(data)
        n.next = newNode
        newNode.prev = n

    def deleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete.")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def deleteAtEnd(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete.")
            return
        n = self.start_node
        if n.next is None:
            self.start_node = None
            return
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        n = self.start_node
        while n is not None:
            print("Element is:", n.item)
            n = n.next
        print()


# Usage example
list1 = DoubleLinkedList()
list1.insertToEmptyList("Data")
s2 = Node("Structure")
s3 = Node("Data")
s4 = Node("Mining")
s5 = Node("Data")
s6 = Node("Cleaning")
s7 = Node("Game")
s8 = Node("Development")

list1.start_node.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = s6
s6.next = s7
s7.next = s8

s2.prev = list1.start_node
s3.prev = s2
s4.prev = s3
s5.prev = s4
s6.prev = s5
s7.prev = s6
s8.prev = s7

list1.display()
a = input("Search: ")

list1.searchElement(a)
