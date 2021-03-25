import collections

# Create an empty deque object
dequeObject = collections.deque()

# Add elements to the deque - left to right
dequeObject.append(1)
dequeObject.append(3)
dequeObject.append(6)
dequeObject.append(10)

# Print the deque contents
print("Deque before any rotation:")
print(dequeObject)

# Rotate once in positive direction
dequeObject.rotate()

print("Deque after 1 positive rotation:")
print(dequeObject)

# Rotate twice in positive direction
dequeObject.rotate(2)

print("Deque after 2 positive rotations:")
print(dequeObject)
