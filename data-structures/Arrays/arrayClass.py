class Array:
    def __init__(self):
        self.arr = []
        self.length = 0

    def get(self, index):
        """
        It returns the value of the array at the given index.
        
        :param index: The index of the element you want to get
        :return: The value of the index in the array.
        """
        return self.arr[index]

    def push(self, item):
        """
        It adds an item to the end of the list.
        
        :param item: The item to be pushed onto the stack
        """
        self.arr.append(item)
        self.length += 1

    def pop(self):
        """
        It removes the last element of the array.
        """
        self.arr.pop()
        self.length -= 1

    def insert(self, index, item):
        """
        Inserts an item at a given index in the array
        
        :param index: The index where you want to insert the item
        :param item: The item to be inserted
        """
        self.arr.insert(index, item)
        self.length += 1

    def print_array(self):
        """
        Prints the array
        """
        for i in range(self.arr):
            print(self.arr[i])


my_array = Array()
my_array.push(4)
my_array.push(8)
my_array.push(3)

print(my_array.print_array())