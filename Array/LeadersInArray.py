# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
def lead_element(arr):
    res=[]
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                break
        else:
            res.append(arr[i])
    return res
arr=[16, 17, 4, 3, 5, 2]
print(lead_element(arr))