
# Node class for Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # ------------------------------------------------
    # Question 1:
    # Write a program to insert a node at the end
    # of a singly linked list.
    # ------------------------------------------------
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    # ------------------------------------------------
    # Question 2:
    # Write a program to insert a new node after
    # a given value in a singly linked list.
    # ------------------------------------------------
    def insert_after(self, key, data):
        temp = self.head

        while temp:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print("Value not found in the list")


    # ------------------------------------------------
    # Question 3:
    # Write a program to delete the last node
    # from a singly linked list.
    # ------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    # ------------------------------------------------
    # Question 4:
    # Write a program to delete a node after
    # a given value in a singly linked list.
    # ------------------------------------------------
    def delete_after(self, key):
        temp = self.head

        while temp and temp.next:
            if temp.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Key not found or no node after key")


    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ------------------ Driver Code ------------------
sll = SinglyLinkedList()

sll.insert_end(10)
sll.insert_end(20)
sll.insert_end(30)
sll.display()

sll.insert_after(20, 25)
sll.display()

sll.delete_end()
sll.display()

sll.delete_after(10)
sll.display()