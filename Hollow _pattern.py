# Hollow Square
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 and j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#    O/P

* * * * * 
*       * 
*   *   * 
*       * 
* * * * * 

# plus Square
n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# O/P
    *     
    *     
* * * * * 
    *     
    *    
# decreasing triangle 
n=5
for i in range(n):
    for j in range(i,n):
        if i==0 or j==0 or i==n-1 or j==n-1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#O/P 
* * * * * 
*     * 
*   * 
* * 
* 

# increasing triangle 
n=5
for i in range(n):
    for j in range(i+1):
        if i==0 or j==0 or i==n-1 or j==n-1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#O/P 
* 
* * 
*   * 
*     * 
* * * * *
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if  i==n-1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#O/P
          * 
        *   * 
      *       * 
    *           * 
  * * * * * * * * * 

# X pattern
n=5
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#O/P
*       * 
  *   *   
    *     
  *   *   
*       * 
