#!/usr/bin/env python3

def print_fibonacci(length):
    # Edge case: if length is 0, print nothing
    if length == 0:
        print("[]")
        return
    
    # Edge case: if length is 1, print only the first Fibonacci number
    elif length == 1:
        print("[0]")
        return
    
    # Initialize the list to hold the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the desired length
    while len(fib_sequence) < length:
        # Append the next Fibonacci number
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Print the list in the required format (as a list in string format)
    print(f"[{', '.join(map(str, fib_sequence))}]")

# Example usage:
print_fibonacci(10)  


