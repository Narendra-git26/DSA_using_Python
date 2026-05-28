# arr = [1,2,3,1,2,1,1,4,2,3]
# n = len(arr)
# len = 0
# k = 3
# for i in range(0,n):
#     sum = 0
#     for j in range(i,n):
#         sum += arr[j]

#         if sum == k:
#             len = max(len, (j-i) + 1)
# print(len)


# arr = [1,2,1,0,1]

# def fun(arr):
#     k = 4
#     left = 0
#     maxi = 0
#     sum = 0

#     for i in range(len(arr)):
#         sum += arr[i]

#         while sum > k and left <= i:
#                 sum -= arr[left]
#                 left += 1

#         if sum == k:
#             maxi = max(maxi, (i - left) + 1)
#     print(maxi)

# fun(arr)


# arr = [1,-2,1,3,0,1]

# def fun(arr):
#     k = 4
#     sum_map = {}
#     maxi = 0
#     sum = 0

#     for i in range(len(arr)):
#         sum += arr[i]

#         if sum == k:
#             maxi = i + 1
#         rem = sum - k
#         if rem in sum_map:
#             maxi = max(maxi, i- sum_map[rem])

#         if rem not in sum_map:
#              sum_map[sum] = i
#     print(maxi)

# fun(arr)





 