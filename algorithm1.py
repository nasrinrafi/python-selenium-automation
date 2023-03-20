def sum_end(n):
    f_sum = 0
    for i in range(n+1):
        f_sum = f_sum+i
        return f_sum

test = sum_end(n=10)
print(test)


def find_max(a,b,c,):
   if a>b and a>c:
       return a
   if b>a and b>c:
      return b
   return c
test=find_max(10,130,148)
print(test)


list_number=[]
event_count=0
odd_count=0
#def odd_even_number(list_number):
  ##    if i%2==0:
    #    odd_count+=odd_count
     ####return odd_count

list_number=[50,20,11,234,345]
test=odd_even_number(list_number)
print(list_number)










