class Array:
    def __init__(self):
        self.arr = []
        self.length = 0

    def get(self, index):
        return self.arr[index]

    def push(self, item):
        self.arr.append(item)
        self.length += 1

    def pop(self):
        self.arr.pop()
        self.length -= 1

    def insert(self, index, item):
        self.arr.insert(index, item)
        self.length += 1

    def print_array(self):
        for i in range(self.arr):
            print(self.arr[i])


my_array = Array()
my_array.push(4)
my_array.push(8)
my_array.push(3)

print(my_array.print_array())