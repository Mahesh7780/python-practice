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
    *

#diamond pattern
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
        print("*",end=" ")
    print()
    
#output
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

#down hill
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
    
#output

* * * * * 
 * * * * 
  * * * 
   * * 
    * 

# hill pattern
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

#output

    * 
   * * 
  * * * 
 * * * * 

#left side

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
#output

  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
# right side 
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

#output

          * 
        * * 
      * * * 
    * * * * 
  * * * * * 

# decreasing triangle
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

#output

* * * * * 
* * * * 
* * * 
* * 
* 

#increasing triangle
for i in range(n):
    for i in range(i+1):
        print("*",end=" ")
    print()

#output

* 
* * 
* * * 
* * * * 
* * * * * 
#rectangle   
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
    
#output

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
