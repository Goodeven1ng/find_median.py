# Mutaz Al-Shara
# Insturctor Rita M. Ghantous
# 5/8/2025
# Engr_103_400_S2025
# find_median.py

def find_median(numbers):
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2

    return median