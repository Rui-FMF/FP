# Example 2: Functions with lists
# jmr 2018

# Read N numbers and return them in a list.
def inputFloats(prompt, N):
    l = []
    for x in range(N):
        r = float(input(prompt))
        l.append(r)
    return l

# A function that modifies the elements in a list.
def up(lst):
    for i in range(len(lst)):
        lst[i] += 1
    # returns no result but changes the list as a side-effect!


# Test the functions:

#temp = inputFloats("temperatura? ", 3)
#print(max(temp))

l = inputFloats("valor? ", 4)
print(l)
up(l)
print(l)

