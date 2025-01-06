arr = [39, 12, 18, 85, 72, 10, 2, 18]
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[i]> arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

print(arr)