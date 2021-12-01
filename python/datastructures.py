'''
Python is an incredibly flexible scripting language that can be used to rapidly code a variety of 
data structures without the need to build out scaffolding code for input, types, arrays, etc.
It's flexibility means that types must be carefully managed and errors may propegate outside from the
line in which they originate from. 
'''

## Syntax Basics ##

# Define a variable
var = 10

# Define an array
array = [1,2,3,4,5,6,7,8]

# Print to console
print("Hello World, please enter some data into console")

# Accept input from console
dat = input()
print("You said: ", dat)

# Accept input with a list comprehension and parse into an array 
nums = [float(x) for x in input("Enter a list of space separated numbers").split()]
print (nums)

# For Loop
for i in range(0,10):
    print (i)

# Define a function
def sum_array(nums):
    sum = 0
    # For each loop
    for val in nums:
        sum+=val

    print(sum)
    return sum

## Basic Data structures ##

## Stack ##
stack = []
# Push to stack
stack.append(1)
stack.append(2)
stack.append(3)
print ("Stack" ,stack)
# Pop from stack
stack.pop()
print (stack)

## Que ##
que = []
# Push to que
que.append(1)
que.append(2)
que.append(3)
print("Que ", que)
# Release from que
que.pop(0)
print(que)

## Linked Lists and Graphs ##
# Class representation of a linked list node
class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Class representation of a graph node
class GraphNode:
    def __init__ (self, data, connections=[]):
        self.data = data
        self.connections = connections

# Dictionary representation of a graph
graph = {
    1: [2,3,4],
    2: [1],
    3: [1, 4],
    4: []
}
print(graph)
print (graph[1])