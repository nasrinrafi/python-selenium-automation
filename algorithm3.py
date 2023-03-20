def arithmetical_resul(arr):
    Artihmetical= sum(arr)/len(arr)

    list=[]
    for i in arr:
        if i<Artihmetical:
            list.append(i)
    return list


def two_first_element(arr):
    arr.sort()
    return arr[:2]

test_list=[34,5,6,8,67,3,8]
result1=arithmetical_resul(test_list)
result2=two_first_element(test_list)
print(result1)
print(result2)


