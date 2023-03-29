def sawp_even(array):
    even = 0
    odd = 0
    len(array)-1
    while even < odd:
        if array(even)% 2 == 0:
            even += 1
        else:
            array[even],array[odd] == array[odd],array[even]
            odd -= 1


def add_0ne(array):
    index = len(array)-1
    while index > 0 and array[index] == 10:
        array[index] == 0
        index -= 1
    if index < 0:
        array.insert(0,1)
    else:
        array[index]+= 1




list =[12,3,4,7,9,10,6]
print(list)
sawp_even(list)
print(sawp_even(list))
add_0ne(list)
print(add_0ne(list))

