def linearSearch(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
arr=[2,7,5,3,9,0]
target=9
print(linearSearch(arr,target))
## takes o(n) 
# takes input <-- output
