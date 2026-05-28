#  Sum of digits 

# n = int(input("enter the number: "))

# sum = 0

# while (n > 0):
#     last = n % 10

#     sum = sum + last

#     n = n // 10

# print(sum)


# reverse of a number


# n = int(input("enter number: "))

# rev = 0

# while (n>0):
#     last = n % 10
#     rev = (rev *10) + last
#     n = n // 10

# print(rev)


# check if number is palindrome or not

# n = int(input("enter number : "))

# dupe = n 

# rev = 0

# while n > 0:
#     last = n % 10
#     rev = (rev * 10) + last
#     n = n//10

# if dupe == rev:
#     print('palindrome')
# else:
#     print('not palindrome')

# count digits

# n = int(input("enter number : "))


# count = 0

# while n > 0:
#     last = n % 10
#     count = count + 1
#     n = n//10

# print(count)

# find largest number 

# n = int(input("enter number : "))

# largest = 0

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit

#     n = n // 10

# print(largest)


# reverse of a string using recursion

# s = input('enter string: ')

# rev = []

# def fun(s, n):
#     if n == len(s):
#         return
#     fun(s, n+1) 
#     rev.append(s[n])
# fun(s,0)

# print(''.join(rev))


# sum of digits using recursion

# n = input("enter the number : ")

# total = 0

# def fun(i,n):
#     global total
#     if i == len(n):
#         return
#     total = total + int(n[i])
#     fun(i+1,n)

# fun(0,n)
# print(total)

    
# n = int(input("enter the number : "))

# def fun(n):
#     if n == 0:
#         return 0
#     return (n % 10) + fun(n // 10)

# print(fun(n))


# palindrome string using recursion


# s = input('enter string: ').lower()

# rev = []

# def fun(s, n):
#     if n == len(s):
#         return
#     fun(s, n+1)
#     rev.append(s[n])

# fun(s,0)

# print(rev)

# if list(s) == rev:
#     print('palindrome')
# else:
#     print('not')

# counting of digits

# n = int(input("enter number: "))

# count = 0

# def fun(n):
#     global count
#     if n == 0:
#         return
#     digit = n % 10
#     if digit > 0:
#         count += 1
#     fun(n//10) # function never calls itself again
# fun(n)
# print(count)

# Factorial of the number

# n = int(input("enter the number: "))


# def fun(n):
#     if n == 1 or n == 0:
#         return 1
    
#     return n * fun(n-1)

# print(fun(n))

# fibnocci series

# n = int(input("enter the number: "))

# def fun(n):
#     if n <= 1:
#         return n
#     last = fun(n-1)
#     slast = fun(n-2)
#     return last + slast

# print(fun(n))



### HASHING


# finding frequency of a number 

# arr = list(map(int, input("enter the numbers: ").split()))

# hash_arr = [0] * 13 # will take upto 12


# for i in range(0, len(arr)):
#     hash_arr[arr[i]] += 1

# q = int(input())

# while q > 0:
#     num = int(input())
#     print(hash_arr[num])

#     q -= 1


## finding frequencies of a string

# s = input("enter the string: ")

# hashh = [0] * 26

# for i in range(0, len(s)):
#     hashh[ord(s[i]) - ord('a')] +=  1

# q = int(input())

# while q > 0:
#     c = input()
#     print(hashh[ord(c) - ord('a')])
#     q -= 1


# frequencies using mapping 

# s = input("enter the string: ")

# mpp = {}

# for i in range(0, len(s)):
#     mpp[ord(s[i])] = mpp.get(ord(s[i]), 0) + 1

# q = int(input())

# while q > 0:
#     c = input()
#     print(mpp.get(ord(c)))
#     q -= 1


# array mapping frequencies

# arr = list(map(int, input("enter the numbers: ").split()))

# mpp = {}

# for i in range(len(arr)):
#     mpp[arr[i]] = mpp.get(arr[i], 0) + 1

# q = int(input())

# while q > 0:
#     c = int(input())
#     print(mpp.get(c))
#     q -= 1



