
#Power of a number (x^y)
x=2
y=3
print(x**y)

#Smallest digit in a number
n=1023456789
c=1
while n>0:
    d=n%10
    if c>d:
        c=d
    n=n//10
print(c)


#Largest digit in a number
n=12345678
c=0
while n>0:
    d=n%10
    if d>c:
        c=d
    n=n//10
print(c)


#Product of digits
n=123
c=1
while n>0:
    d=n%10
    c=c*d
    n=n//10
print(c)

#Sum of digits
n=map(int,input().split())
# print(sum(n))
c=0
for i in (n):
    c+=i
print(c)

#Count digits in a number
n=123
c=0
while n>0:
    d=n%10
    c=c+1
    n=n//10
print(c)
    


#Perfect number
n=6
t=0
for i in range(1,n):
    if n%i==0:
        t=t+i
if t==n:
    print("Perfect")
else:print("not Perfect")

# Strong number
n = 145
t = n
s = 0

while n > 0:
    m = n % 10
    f = 1
    for i in range(1, m+1):
        f = f * i
    s = s + f
    n = n // 10

if t == s:
    print("Strong number")
else:
    print("not Strong number")

#Armstrong number
n=153
t=n
s=0
d=len(str(n))
while n>0:
    m=n%10
    s=s+m**d
    n=n//10
if t==s:
    print("Armstrong")
else:print("not Armstrong")

#Palindrome number
n=101
t=n
c=0
while n>0:
    d=n%10
    c=c*10+d
    n=n//10
if t==c:
    print("palindrome")
else:print("not palindrome")

#Reverse a number
n=123
c=0
while n>0:
    d=n%10
    c=c*10+d
    n=n//10
print(c)
    

#Fibonacci series
n=10
a=0
b=1
for i in range(n):
    print(a,end=",")
    c=a+b
    a=b
    b=c
    

#Print prime numbers from 1 to N
n=10
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

#Prime number check
n=11
if n<=1:
    print("not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")


#Factorial of a number
n=10
f=1
for i in range(1,n+1):
    f=f*i
print(f)


#Print numbers from 1 to N
n=5
for i in range(1,n+1):
    print(i)
#Print even numbers from 1 to N
n=10
for i in range(1,n+1):
    if i%2==0:
        print(i)
#Print odd numbers from 1 to N
n=10
for i in range(1,n+1):
    if i%2!=0:
        print(i)
#Sum of first N numbers
n=10
print((n*(n+1))//2)
