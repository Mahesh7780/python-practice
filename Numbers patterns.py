#increasing nums
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()
    
#decreasing nums
n=5
p=5
for i in range(n):
    for j in range(i,n):
        print(p,end=" ")
    p-=1
    print()

# right side triangle of nums
n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()

#O/p
          1 
        2 2 
      3 3 3 
    4 4 4 4 
  5 5 5 5 5 
