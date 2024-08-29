def chop(lst):
    if len(lst) > 2:
        del lst[0]  # Remove the first element
        del lst[-1]  # Remove the last element

# Example usage
lst = [1, 2, 3, 4, 5]
chop(lst)
print(lst)  # Output: [2, 3, 4]


def cumsum(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)
    return result

# Example usage
numbers = [1, 2, 3, 4]
print(cumsum(numbers))  # Output: [1, 3, 6, 10]


def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# Example usage
lst = [1, 2, 3, 4, 1]
print(has_duplicates(lst))  # Output: True

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage
lst = [1, 2, 2, 3]
print(is_sorted(lst))  # Output: True

def nested_sum(lst_of_lists):
    total = 0
    for inner_list in lst_of_lists:
        for number in inner_list:
            total += number
    return total

# Example usage
lst_of_lists = [[1, 2], [3, 4], [5]]
print(nested_sum(lst_of_lists))  # Output: 15


