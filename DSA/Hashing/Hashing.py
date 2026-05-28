# arr = list(map(int, input("enter the numbers: ").split()))

# hash_arr = [0] * 13

# for i in range(len(arr)):
#     hash_arr[arr[i]] += 1

# q = int(input())

# while(q > 0):
#     num = int(input())
#     print(hash_arr[num])
#     q -= 1


# character frequency hashing

# s = input("enter a string: ").lower()

# hashh = [0] * 26

# for i in range(len(s)):
#     hashh[ord(s[i]) - ord('a')] += 1

# q = int(input())

# while (q > 0):
#     c = input()
#     print(hashh[ord(c)-ord('a')])
#     q -= 1



# arr = list(map(int, input("enter the numbers: ").split()))

# mpp = {}

# for i in range(len(arr)):
#     mpp[arr[i]] = mpp.get(arr[i],0) + 1

# q = int(input("enter number of queries: "))

# while(q > 0):
#     num = int(input("Enter number to get the frequency : "))
#     print(mpp.get(num,0))
#     q -= 1


# from collections import Counter

# arr = list(map(int, input().split()))
# mpp = Counter(arr)

# q = int(input())

# while q > 0:
#     num = int(input())
#     print(mpp[num])
#     q -= 1


# finding frequency using mapping


# s = input("enter a string: ")

# mpp = {}

# for i in range(len(s)):
#     mpp[ord(s[i])] = mpp.get(ord(s[i]),0) + 1

# q = int(input("enter number of queries: "))

# while(q > 0):
#     num = input("Enter character to get the frequency : ")
#     print(mpp.get(ord(num)))
#     q -= 1






















