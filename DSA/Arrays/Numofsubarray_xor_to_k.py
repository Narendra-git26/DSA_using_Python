# Better solution
# Time O(n^2)
# space = O(1) constant space
# nums = [4,2,2,6,4]
# k = 6
# count = 0
# n = len(nums)
# for i in range(0,n):
#     xor = 0
#     for j in range(i , n):
#         xor = xor ^ nums[j]
#
#         if xor == 6:
#             count += 1
# print(count)

# time = O(n)
# space = O(1) constant space no extra space taken
nums = [4,2,2,6,4]

k = 6
count = 0
hash_map = {0:1}
xor = 0
for i in range(0,len(nums)):
    xor = xor ^ nums[i]

    if xor == k:
        count += 1
    x = xor ^ k
    if x in hash_map:
        count += hash_map[x]
    hash_map[xor] = hash_map.get(xor, 0) + 1
    print(count)




