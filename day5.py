# MinStack class for stack operations with additional getMin functionality
class MinStack:

    def __init__(self):
        # Constructor to initialize the stack as an empty list
        self.stack = []
    
    # Method to push a new value onto the stack
    def push(self, val: int) -> None:
        self.stack.append(val)  # Append the value to the stack

    # Method to remove the top element from the stack
    def pop(self) -> None:
        self.stack.pop()  # Remove the last element in the stack

    # Method to return the top element of the stack without removing it
    def top(self) -> int:
        return self.stack[-1]  # Return the last element in the stack (top element)

    # Method to retrieve the minimum element from the stack
    def getMin(self) -> int:
        # Initialize the minimum value as the last element in the stack
        self.min = self.stack[len(self.stack) - 1]
        
        # Loop to iterate through the stack from top to bottom
        for i in range(len(self.stack) - 1, -1, -1):
            # Update min if a smaller element is found
            if self.min > self.stack[i - 1]:
                self.min = self.stack[i - 1]
        
        # Return the minimum value found
        return self.min

# Instantiating the MinStack object
minStack = MinStack()

# Pushing values onto the stack
minStack.push(0)  # Push 0 onto the stack
minStack.push(5)  # Push 5 onto the stack
minStack.push(4)  # Push 4 onto the stack
minStack.push(7)  # Push 7 onto the stack

# Retrieving and printing the minimum value in the stack
print(minStack.getMin())  # Output: 0

# Popping the top element from the stack (removes 7)
print(minStack.pop())  # Removes 7, returns None

# Retrieving and printing the top element (should now be 4)
print(minStack.top())  # Output: 4

# Popping the top element again (removes 4)
minStack.pop()  # Removes 4

# Retrieving and printing the new minimum value (should be 0)
print(minStack.getMin())  # Output: 0

# Popping the top element again (removes 5)
minStack.pop()  # Removes 5
