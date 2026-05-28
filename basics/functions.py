# def fun_name(a,b):
#     return a + b
# print(fun_name(3,4))


# def add_nums(*nums):
#     return sum(nums)
# print(add_nums(1,2,3,4,5,6,7,8,9,0))


# def add():
#     a = int(input("enter first num: "))
#     b = int(input("enter second num: "))
#     print("sum: ", a + b)

# add()


# a = int(input("enter first num: "))
# b = int(input("enter second num: "))
# print("sum: ", a + b)

# def add(a: float, b: float) -> float:
#     return a + b

# print(add(2.324,3))


# def greet():
#     print("hi")
#     print("jenny")

# greet()
# greet()
# greet()

# even or odd

# num = int(input("Enter a number: "))

# def check(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# no return required
# check(num)

# positive/ negative/ or zero

# def number(num):
#     if num > 0:
#         print(f'positive')
#     elif num < 0:
#         print(f'Negative')

#     else:
#         print("zero")

# num = int(input("enter the number: "))

# print((number(num)))

# Greatest of three numbers

# def greatest(a,b,c):

#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# a,b,c = map(int, input('enter three numbers: ').split())
# print("greatest number is: ", greatest(a,b,c))

# c leap year check

# def leap(num):
#     if num % 100 == 0:
#         if num % 400 == 0:
#             return 'Leap year'
#         else:
#             return 'Not a leap year'
#     elif num % 4 == 0:
#         return 'Leap year'
#     else:
#         return 'Not a leap year'

# num = int(input("Enter number: "))
# print(leap(num))

# def leap(num):
#     if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
#         return 'Leap year'
#     else:
#         return 'Not a leap year'

# num = int(input("Enter number: "))
# print(leap(num))

# def leap(num):
#     return (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0)

# num = int(input("Enter number: "))
# print("Leap year" if leap(num) else "Not a leap year")

# vowel or consonant


# def vowel(alphabet):
#     if alphabet in 'aeiou':
#         return 'vowel'
#     else:
#         return 'consonant'

# alphabet = input("enter the alphabet: ".lower())
# print(vowel(alphabet))


# alphabet = input("enter the alphabet: ")
# alphabet = alphabet.lower()

# if alphabet in 'aeiou':
#     print('vowel')

# else:
#     print('consonant')


# Loops practice

# n = int(input("Enter the number: "))

# for i in range (1, n+1):
#     print(i)


# From N to 1

# n = int(input("Enter number: "))

# while n >= 1:
#     print(n)
#     n -= 1


# n = int(input("Enter number: "))

# i = 1
# sum = 0

# while i<=n:
#      sum = sum + i
#      i += 1

# print("sum is: ", sum)

# fact of number

# n = int(input("Enter number: "))

# fact = 1
# i = 1

# while i <= n:
#     fact = fact * i
#     i += 1

# print("factorial of a number: ", fact)


# n = int(input("Enter number: "))


# for i in range(1, 11):
#     print(n, 'X', i, '=', n*i)


# n = int(input("Enter number: "))

# i = 1

# while i<=10:
#     print(n, 'X', i, '=', n * i)
#     i += 1


# n = int(input("Enter the number: "))

# i = 1

# while n>=i:
#     print(i)
#     i += 1


# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     for j in range(i):
#         print('*', end=' ')
#     print()


# n = int(input("Enter the number: "))

# for i in range(n,0,-1):
#     for j in range(i):
#         print('*', end=' ')
#     print()


# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(i, end=' ')
#     print()

# n = int(input("Enter the number: "))

# num = 1

# for i in range(1,n+1):
#     for j in range(i):
#         print(num, end=' ')
#         num += 1
#     print()


# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     for j in range(n):
#         print('*', end=' ')
#     print()

# n = int(input("enter num: "))

# while (n > 0):
#     lastdigit = n % 10
#     print(lastdigit)
#     n = n // 10

# n = int(input("enter num: "))

# count = 0
# while (n > 0):
#     lastdigit = n % 10
#     count = count + 1
#     n = n // 10

# print(count)


# Reverse of a number

# n = int(input("enter num: "))

# reverse = 0
# while (n > 0):
#     lastdigit = n % 10
#     n = n // 10
#     reverse = (reverse * 10) + lastdigit

# print(reverse)

# palindrome of a number

# n = int(input("enter num: "))

# original = n
# reverse = 0
# while (n > 0):
#     lastdigit = n % 10
#     n = n // 10
#     reverse = (reverse * 10) + lastdigit

# if original == reverse:
#     print("palindrome number")
# else:
#     print('Not palindrome')


# armstrong number

# n = int(input("enter num: "))

# original = n
# sum = 0
# digits = len(str(n))
# while (n > 0):
#     lastdigit = n % 10
#     sum = sum + (lastdigit ** digits)
#     n = n // 10

# if original == sum:
#     print("Armstrong")
# else:
#     print('Not armstrong')


# n = int(input('enter the number: '))


# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)


# n = int(input('enter the number: '))

# import math

# factors = []

# root = int(math.sqrt(n))
# for i in range(1, root +1 ):
#     if n % i == 0:
#         factors.append(i)
#         if((n//i)!= i):
#             factors.append(n//i)

