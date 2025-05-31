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

# Steps:
# Check if the array is empty:
# 
# If the array has no elements, return None (no maximum value can be found).
# 
# Initialize the maximum:
# 
# Set a variable max_element to the first element of the array (arr[0]).
# 
# Loop through the remaining elements (from index 1 to end):
# 
# For each number num in the array:
# 
# Compare it with max_element.
# 
# If num is greater than max_element, update max_element to be num.
# 
# Return the result:
# 
# After the loop ends, return max_element as the largest value.



 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 