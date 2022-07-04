class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self, value):
        """
        We create a new node with the value passed to the function, and assign the head and tail to be
        the new node, and the length to be 1
        
        :param value: The value of the node we're adding
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self) -> None:
        """
        We start at the head of the linked list and print each value until we reach the end of the
        linked list
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def add_node_beginning(self, value) -> bool:
        """
        We create a new node, and if the list is empty, we set the head and tail to the new node.
        Otherwise, we set the new node's next to the current head, and then set the head to the new node
        
        :param value: The value of the node to be added
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_node_end(self, value) -> bool:
        """
        We create a new node, and if the list is empty, we set the head and tail to the new node.
        Otherwise, we set the next property of the tail to the new node, and then set the tail to the
        new node
        
        :param value: The value of the node to be added
        :return: True
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def remove_node_beginning(self) -> Node:
        """
        We're removing the head node and returning it
        :return: The node that was removed from the beginning of the linked list.
        """
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def remove_node_end(self) -> Node:
        """
        We start at the head and traverse the list until we reach the end. 
        
        We then set the tail to the previous node and set the next pointer of the tail to None. 
        
        We then decrement the length of the list by 1. 
        
        If the length of the list is 0, we set the head and tail to None. 
        
        Finally, we return the node that was removed
        :return: The node that was removed from the end of the list.
        """
        if self.length == 0:
            return None

        temp = self.head
        prev = self.tail
        while (temp.next):
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


    def get_node(self, index) -> Node:
        """
        We start at the head and traverse the linked list until we reach the index we want to get to
        
        :param index: The index of the node we want to get
        :return: The node at the given index.
        """
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def set_node_value(self, index, value) -> bool:
        """
        If the node at the given index exists, set its value to the given value and return True.
        Otherwise, return False
        
        :param index: The index of the node you want to change
        :param value: The value to be stored in the node
        :return: The value of the node at the given index.
        """
        temp = self.get_node(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert_node_by_index(self, index, value) -> bool:
        """
        We create a new node, and then we set the next pointer of the new node to the next pointer of
        the node at index - 1. 
        
        Then we set the next pointer of the node at index - 1 to the new node. 
        
        Finally, we increment the length of the linked list.
        
        :param index: The index of the node you want to insert
        :param value: The value of the node to be inserted
        :return: A boolean value
        """
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.add_node_beginning(value)
        if index == self.length:
            return self.add_node_end(value)

        new_node = Node(value)
        temp = self.get_node(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove_node_by_index(self, index) -> Node:
        """
        We get the node before the one we want to remove, and then we set the next pointer of the
        previous node to the next pointer of the node we want to remove
        
        :param index: The index of the node to be removed
        :return: The node that was removed.
        """
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.remove_node_beginning()
        if index == self.length - 1:
            return self.remove_node_end()

        prev = self.get_node(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse_nodes(self) -> None:
        """
        We swap the head and tail, then we iterate through the list, setting the next node to the
        previous node, and then setting the previous node to the current node
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next 
            temp.next = before
            before = temp
            temp = after

# Let's create linkedlist of 11, 3, 4, 7, 70
my_linked_list = LinkedList(11)
my_linked_list.add_node_end(3)
my_linked_list.add_node_end(4)
my_linked_list.add_node_end(7)
my_linked_list.add_node_end(70)

my_linked_list.add_node_beginning(10) # add 10 at the beg = 10, 11, 3, 4, 7, 70
my_linked_list.add_node_end(77) # add 77 at the end = 10, 11, 3, 4, 7, 70, 77

my_linked_list.remove_node_beginning() # remove from the beg = 11, 3, 4, 7, 70, 77
my_linked_list.remove_node_end() # remove from the end 11, 3, 4, 7, 70

my_linked_list.get_node(0) # gets node on the index 0 -> 11

my_linked_list.set_node_value(0, 9) # sets node value on the index 0 -> 9, 3, 4, 7, 70

my_linked_list.insert_node_by_index(4, 77) # inserts node on the index 4 -> 9, 3, 4, 7, 77, 70

my_linked_list.remove_node_by_index(0) # removes node on the index 0 -> 3, 4, 7, 77, 70

my_linked_list.reverse_nodes() # reverse nodes in opposite direction -> 70, 77, 7, 4, 3

my_linked_list.print_linked_list() # 70, 77, 7, 4, 3
