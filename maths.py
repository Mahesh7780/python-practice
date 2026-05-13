#Fibonacci Check 49
n=13
a=0
b=1
for i in range(n):

    c=a+b
    a=b
    b=c
    if c==n:
        print("Fibonacci")
        break
else:
    print("not Fibonacci")
# Swap First & Last Digit  
n=1234
t=n
c=0
l=n%10
while n>=10:
    n//=10
    c+=1
m=(t%(10**c))//10
r=(l*(10**c))+(m*10)+n
print(r)

# Harshad Number 
n=int(input())
m=0
t=n
while n>0:
    f=n%10
    m+=f
    n=n//10
if  m != 0 and t%m==0:
    print("Harshad Number")
else:print("Not Harshad Number")

# Duck Number 
num = 0123
temp = num
duck = False
while temp > 0:
    digit = temp % 10

    if digit == 0:
        duck = True
        break
    temp //= 10
if duck:
    print("Duck Number")
else:
    print("Not a Duck Number")
    
    # or
    
num = "0123"
if '0' in num and num[0] != '0':
    print("Duck Number")
else:
    print("Not a Duck Number")

#  Neon Number  
n=9
t=n**2
m=0
while t>0:
    c=t%10
    m+=c
    t=t//10
if n==m:
    print("yes")
else:print("no")

#  Automorphic Number 
n=25
t=n**2
l=len(str(n))
s=t%(10**l)
if n==s:
    print("yes")
else:print("no")
print(l)

# Perfect Number    
n=28
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if n==s:
    print("Perfect Number")
else:print("Not Perfect Number")

# Sum of array elements 
s=[10,2,3,4,50]
m=0
for i in s:
    m=m+i
print(m)
# Find minimum element
s=[10,2,3,4,50]
m=s[-1]
for i in s:
    if i<m:
        m=i
print(m)

# Find maximum element

s=[10,2,3,4,50]
m=s[0]
for i in s:
    if i>m:
        m=i
print(m)

# Find length of list
s=[1,2,3,4,5]
l=0
for i in s:
    l+=1
print(l)
#or
print(len(s))

#Check Anagram
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")
    
#Copy One String to Another
s1 = input("Enter a string: ")
s2 = ""
for i in s1:
    s2 += i
print("Copied string:", s2)

#Find Frequency of a Character
s = input()
ch = input()
count = 0
for i in s:
    if i == ch:
        count += 1
print(count)

#Remove Spaces from String
s = input()
r= ""
for i in s:
    if i != " ":
        r += i
print (r)

#Count digits in string
s="hellocs097ebcb5k8v0jbjxs"
c=0
for i in s:
    if i>="0" and i<="9":
        c+=1
print(c)

#Count words
s="hello cs ebcbkv jbjxs"
c=0
for i in s:
    if i ==" ":
        c+=1
print(c)

#Count consonants
s="hello"
a="aeiou"
c=0
for i in s:
    if i not in a:
        c+=1
print(c)

#Count vowels
s="hello"
a="aeiou"
c=0
for i in s:
    if i in a:
        c+=1
print(c)

#Check palindrome string
s="hello"
t=s
c=""
for i in s:
    c=i+c
if t==c:
    print("palindrome")
else:print("not palindrome")

#reverse string
s="hello"
c=""
for i in s:
    c=i+c
print(c)

#Find length of string
s="hello"
c=0
for i in s:
    c+=1
print(c)

#Count even and odd digits
n=12345
odd=0
even=0
while n!=0:
    d=n%10
    if n%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(odd)
print(even)

#Swap two numbers (without third variable)
a=20
b=30
a=a+b
b=a-b
a=a-b
print(a,b)

#GCD / HCF of two numbers
a=12
b=24
while b!=0:
    tep=b
    b=a%b
    a=tep
print(a)

#Power of a number (x^y)
x=2
y=3
print(x**y)

#Smallest digit in a number
n=234956
c=n%10
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
