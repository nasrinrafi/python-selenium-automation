def swap_string(a):
    string=len(a)
   # half_first=a[0:len(a)//2]
    if len(a)//2 and len(a)%2 == 0:
     half_second = a[(len(a)//2+1):]
    else:
     half_first=a[0:len(a)//2]
   # return half_second+half_first

 #test_a='aaasss'
#test=swap_string(test_a)
#print(test)
#number2
def uniq_letter (string:str):
    string=string.lower()
    d={}
    for letter in string:
        if letter not in d:
          d[letter]=1
        else:
            d[letter]+=1
    print(d)

print(uniq_letter('google.com'))









