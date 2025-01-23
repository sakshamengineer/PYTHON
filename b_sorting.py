arr = [39, 12, 18, 85, 72, 10, 2, 18]
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)
