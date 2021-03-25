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

#2nd option
import collections
sequence = (1, 2, 4, 8, 16, 32)

# Create a deque from the tuple
sequenceInDeque = collections.deque(sequence)

# Print the contents of the deque object
print("Deque before any rotation:")
print(sequenceInDeque)

# Rotate once - in negative direction
sequenceInDeque.rotate(-1)
print("Deque after 1 negative rotation:")
print(sequenceInDeque)
