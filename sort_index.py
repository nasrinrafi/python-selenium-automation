def sort_index(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
          if arr[j]>arr[min_index]:
           min_index = j
        arr[min_index],arr[i] == arr[i],arr[min_index]



    return(arr)

list = [12,2,4,78,98,6]
print(sort_index(list))

def Bubbel_sort(arr):
    for i in range(len(arr)):
        for j in range (0,len(arr)-i-1):
          if arr[j] > arr[j+1]:
           arr[j],arr[j+1]==arr[j+1],arr[j]
    return (arr)

list = [12,2,4,78,98,6]
print(Bubbel_sort(list))

def insert_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j<=0 and key > arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key

    return arr








