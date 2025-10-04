arr=[6,9,8,34,5,6]
n=len(arr)
res=[]
for i in range(n-1,-1,-1):
  res.append(arr[i])
print(res)