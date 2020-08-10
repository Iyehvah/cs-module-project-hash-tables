class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
        return None

    def insert(self, value):
        value.next = self.head #moving our head over to make room for the new head of our list
        self.head = value #making new value our head here

    def delete(self, value):
        #creating a starting point for our loop to find the value we want to delete.
        current = self.head #starting at the head of the list

        #if the value we want to delete is THE HEAD of our list
        if current.value == value: # loop through till we find our value
            self.head = self.head.next # make the new head of our list the .next value
            current.next = None
            return current

        #if the value we want to delete is not the head of our list
        prev = current
        current = current.next 

        while current is not None:
            if current.value == value:
                prev.next = current.next
                current.next = None
                return current
            else:
                prev = prev.next
                current = current.next
        return None