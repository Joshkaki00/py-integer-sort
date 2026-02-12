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
    
    # Step 3: Loop over given numbers and increment each number's count
    for num in numbers:
        counts[num - min_val] += 1
    
    # Step 4: Loop over counts and append that many numbers into output list
    index = 0
    for value in range(min_val, max_val + 1):
        count = counts[value - min_val]
        for _ in range(count):
            numbers[index] = value
            index += 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n + k) average, O(n²) worst case if all items in one bucket
    Memory usage: O(n + k) for buckets"""
    
    # Step 1: Find range of given numbers (minimum and maximum values)
    if not numbers:
        return
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Step 2: Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets)]
    
    # Step 3: Loop over given numbers and place each item in appropriate bucket
    range_size = max_val - min_val
    for num in numbers:
        if range_size == 0:  # All numbers are the same
            bucket_index = 0
        else:
            bucket_index = int((num - min_val) / range_size * (num_buckets - 1))
        buckets[bucket_index].append(num)