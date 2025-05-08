# Mutaz Al-Shara
# Instructor Rita M. Ghantous
# 5/8/2025
# Engr_103_400_S2025
# find_median.py

def find_median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float or None: The median of the list, or None if the list is empty.
    """
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2

    return median
