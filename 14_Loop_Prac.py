n = int(input("enter the number :"))
for i in range(n):
    print("Hello Yashank How Are You")

n = int(input("enter the number :"))
for i in range(1, n+1):
    print(i)

#sum of n numbers
n = int(input("enter the number :"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
    print(sum)

# factorial

n = int(input("enter the number :"))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print(f"the factorial is {fact}")

# sum of even no. and odd no.

n = int(input("enter the number :"))
even_sum = 0
odd = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd = odd + i

print(f"your sum of {even_sum}, {odd}")

# factors of numbers

n = int(input("enter the number :" ))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# check of perfect numbers

n = int(input("enter the number :"))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("perfect number")
else:
    print("not perfect number")

# check prime number
n = int(input("enter the number :"))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("prime number")
else:
    print("not prime number")

# print reverse string

a = "GANDHINAGAR"

for i in range(len(a) -1, -1, -1):
    print(a[i])

#palindrome or not

a = "NAMAN"
b = ""

for i in range(len(a) -1, -1, -1):
    b = b + a[i]

if b == a:
    print("palindrome")
else:
    print("not palindrome")
