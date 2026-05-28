### ARRAYS EASY QUESTIONS

## find largest in an array

# arr = list(map(int,input("enter array numbers: ").split()))

# def sort(arr):
#     arr.sort()

#     return arr[-1]

# print('largest element: ', sort(arr))

## optimal approach

# arr = list(map(int,input("enter array numbers: ").split()))

# for i in range(0, len(arr)):
#     max = arr[0]
#     if arr[i] > max:
#         max = arr[i]
#         i += 1

# print(max)

## second largest element
# Brute force approach


# arr = list(map(int,input("enter array numbers: ").split()))

# def sort(arr):
#     arr.sort()

#     return arr[-2]
# print(' second largest element: ', sort(arr))


## Optimal approach

# arr = list(map(int,input("enter array numbers: ").split()))

# n = len(arr)

# def secondsmall(arr,n):
#     if n < 2:
#         return -1
    
#     small = float('inf')
#     s_small = float('inf')

#     for i in range(n):
#         if arr[i] < small:
#             s_small = small
#             small = arr[i]
        
#         elif arr[i] < s_small and arr[i] != small:
#             s_small = arr[i]

#     return s_small

# def secondlarge(arr,n):
#     if n < 2:
#         return -1
    
#     large = float('-inf')
#     s_large = float('-inf')

#     for i in range(n):
#         if arr[i] > large:
#             s_large = large
#             large = arr[i]
        
#         elif arr[i] > s_large and arr[i] != large:
#             s_large = arr[i]

#     return s_large

# print('second smallest : ', secondsmall(arr,n))
# print('second largest : ', secondlarge(arr,n))


### Left rotate array by k places to the right


# arr = list(map(int,input("enter array numbers: ").split()))

# k = int(input("enter k value: "))

# n = len(arr)

# k = k % n

# new_array = []

# for i in range(n-k, n):
#     new_array.append(arr[i])
# for i in range(0,n-k):
#     new_array.append(arr[i])

# for i in range(0,n):
#     arr[i] = new_array[i]

# print(new_array)


## Duplicate value removal using 2 arrays

# arr = list(map(int,input("enter array numbers: ").split()))

# n = len(arr)

# new_list = []

# for i in range(n):
#     if arr[i] not in new_list:
#         new_list.append(arr[i])
#     else:
#         i += 1

# print(new_list)


## duplicate value removal using single array

# nums = list(map(int,input("enter array numbers: ").split()))

# def duplicate(nums):
#     if len(nums) == 0:
#         return 0

#     i = 0  # pointer for unique elements

#     for j in range(1, len(nums)): 
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]

#     return i + 1

# k = duplicate(nums)

# print('k', k)
# print("unique elements: ", nums[:k])




## SECOND LARGEST ELEMENT

#

# arr = list(map(int,input("enter array numbers: ").split()))
# n = len(arr)

# def sort(arr):
#     arr.sort()
#     large = arr[-1]

#     for i in range(n-2, -1,-1):
#         if arr[i] != large:
#             sec_large = arr[i]
#             print(sec_large)
#             break
# sort(arr)


# BETTER APPROACH


# arr = list(map(int,input("enter array numbers: ").split()))

# n = len(arr)

# large = arr[0]

# for i in range(0,n):
#     if arr[i] > large:
#         large = arr[i]
# print(large)

# slarge = -1
# for i in range(0,n):
#     if arr[i] > slarge and arr[i] != large:
#         slarge = arr[i]
# print(slarge)


## check if array is sorted or not

# nums = list(map(int, input("Enter array: ").split()))

# def check(nums):
#     count = 0
#     n = len(nums)

#     for i in range(n):
#         if nums[i] > nums[(i + 1) % n]: 
#                 count += 1
#     return count <= 1

# print(check(nums))


## ROTATING ARRAY BY ONE PLACE

# arr = list(map(int, input("Enter array: ").split()))

# n = len(arr)

# temp = arr[0]

# for i in range(1, n):
#     arr[i-1] = arr[i]

# arr[n-1] = temp

# print(arr)


## ROTATE ARRAY BY K ELEMENTS TO LEFT 

# arr = list(map(int, input("Enter array: ").split()))

# n = len(arr)

# k = int(input("enter k value: "))

# k = k % n

# temp = []
# for i in range(0,k):
#     temp.append(arr[i])

# for i in range(k,n):
#     arr[i - k] = arr[i]

# for i in range(n-k, n):
#     arr[i] = temp[i-(n-k)]

# print(arr)

## MOVE ZEROS TO LAST

# arr = list(map(int, input("Enter array: ").split()))

# def move_zeros(arr):
#     non_zeros = [ x for x in arr if x != 0]
#     return non_zeros + [0] * (len(arr) - len(non_zeros))
# print(move_zeros(arr))


# arr = [0, 1, 0, 3, 12]

# def move_zeros(arr):
#     zeros = []
#     non_zeros = []

#     for x in arr:
#         if x == 0:
#             zeros.append(x)
#         else:
#             non_zeros.append(x)

#     return non_zeros + zeros

# print(move_zeros(arr))


## leetcode

# class Solution:
#     def moveZeroes(nums) -> None:
#         zeros = []
#         non = []

