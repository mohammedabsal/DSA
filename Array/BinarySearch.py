def BinarySearch(arr,target):
    n=len(arr)
    left,right=0,n-1
    while(left<right):
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
arr=[10,20,30,40,50,60,70,80,90,100]
target=80
result=BinarySearch(arr,target)
print(result)