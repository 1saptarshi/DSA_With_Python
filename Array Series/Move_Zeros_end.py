# #  Move all Zeros to the end of the 
# 💥 1. Brute Force Approach
# ➕ Idea:
# Create a new array.

# Add all non-zero elements first (in order).

# Then add the zeros at the end.

# Finally, copy it back or return the new array.

def move_zeros_brute_force(arr):
    result = []

    # Add all non-zero elements
    for num in arr:
        if num != 0:
            result.append(num)
    
    # Add zeros at the end
    zero_count = len(arr) - len(result)
    result.extend([0] * zero_count)

    return result
arr = [0, 1, 0, 3, 12]
print(move_zeros_brute_force(arr))  # Output: [1, 3, 12, 0, 0]

