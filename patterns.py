# midle of the diamond
n=int(input())
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in  range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in  range(i,n):
        if i==0 and j==2:
            print("m",end=" ")
        else:
            print("*",end=" ")
    print()
    
# output

    * 
   * * 
  * * * 
 * * * * 
* * m * * 
 * * * * 
  * * * 
   * * 
