# n = [2,4,1,3,6,8]

# for i in range(len(n)):
#     mini = i
#     for j in range(i +1, len(n)):
#         if n[j] < n[mini]:
#             mini = j
#     n[i] , n[mini] = n[mini] , n[i]

# print(n)


# n = [2,4,1,3,6,8]

# for i in range(len(n)):
#     max = i
#     for j in range(i +1, len(n)):
#         if n[j] > n[max]:
#             max = j
#     n[i] , n[max] = n[max] , n[i]

# print(n)


# n = [2,4,1,3,6,8]

# for i in range(len(n)-1, 0, -1):
#     for j in range(0,i):
#         if n[j] > n[j + 1]:
#             n[j], n[j+1] = n[j+1], n[j]

# print(n)


# n = [2,4,1,3,6,8]

# for i in range(1, len(n)):
#     j = i
#     while(j > 0 and n[j-1] > n[j]):
#         n[j-1], n[j] = n[j], n[j-1]
#         j -= 1

# print(n)