#         for i in nums:
#             if i == 0:
#                 zeros.append(i)

#             else:
#                 non.append(i)
                
#         result = non + zeros
        
#         for i in range(len(nums)):
#             nums[i] = result[i]



## BRUTE FORCE

# arr = list(map(int, input("Enter array: ").split()))
# def move_zeros(arr):
#     n = len(arr)
#     temp = []

#     for i in range(0,n):
#         if arr[i] != 0:
#             temp.append(arr[i])
#     nz = len(temp)

#     for i in range(0, nz):
#         arr[i] = temp[i]

#     for i in range(nz, n):
#         arr[i] = 0
#     return arr


# print(move_zeros(arr))

## OPTIMAL APPROACH


# arr = list(map(int, input("Enter array: ").split()))
# def fun(arr):
#     n = len(arr)

# ## we can also use put j =-1 
#     j = 0 

#     for i in range(0, n):
#         if arr[i] == 0:
#             j = i
#             break

#     for i in range(j+1, n):
#         if arr[i] != 0:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
#     return arr

# print(fun(arr))


##  LINEAR SEARCH

#

# arr = list(map(int, input("Enter array: ").split()))
# n = len(arr)
# num = int(input("enter num to search: "))

# def linear(arr):
#     for i in range(0, n):
#         if arr[i] == num:
#             return i
#     return -1

# result = linear(arr)

# if result != -1:
#     print('found at index: ', result)

# else:
#     print('not found')


## UNION OF TWO SORTED ARRAYS

#

# arr1 = [1,2,2,3,4,5]
# arr2 = [2,2,5,6,7]

# s = set()

# for i in arr1:
#     s.add(i)

# for i in arr2:
#     s.add(i)

# print('set',s)

# union = []

# for i in s:
#     union.append(i)

# print(union)


# x = [1,2,2,3,2,6,3,9]
# y = [2,2,5,6,5,8]

# x.sort()
# y.sort()

# a = x
# b = y

# n1 = len(a)
# n2 = len(b)

# i = 0
# j = 0

# union = []

# while(i < n1 and j < n2):
#     if a[i] <= b[j]:
#         if len(union) == 0 or union[-1] != a[i]:
#             union.append(a[i])
#         i += 1
#     else:
#         if len(union) == 0 or union[-1] != b[j]:
#             union.append(b[j])
#         j += 1


# while(j < n2):
#     if len(union) == 0 or union[-1] != b[j]:
#             union.append(b[j])
#     j += 1

# while(i < n1):
#     if len(union) == 0 or union[-1] != a[i]:
#             union.append(a[i])
#     i += 1

# print(union)
    


## TWO SUM

##   

# arr = [2,8,7,5,6]

# n = len(arr)

# target = 9

# for i in range(0,n):
#     for j in range(i + 1, n):
#         if arr[i] + arr[j] == target:
#             print("indexes are ", i,j)


# arr = [2,8,7,5,6]

# n = len(arr)

# target = 9

# hash = {}

# def two_sum(arr):
#     for i in range(0,n):
#         comp = target - arr[i]

#         if comp in hash:
#             return [hash[comp], i]
#         else:
#             hash[arr[i]] = i

# print(two_sum(arr))



###  CONSECUTIVE ONES 

## 

# arr = [1,1,0,9,1,1,1,1]
# count = 0
# maxi = 0
# for i in range(len(arr)):
#     if arr[i] == 1:
#         count += 1

#     else:
#         count = 0

#     maxi = max(maxi,count)

# print(maxi)


###  ONE NUMBER ONCE AND OTHERS TWICE

# 

# arr = [7,2,2,4,5,4,5]

# hash = {}

# for i in range(len(arr)):
#     if arr[i] in hash:
#         hash[arr[i]] += 1

#     else:
#         hash[arr[i]] = 1

# for num in hash:
#     if hash[num] == 1:
#         print(num)


### USING XOR OPERATOR 

# arr = [7,2,2,4,5,4,5]
# def singlenumber(arr):
#     ans = 0

#     for num in arr:
#         ans ^= num
#     return ans
# print(singlenumber(arr))


## MISSING NUMBER 
#
# arr = [1,2,3,4,5,6,8]

# n = len(arr) + 1

# for i in range(1, n+1):
#     for j in range(n-1):
#         if arr[j] == i:
#             break

#     if arr[j] != i:
#             print(i)

## better approach using sum of arr intergers

# arr = [1,2,3,4,5,6,8]

# n = len(arr) + 1

# num = sum(arr)

# expsum = n * (n + 1) // 2

# missing = expsum - num

# print(missing)

# arr = [1,0,2,0,1,2,0]

# def three_pointer(arr):
#     low = 0
#     # low is used to keep the 0's behind it or in the place of low it will not change until the value is 0
#     mid = 0
#     # this will track all the 0's in the array if found it will swap with non zero low with 0 at mid
#     high = len(arr) - 1

#     while (mid <= high):
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             mid += 1
#             low += 1

#         elif arr[mid] == 1:
#             mid += 1
#         else:
#             arr[mid] , arr[high] = arr[high] , arr[mid]
#             high -= 1
#     return arr

# print(three_pointer(arr))



