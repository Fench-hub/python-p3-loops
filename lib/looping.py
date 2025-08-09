 #!/usr/bin/env python3

def happy_new_year():
    """
    Counts down from 10 to 1 using a while loop and then prints "Happy New Year!".
    """
    # Initialize the counter for the countdown
    count = 10
    
    # Loop while the count is greater than 0
    while count > 0:
        print(count)
        # Decrement the counter
        count -= 1
    
    # After the loop, print the final message
    print("Happy New Year!")


def square_integers(numbers):
    """
    Takes a list of integers and returns a new list with each integer squared.
    
    Args:
        numbers: A list of integers.
        
    Returns:
        A new list with the squared values.
    """
    # Create an empty list to store the results
    squared_numbers = []
    
    # Loop through each number in the input list
    for num in numbers:
        # Square the number and append it to the new list
        squared_numbers.append(num ** 2)
        
    return squared_numbers

# An alternative, more Pythonic way using a list comprehension:
# def square_integers(numbers):
#     return [num ** 2 for num in numbers]


def fizzbuzz():
    """
    Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    """
    # Iterate through numbers from 1 up to and including 100
    for num in range(1, 101):
        # Check for multiples of both 3 and 5 first
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        # Check for multiples of 3
        elif num % 3 == 0:
            print("Fizz")
        # Check for multiples of 5
        elif num % 5 == 0:
            print("Buzz")
        # For all other numbers, just print the number
        else:
            print(num)
