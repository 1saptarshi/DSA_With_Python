# Rotate array by K elements

def rotate_array(arr, k, direction):
    n = len(arr)

    # Handle if k is bigger than array length
    k = k % n

    # Right rotation
    if direction == "right":
        # Last k elements + first n-k elements
        rotated = arr[-k:] + arr[:-k]

    # Left rotation
    elif direction == "left":
        # From k to end + from start to k
        rotated = arr[k:] + arr[:k]

    else:
        return "Invalid direction. Use 'left' or 'right'."

    return rotated


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
direction = "right"

result = rotate_array(arr, k, direction)
print("Rotated array:", result)


# algo

# 🧠 Algorithm (for both directions):
# Take the input array and value of k.

# Use slicing to rotate:

# For right rotation:

# Do: array[-k:] + array[:-k]

# For left rotation:

# Do: array[k:] + array[:k]

# Print or return the result.