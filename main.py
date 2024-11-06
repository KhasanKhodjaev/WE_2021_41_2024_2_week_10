from typing import List

# Function to filter out even numbers from a list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and returns a list of even numbers.
    
    Args:
        int_list: A list of integers.
        
    Returns:
        A list of even integers.
    """
    even_numbers = []
    
    # Iterate through the input list and check for even numbers
    for num in int_list:
        if num % 2 == 0:  # Check if the number is even
            even_numbers.append(num)  # Add it to the list
    
    return even_numbers


# Function to calculate the sum of squares of even numbers in a list
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in the list.
    
    Args:
        even_int_list: A list of even integers.
        
    Returns:
        The sum of the squares of all even numbers in the list.
    """
    sum_squares = 0
    
    # Iterate through the list of even integers and add the square of each number
    for num in even_int_list:
        sum_squares += num ** 2
    
    return sum_squares


# Main function to demonstrate the functionality
def main():
    # Example input list of integers
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Step 1: Get the list of even integers
    even_int_list = even_list(int_list)
    print(f"Even numbers from the list: {even_int_list}")
    
    # Step 2: Calculate the sum of squares of the even integers
    output = sum_of_squares_of_even(even_int_list)
    print(f"Sum of the squares of the even numbers: {output}")


# Boilerplate code to ensure that the main function runs when the script is executed
if __name__ == "__main__":
    main()
