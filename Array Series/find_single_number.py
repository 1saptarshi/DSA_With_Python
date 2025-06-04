#Find the number that appears once, and the other numbers twice
def find_single_number(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example
arr = [2, 3, 5, 4, 5, 3, 2]
print("The single number is:", find_single_number(arr))  # Output: 4


 