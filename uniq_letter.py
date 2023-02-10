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












