# Check if an Array is Sorted
# Brute Force Approach
arr = [1, 2, 2, 4, 5]  # You can change this to test

is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print("Is array sorted (Brute Force)?", is_sorted)

# algo

# Input: an array arr of size n
# 
# If n <= 1, return True (an empty or single-element array is sorted)
# 
# Loop from i = 0 to n - 2:
# 
# If arr[i] > arr[i+1], return False
# 
# If loop completes without returning False, return True
#  
#  
 
 
 
 
 
 