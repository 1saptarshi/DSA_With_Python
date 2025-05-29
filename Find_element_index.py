# # ✅ 1. Brute Force Approach
# 🔧 Algorithm:
# Store the first element in a temporary variable.

# Shift all elements from index 1 to N-1 to the left by one.

# Put the stored element at the end of the array.

def left_rotate_brute_force(arr):
    if not arr:
        return arr
    
    temp = arr[0]  # Step 1: Store first element
    for i in range(1, len(arr)):  # Step 2: Shift all elements to the left
        arr[i - 1] = arr[i]
    arr[-1] = temp  # Step 3: Put the first element at the end
    return arr

# Example usage:
arr = [1, 2, 3, 4, 5]
print(left_rotate_brute_force(arr))  # Output: [20, 30, 40, 50, 10]

# ✅ 2. Optimal Approach (Using Slicing)
# 💡 Algorithm:
# Use Python list slicing:

# arr[1:] gives elements from index 1 to end.

# [arr[0]] is the first element.

def left_rotate_optimal(arr):
    if not arr:
          return arr
    return arr[1:]+[arr[0]]
arr = [10, 20, 30, 40, 50]
print(left_rotate_optimal(arr))
