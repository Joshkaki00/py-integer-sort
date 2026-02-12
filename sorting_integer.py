#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n + k) where n is number of items, k is range of values
    Memory usage: O(k) for counts array"""
    
    # Step 1: Find range of given numbers (minimum and maximum integer values)
    if not numbers:
        return
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Step 2: Create list of counts with a slot for each number in input range
    range_size = max_val - min_val + 1
    counts = [0] * range_size

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
