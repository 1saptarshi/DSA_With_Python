# Find the Largest element in an array
# ✅ 1. Brute Force Approach

def find_largest_brute_force(arr):
    if not arr:
        return None  # Handle empty array
    max_element = arr[0]
    for num in arr[1:]:
        if num > max_element:
            max_element = num
    return max_element

arr = [5, 3, 9, 1, 7]
print("Largest element (Brute Force):", find_largest_brute_force(arr))
