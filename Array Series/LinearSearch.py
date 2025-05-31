def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i  # Element found at index i
    return -1  # Element not found

# Example usage:
arr = [10, 25, 30, 45, 50]
num = 30

result = linear_search(arr, num)
print(result)  # Output: 2


 
 
 
 
 
 
 
 
 
 
 