### SORTING

## Selection sort ascending order

# n = list(map(int,input("enter array numbers: ").split()))

# for i in range(len(n)):
#     mini = i
#     for j in range(i + 1,len(n)):
#         if(n[j] < n[mini]):
#             mini = j
#     n[i], n[mini] = n[mini], n[i]
# print("sorted array: ", n)


## explanation for the above code

# arr = [5, 3, 2, 4, 1]

# for i in range(len(arr)):
#     mini = i
#     print(f"\nPass {i}: starting mini index = {mini}, value = {arr[mini]}")

#     for j in range(i + 1, len(arr)):
#         print(f"  Compare arr[{j}] = {arr[j]} with arr[{mini}] = {arr[mini]}")
#         if arr[j] < arr[mini]:
#             mini = j
#             print(f"  → New mini found at index {mini}, value = {arr[mini]}")

#     arr[i], arr[mini] = arr[mini], arr[i]
#     print(f"After swap: {arr}")


## Selection sort descending order

# n = list(map(int,input("enter array numbers: ").split()))

# for i in range(len(n)):
#     max = i
#     for j in range(i + 1,len(n)):
#         if(n[j] > n[max]):
#             max = j
#     n[i], n[max] = n[max], n[i]
# print("sorted array: ", n)

## BUBBLE SORT

# sorted order using bubble sort

# n = list(map(int,input("enter array numbers: ").split()))

# for i in range(len(n)-1, 0, -1):
#     for j in range(0, i):
#         if(n[j] > n[j+1]):
#             n[j] , n[j+1] = n[j+1], n[j]
# print("sorted order: ", n)


# Bubble sort high to low


# n = list(map(int,input("enter array numbers: ").split()))

# for i in range(len(n)-1, 0, -1):
#     for j in range(0, i):
#         if(n[j] < n[j+1]):
#             n[j] , n[j+1] = n[j+1], n[j]
# print("sorted order: ", n)

## INSERTION SORT

## Insertion sort low to high

# n = list(map(int,input("enter array numbers: ").split()))

# for i in range(1, len(n)):
#     j = i
#     while (j > 0 and n[j-1] > n[j]):
#         n[j-1], n[j] = n[j] , n[j-1]
#         j -= 1
# print("sorted order : ", n)


## insertion high to low


# n = list(map(int,input("enter array numbers: ").split()))

# for i in range(1, len(n)):
#     j = i
#     while (j > 0 and n[j-1] < n[j]):
#         n[j-1], n[j] = n[j] , n[j-1]
#         j -= 1
# print("sorted order : ", n)


## MERGE SORTING

## merge sort questions

# arr = list(map(int,input("enter array numbers: ").split()))


# def merge(arr,low,mid,high):
#     temp = []
#     left = low
#     right = mid + 1

#     while(left <= mid and right <= high):
#         if( arr[left] <= arr[right]):
#             temp.append(arr[left])
#             left += 1

#         else:
#             temp.append(arr[right])
#             right += 1
    
#     while(left <= mid):
#         temp.append(arr[left])
#         left += 1

#     while(right <= high):
#         temp.append(arr[right])
#         right += 1

#     for i in range(low, high+1):
#         arr[i] = temp[i - low]


# def ms(arr, low, high):
#     if(low == high):
#         return
    
#     mid = (low + high) // 2

#     ms(arr, low, mid)
#     ms(arr, mid+1, high)
#     merge(arr,low,mid,high)

# ms(arr,0,len(arr)-1)
# print("sorted array: ", arr)



##  QUICK SORT 

# QUICK SORT in ascending order

# arr = list(map(int,input("enter array numbers: ").split()))

# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high
#     while (i < j):
#         while(arr[i] <= pivot and i <= high + 1):
#             i += 1

#         while(arr[j] > pivot and j >= low - 1):
#             j -= 1

#         if(i < j):
#             arr[i], arr[j] = arr[j] , arr[i]
    
#     arr[low] , arr[j] = arr[j], arr[low]
#     return j


# def qs(arr, low, high):

#     if(low < high):
#         pindex = partition(arr, low, high)
#         qs(arr, low, pindex -1)
#         qs(arr, pindex + 1 , high)


# qs(arr, 0, len(arr) -1)
# print('sorted array: ', arr)


## quick sort descending order


# arr = list(map(int,input("enter array numbers: ").split()))

# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low + 1
#     j = high
#     while (i < j):
#         while(arr[i] >= pivot and i <= high):
#             i += 1

#         while(arr[j] < pivot and j >= low):
#             j -= 1

#         if(i < j):
#             arr[i], arr[j] = arr[j] , arr[i]
    
#     arr[low] , arr[j] = arr[j], arr[low]
#     return j


# def qs(arr, low, high):

#     if(low < high):
#         pindex = partition(arr, low, high)
#         qs(arr, low, pindex -1)
#         qs(arr, pindex + 1 , high)


# qs(arr, 0, len(arr) -1)
# print('sorted array: ', arr)


## RECURSIVE INSERTION SORT 


# n = list(map(int,input("enter array numbers: ").split()))

# def insert(n, i):
#     if i == 0:
#         return
    
#     insert(n, i-1)

#     j = i

#     while j > 0 and n[j-1] > n[j]:
#         n[j-1], n[j] = n[j], n[j-1]
#         j -= 1

# insert(n, len(n)-1)
# print(n)


# for i in range(len(n)-1, 0, -1):
#     for j in range(0, i):
#         if(n[j] > n[j+1]):
#             n[j] , n[j+1] = n[j+1], n[j]
# print("sorted order: ", n)


# n = list(map(int,input("enter array numbers: ").split()))

# def bubble(arr, n):
#     if n == 1:
#         return
#     for j in range( n - 1):
#         if arr[j] > arr[j+1]:
#             arr[j] , arr[j+1] = arr[j+1], arr[j]
#     bubble(arr,n - 1)

# bubble(n, len(n))

# print(n)



