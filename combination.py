#Write a program to print all the combinations of the given word with or without meaning (when unique characters are given).

def convertToString(a):
    k="".join(a)    #join the elemets of list with "no space"
    print(k)

def permute(a,first,last):
    if(first==last):
        convertToString(a)
    else:
        for i in range(first,last+1):
            a[first],a[i]=a[i],a[first] #swap
            permute(a,first+1,last) #permute
            a[first],a[i]=a[i],a[first] #swap



#main function

str=input()
l=len(str)
a=list(str)     #convert to list
permute(a,0,l-1)


