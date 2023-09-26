"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    stringItems = [str(item) for item in items]

    for i in stringItems:
        if i not in frequencies:
            frequencies[str(i)] = 1
        elif i in frequencies:
            frequencies[str(i)] = frequencies.get(i) + 1
            
            
       
    



    return frequencies
