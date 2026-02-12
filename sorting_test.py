#!python

import random
from sorting_integer import counting_sort, bucket_sort

def is_sorted(items):
    """Return whether items are in sorted order."""
    return all(items[i] <= items[i + 1] for i in range(len(items) - 1))

def random_ints(count, min_val, max_val):
    """Return a list of count random integers in range [min_val...max_val]."""
    return [random.randint(min_val, max_val) for _ in range(count)]

sort = bucket_sort
    

def test_sort_on_empty_list():
    items = []
    sort(items)
    assert items == []  # List should not be changed

def test_sort_on_small_lists_of_integers():
    items1 = [3]
    sort(items1)
    assert items1 == [3]  # List should not be changed
    items2 = [5, 3]
    sort(items2)
    assert items2 == [3, 5]  # List should be in sorted order
    items3 = [5, 7, 3]
    sort(items3)
    assert items3 == [3, 5, 7]


def test_sort_on_lists_of_random_integers():
    # Generate list of 10 random integers from range [1...20]
    items1 = random_ints(10, 1, 20)
    sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
    sort(items1)  # Call mutative sort function to sort list items in place
    assert items1 == sorted_items1

    # Generate list of 20 random integers from range [1...50]
    items2 = random_ints(20, 1, 50)
    sorted_items2 = sorted(items2)  # Copy
    sort(items2)  # Mutate
    assert items2 == sorted_items2

    # Generate list of 30 random integers from range [1...100]
    items3 = random_ints(30, 1, 100)
    sorted_items3 = sorted(items3)  # Copy
    sort(items3)  # Mutate
    assert items3 == sorted_items3


if __name__ == '__main__':
    test_sort_on_empty_list()
    print("✓ test_sort_on_empty_list")
    
    test_sort_on_small_lists_of_integers()
    print("✓ test_sort_on_small_lists_of_integers")
    
    test_sort_on_lists_of_random_integers()
    print("✓ test_sort_on_lists_of_random_integers")
    
    print("\nAll tests passed!")
