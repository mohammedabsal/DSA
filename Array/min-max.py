def max_f(arr):
    n=len(arr)
    max_value=arr[0]
    for i in range(n):
        if arr[i]>max_value:
            max_value=arr[i]
    return max_value
def min_f(arr):
    n=len(arr)
    min_value=arr[0]
    for i in range(n):
        if arr[i]<min_value:
            min_value=arr[i]
    return min_value
arr=[9,3,4,56,1]
print(max_f(arr))
print(min_f(arr))