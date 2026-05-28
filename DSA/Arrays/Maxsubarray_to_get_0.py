nums = [9, -3, 3, -1, 6, -5]
hash_map = {}
maxi = 0
sum = 0
for i in range(len(nums)):
    sum += nums[i]

    if sum == 0:
        maxi = i + 1

    elif sum in hash_map:
        length = i - hash_map[sum]

        maxi = max(maxi, length)
    else:
        hash_map[sum] = i

print(maxi)