# factors.sort()

# for f in factors:
#     print(f)

# prime or not 

# n = int(input('enter the number: '))

# count = 0

# for i in range(1, n +1):
#     if n % i == 0:
#         count = count+1

# if count == 2:
#     print('prime number')

# else:
#     print('not a prime number')


# n = int(input('enter the number: '))

# import math
# count = 0
# root = int(math.sqrt(n))

# for i in range(1, root +1):
#     if n % i == 0:
#         count = count+1
#         if (n // i)!= i:
#             count = count+1

# if count == 2:
#     print('prime number')

# else:
#     print('not a prime number')


# GCD of numbers

# n1 = int(input("enter num 1: "))
# n2 = int(input("enter num 2: "))

# for i in range(1, min(n1,n2)):
#     if (n1 % i == 0 & n2 % i == 0):
#         gcd = i
# print(gcd)

# other method of gcd

# n1 = int(input("enter num 1: "))
# n2 = int(input("enter num 2: "))

# for i in range(min(n1,n2), 0, -1):
#     if (n1 % i == 0 and n2 % i == 0):
#         print(i)
#         break

# n1 = int(input("enter num 1: "))
# n2 = int(input("enter num 2: "))

# while (n1 > 0 and n2 > 0):
#     if n1 > n2:
#         n1 = n1 % n2 
#     else:
#         n2 = n2 % n1
# if n1 == 0:
#     print(n2)
# elif n2 == 0:
#     print(n1)

# # else not required just for sake of easy understanding
# else:
#     print('nothing')


##   RECURSION 

# count = 0

# def fun():
#     global count
#     if count == 3:
#         return
#     else:
#         print(count)
#         count += 1
#         fun()

# fun()

# print name n times

# n = int(input("enter n: "))

# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)
#     print(n)

# fun(n)


# print linearly from 1 to N

# n = int(input("enter n : "))

# def fun(n):
#     if n ==0:
#         return
#     fun(n-1)
#     print(n)

# fun(n)

# print linearly from N to 1

# n = int(input("enter n : "))

# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     fun(n-1)

# fun(n)


# print 1 to N using Backtracking

# n = int(input("enter n : "))

# def fun(n):
#     if n ==0:
#         return
#     fun(n-1)
#     print(n)

# fun(n)


# print N to 1 using backtracking

# n = int(input("enter n : "))

# def fun(i,n):
#     if i > n:
#         return
#     fun(i + 1, n)
#     print(i)

# fun(1,n)



# summation or sum of first N numbers

# n = int(input("enter the number: "))

# sum = 0

# def fun(i,n):
#     global sum
#     if i > n:
#         return
#     sum = sum + i
#     fun(i +1,n)

# fun(1,n)
# print(sum)


# factorial of a number

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)

# n = int(input("enter number: "))
# print(fact(n))


# sum of first N numbers in pure Recursion way


# n = int(input("enter a number: "))

# def fun(n):
#     if n == 0:
#         return 0
#     return n + fun(n-1)

# print(fun(n))


# Factorial  of  N in pure Recursion way



# def fun(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fun(n-1)

# n = int(input("enter N : ")) 
# print(fun(n))


# reverse an array using recursion

# arr = list(map(int, input("enter numbers: ").split()))

# def fun(arr,n):
#     if n == len(arr):
#         return
#     fun(arr, n+1)
#     print(arr[n], end=" ")

# fun(arr, 0)


# palindrome or not using recursion


# s = input("enter string: ")
# rev =[]

# def fun(s,n):
#     if n == len(s):
#         return
#     fun(s, n+1)
#     rev.append(s[n])

# fun(s, 0)

# if list(s) == rev:
#     print('palindrome')
# else:
#     print('not a palindrome')



# palindrome or not using recursion leetcode


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # cleaning all the things except alphanumerics

#         clean = ""
#         for ch in s:
#             if ch.isalnum():
#                 clean += ch.lower()
#         rev = []

#         def fun(n):
#             if n == len(clean):
#                 return
#             fun(n+1)
#             rev.append(clean[n])
#         fun(0)
#         return list(clean) == rev


# palindrome 2nd method 


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # step 1: clean string
#         clean = ""
#         for ch in s:
#             if ch.isalnum():
#                 clean += ch.lower()

#         # step 2: recursion
#         def fun(n):
#             if n >= len(clean) // 2:
#                 return True
#             if clean[n] != clean[len(clean) - n - 1]:
#                 return False
#             return fun(n + 1)

#         return fun(0)


# Multiple recursion calls

# fibnocci numbers

# class Solution:
    # def fib(self, n: int) -> int:
    #     if (n<=1):
    #         return n
    #     last = self.fib(n-1)
    #     slast = self.fib(n-2)

    #     return last + slast
    #     print(fib(self.n))

# n = int(input())
# def fib(n):
#         if (n<=1):
#             return n
#         last = fib(n-1)
#         slast = fib(n-2)

#         return last + slast
# print(fib(n))


# n = int(input())
# def fib(n):
#         ans = [0,1]

#         for i in range(2,n+1):
#             ans.append(ans[i-1] + ans[i - 2])
#         return ans
# print(fib(n))
        












    

    

