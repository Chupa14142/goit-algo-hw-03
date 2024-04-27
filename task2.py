"""Module 3/Task2"""
from random import sample


def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    """Get list of random numbers in a range"""

    if min_number < 1 or min_number >= max_number:
        print("Min must be bigger than 0 and lower than max")
        return []

    if max_number > 1000:
        print("Max must be lower or equal 1000")
        return []
    
    if quantity > max_number or quantity > max_number - min_number or quantity == 0:
        print("Quantity must be lower than max, bigger than (max - min) and bigger than 0")
        return []

    # Get a list of random numbers
    random_numbers = sample(range(min_number, max_number+1), quantity)

    # Return a sorted list of random numbers
    return sorted(random_numbers)


if __name__ == "__main__":
    # Valid
    print(get_numbers_ticket(10, 20, 9)) 

    # Invalid
    # print(get_numbers_ticket(0, 50, 5))
    # print(get_numbers_ticket(1, 1001, 10))
    # print(get_numbers_ticket(50, 50, 5))
    # print(get_numbers_ticket(1, 50, 0))
    # print(get_numbers_ticket(1, 50, 51))
    # print (get_numbers_ticket(10, 20,15))
