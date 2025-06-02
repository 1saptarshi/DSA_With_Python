# Find the missing number in an array

def missing_number(arr,N):
    expected_sum=N*(N+1)//2
    actual_sum=sum(arr)
    return expected_sum-actual_sum
N=9
arr=[1,2,4,5,6,7,8,9]
print(missing_number(arr,N))


 