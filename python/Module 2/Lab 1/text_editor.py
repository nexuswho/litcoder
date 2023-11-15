class CustomStack:
    def __init__(self):
        self.text = ""  # Initial text
        self.command_stack = []  # Stack to keep track of commands for undo operation

    def insert(self, value):
        self.text += value
        self.command_stack.append(
            ("delete", len(value))
        )  # Store the reverse operation for undo

    def delete(self, value):
        deleted_text = self.text[-value:]
        self.text = self.text[:-value]
        self.command_stack.append(
            ("insert", deleted_text)
        )  # Store the reverse operation for undo

    def get(self, value):
        char = self.text[value - 1]
        print(char)

    def undo(self):
        if self.command_stack:
            operation, value = self.command_stack.pop()
            if operation == "insert":
                self.text += value
            elif operation == "delete":
                self.text = self.text[:-value]


# Exercise-1
editor1 = CustomStack()
commands1 = ["1 abc", "3 3", "2 2", "3 1"]
for command in commands1:
    action, *args = command.split()
    if action == "1":
        editor1.insert(args[0])
    elif action == "2":
        editor1.delete(int(args[0]))
    elif action == "3":
        editor1.get(int(args[0]))

# Exercise-2
editor2 = CustomStack()
commands2 = ["1 zxy", "3 3", "2 2", "1 def", "3 2"]
for command in commands2:
    action, *args = command.split()
    if action == "1":
        editor2.insert(args[0])
    elif action == "2":
        editor2.delete(int(args[0]))
    elif action == "3":
        editor2.get(int(args[0]))
