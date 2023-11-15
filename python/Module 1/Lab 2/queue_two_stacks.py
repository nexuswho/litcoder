class CustomQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # Queue is empty

    def print_front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        else:
            return None  # Queue is empty


# Exercise-1
queue1 = CustomQueue()
queries1 = ["1 42", "2", "1 14", "3"]
for query in queries1:
    if query.startswith("1"):
        _, element = query.split()
        queue1.enqueue(int(element))
    elif query == "2":
        queue1.dequeue()
    elif query == "3":
        result = queue1.print_front()
        print(result)

# Exercise-2
queue2 = CustomQueue()
queries2 = ["1 23", "2", "1 14", "3", "2", "1 78", "3"]
for query in queries2:
    if query.startswith("1"):
        _, element = query.split()
        queue2.enqueue(int(element))
    elif query == "2":
        queue2.dequeue()
    elif query == "3":
        result = queue2.print_front()
        print(result)
