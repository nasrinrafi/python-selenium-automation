def remove_item (list,n):
    for i in range(len(list)-1):
        if list[i] == n:
            list.pop(i)
    return(list)


list=[12,4,5,88,7,9,8]
result=remove_item(list,8)
print(result)
