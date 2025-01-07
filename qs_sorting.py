arr = [2,0,2,1,1,0]
def qs(arr):
    def quicksort(arr):  
        if len(arr) < 2:  
            return arr  
        pivot = arr[0]  
        left = [x for x in arr[1:] if x < pivot]  
        right = [x for x in arr[1:] if x >= pivot] 
        return quicksort(left) + [pivot] + quicksort(right)
    arr = quicksort(arr)

print(arr)
qs(arr)
print(arr)