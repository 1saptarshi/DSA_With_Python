# # Count Maximum Consecutive One's in the array
# Initialize two counters:

# max_count = 0 → to store the maximum number of consecutive 1s found so far.

# current_count = 0 → to count the current streak of 1s.

# Loop through the array:

# If the element is 1:

# Increase current_count by 1.

# Update max_count if current_count is greater than max_count.

# If the element is 0:

# Reset current_count to 0 (because the streak of 1s is broken).

# Return max_count after the loop ends.

def max_consecutive_ones(arr):
    max_count = 0
    current_count = 0

    for num in arr:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count
arr = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(arr))  # Output: 3

