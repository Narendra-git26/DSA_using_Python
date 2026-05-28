#  generators 
#  we can write our own range function

# def myrange(n):
#     i=0
#     while i<n:
#         yield i
#         i = i+1
# m = myrange(4)
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

# iteration and sequence manipulation 

# sorted 
#  reversed (seq,/)
# slice(start,stop,step)

# sorted(iterable,/,*,key=none,reverse=false)

# list1 = [1,12,7,-3]
# l2 = sorted(list1)
# print(l2)

# list1 = [1,12,7,-3]
# l2 = sorted(list1,reverse=True)
# print(l2)

# list1 = [1,12,7,-3]
# l2 = sorted(list1,key=abs)
# print(l2)

# list1 = [1,12,7,-3]
# rev = reversed(list1)
# print(list(rev))

#  slice(start,stop,step)

# l1 = [ 1,2,3,4,5,6,7,8,9]
# s = slice(5)
# l2 = l1[s]
# print(l2)

# #  iterator 

# l1 = [1,2,3]
# it = iter(l1)
# print(next(it))
# print(next(it))
# print(next(it))



