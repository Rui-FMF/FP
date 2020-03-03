# Example 3: 
# Read numbers until a sentinel (an empty string), and return their sum.
# JMR 2018

# This is a typical example of a "loop-and-a-half"

def inputTotal():
    tot = 0.0
    while True:
        s = input("valor? ")
        if s == "": break   # if empty line, stop repeating!
        v = float(s)
        tot = tot + v
    return tot

tot = inputTotal()
print(tot)

