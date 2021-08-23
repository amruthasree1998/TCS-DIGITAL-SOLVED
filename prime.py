#There is a range given n and m in which we have to find the count of all the prime pairs whose difference is 6. We have to find how many sets are there within a given range.
#Output:
#The output consists of a single line, print the count prime pairs in a given range. Else print"No Prime Pairs".


n = int(input())
m = int(input())  
b=[]; 
for num in range(n,m + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
           b.append(num)
print(b)
count=0
for i in b:
    for j in b:
        if((i-j==6) or (j-i==-6)):
           count=count+1; 
           
if count==0:
    print("No Prime Pairs")
else:
    print(count)
