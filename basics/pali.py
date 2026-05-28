# palindrome project

# s1 = input("enter the string: ")
# s2 = s1.replace(" ","")
# rev = s2[::-1]
# if s2.casefold() == rev.casefold():
#     print(s1)

# else:
#     palindrome = s2.casefold() + rev.casefold()
#     print(palindrome)


#url parsing project 

# url = input("enter the url: ")

# protocol = url[ :url.find(':')]

# dot1 = url.find('.')
# dot2 = url.find('.',dot1+1)
# domain = url[dot1+1 : dot2]
# page = url[ url.find('/',dot2) : ]

# print("ptotocol: ", protocol)
# print("domain: ", domain)
# print("page : " ,page)

# salary calculation
# work_hours = [int(x) for x in input('enter the hours per day in entire week ,separated by coma ').split()] #list comprehension
# wage = int(input('enter hourly wages'))
# total = sum(work_hours)

# salary = total *wage
# print('salary is : ', salary)

#  removing duplicates 

# l1 = [3,3,5,7,6,9,8,9,3]

# l2=[]

# for x in l1:
#     if x not in l2:
#         l2.append(x)

# print(l2)

#  concatenate all integers into single number 

# l1= [3,5,12,10]
# s1= ''

# for x in l1:
#     s1 += str(x)

# print(int(s1))

# minimum index sum of two lists 

# fav1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']

# fav2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']

# index1 = 10
# index2 = 10

# for i in range(len(fav1)):
#     indx = fav2.index(fav1[i])

#     if i + indx < index1 + index2:
#         index1 = i
#         index2 = indx

# print(fav1[index1],index1+index2)

# overlapping elements of two  list 

# l1 = [10,15,6,9,12,8,4]
# l2 = [14,6,19,4,7,10,11]

# l3 =[]

# for x in l1:
#     if x in l2:
#         l3.append(x)
# print(l3)

# find the number of occurencies of each item

# l1= ['A','B','C','D','E','A','B','E','B','D','B','E']

# result=[]

# for x in l1:
#     if x not in result:
#         result.append(x)
#         count = l1.count(x)
#         result.append(count)

# print(result)

# telegram morse code

# codes = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___']

# text = 'deface'

# morse_str = ''

# for x in text:
#     morse_str = morse_str + codes[ord(x)-97] + " "

# print(morse_str)

# adding two matrix 

# l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2= [[5,6,7,8],[5,6,7,8],[5,6,7,8]]

# l3=[]

# for i in range(3):
#     s = []
#     for j in range(4):

#         r=l1[i][j]+l2[i][j]
#         s.append(r)
#     l3.append(s)

# print(l3)

#  transpose of a matrix

# l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2=[]

# for i in range(4):
#     s=[]
#     for j in range(3):
#         s.append(l1[j][i])
#     l2.append(s)
# print(l2)

# word starting with a given letter 

# food = ['pizza','nuggets','hotdog','noodles','pasta','burger'] 

# letter = input('enter the letter :')

# for x in food:
#     if x.startswith(letter):
#         print(x)


# l1=[None]*10
# print(l1)



# leetcode #1 problem

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         h = {}  # dictionary to store num -> index
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in h:
#                 return [h[complement], i]
#             h[num] = i


# l2 = list('abcde')
# print(l2)

# l1 = [1,2,3,4]
# for x in l1:
#     print(x)

# l1 = [123, 'abc' ,12.25]
# print(l1)
# l1.append(25)
# print(l1)
# l1.remove(123)
# print(l1)

# indexing and slicing 

# read / write in index and slicing 

# l1 = [1,2,3,4,5,6,7]
# print(l1[4])

# print(l1[:])
# print(l1[-5:6])
# print(l1[: :-1])
# writing for indexing and slicing 

# l1 = [1,2,3,4,5,6,7]
# l1[3]= [10,11]
# print(l1)
# l1[9:9]= [10]
# print(l1)

# l2 = [10,11,12,13,14,15]
# l3= l1+l2
# print(l3)
# l4 = l2 + [16]
# print(l4)

# l1.extend([8,9,17])
# print(l1)

# l1 = [1,2,3,4,5,6,7]
# for i in range(len(l1)):
#     print(i,l1[i])

# l1 = [1,2,3,4,5,6,7]
# i = 0
# while (i<len(l1)):
#     print(i,l1[i])
#     i = i+1

# l1 = [1,2,3,4,5,6,2,1,7]
# print(l1.index(2,5))
# index.(element,start index,end index)

# l1 = [1,2,3,4,5,6,7,2,2,3,4,2]
# print(l1.count(2))

# l1 = [1,2,3,10,112,17,4,5,6,7]
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# # list comprehensions 

# l = [expression for item in iterable]  Syntax

# l1 = [x for x in range(1,7)]
# print(l1)


# l1 = [x**2 for x in range(1,7)]
# print(l1)


# l1 = [x for x in 'abc12@b&CV' if x.isalpha()]
# print(l1)

# # nested list 


# l1 = [1,2,3,4,5,6,7,8,9]
# l2=[[1,2],2,6,[10,11]]
# print(l2[0][1])
# print(l1[5])

# dictionary data type 
#  dictionary comprehensions 
#  iterable pairs zip function  enumerate function  dict 
# d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
# l1 = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]

# d1 = { x:y for x,y in l1}
# print(d1)

# zip function 
# l1 = [1,2,3,4] 
# l2= ['one','two','three','four']

# d1 = {x:y for x,y in zip(l1,l2)}
# print(d1)

# enumerate function 
# l1= ['one','two','three','four']

# d1= {x:y for x,y in enumerate(l1,start=1)}
# print(d1)

#  looping over dictionary 

#  keys()
# values()
# items()


# d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
# for i in d1:
#     print(i,d1[i])

# d1.keys()
# for x in d1.keys():
#     print(x,d1[x])

# d1.values()
# for x in d1.values():
#     print(x)

# d1.items()
# for x,y in d1.items():
#     print(x,y)

# d1.get(5,'missing')

# d1.setdefault(5)
# print(d1)

# 5 value will be none 

# d1.setdefault(5,'undefined')
# print(d1)

# dictionary methods 

# update(dictionary)
# fromkeys(sequence,default)
# copy()
# pop(key,alt_value)
# popitem()
# clear()

# d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
# d2 = {5:'five'}
# d1.update(d2)
# print(d1)

# l1 = [1,2,3,4]
# d1= dict.fromkeys(l1)
# print(d1)

# d1= dict.fromkeys(l1,'unknown')
# print(d1)

# d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
# d2 = d1.copy()
# print(d2)

# d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
# # d1.pop(2)
# # print(d1)

# # d1.pop(5,'missing')
# # print(d1)

# d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
# d1.popitem()
# print(d1)

# d1.clear()
# print(d1)

# challenges 
# birthday of a person

# birthdays = {
#     'sachin':'03/12/2004',
#     'ramu':'05/10/2001',
#     'nanu':'04/02/2002',
#     'samantha':'02/11/2003'
# }

# name = input('enter the name: ')

# if name in birthdays:
#     print('Mr./Miss {} was born on {}'.format(name,birthdays[name]))

# else:
#     print('Name not found')

# d = dict()
# for x in enumerate(range(2)):
#     d[x[0]]=x[1]
#     d[x[1]+7] = x[0]
# print(d)

# a = {i:i*i for i in range(6)}
# print(a)

# finding longest and shortest meaning in dictionary

# dict1 = { "piece" : 'portion of an object or material,produced by cutting',
#           'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
#           'area': 'a region or part of a town,a country,or other world',
#           'visit':'go to see and spend time with(someone)',
#           'with': 'having or processing',
#           'small': 'less than normal'}

# keys = list(dict1.keys())
# values = list(dict1.values())
# lens = [len(x) for x in values]

# max_len = max(lens)
# min_len = min(lens)

# max_index = lens.index(max_len)
# min_index = lens.index(min_len)

# print('max',keys[max_index],values[max_index])
# print('min',keys[min_index],values[min_index])

# countries names

# countries = {}

# for i in range(4):
#     name = input('enter country name ')
#     if name[0].upper() not in countries:
#         countries[name[0].upper()] = [name]

#     else:
#         countries[name[0].upper()].append(name)

# print(countries)

#  roman number to integer number 

# roman = {'I' : 1,'V':5,'X':10,'L':50,'C':100,'D':100,'M':1000}

# number = input('enter the roman number in upper cases :')

# deci_num = 0

# i = 0

# while i< len(number):
#     if i+1 < len(number) and roman[number[i]] < roman[number[i+1]]:
#         deci_num += roman[number[i+1]] - roman[number[i]]
#         i +=1

#     else:
#         deci_num += roman[number[i]]
#         i += 1

# print(deci_num)

# STUDENT DETAILS 

# students = {}

# for i in range(3):
#     name = input('enter the name:')
#     roll=int(input('enter roll number:'))
#     dept = input('enter department:')

#     students[name] = {'roll':roll,'name':name,'dept':dept}

# print(students)

# FUNCTIONS 
# What are functions

#  function is a piece of code which performs specific tasks
#  it is reusable code

# def fun1(<parameter>):
#     ______
#     ______
#     return result

#  it supports team based development 
#  built-in and  user defined function
#  takes input as parameter and gives resulta s output

# how to write a functions 

# def fun_name(<parameter list>):
#     stamt 1;
#     stamt 1;
#     stamt 1;
#     return Value 

#  volume of a cuboid 

# def volume(length,breadth,height):
#     vol = length*breadth*height
#     return vol

# v = volume(10,5,3)
# print(v)

#  how parameteres are passed

# POSITIONAL vs KEYWORD ARGUMENTS

# def volume(length,breadth,height):
#     print(length,breadth,height)
#     vol = length*breadth*height
#     return vol

# v = volume(5,10,3)
# print(v)
#  it will pass in same order 

# def volume(length,breadth,height):
#     print(length,breadth,height)
#     vol = length*breadth*height
#     return vol

# v = volume(height=3,length=10,breadth=5)
# print(v)

# mixed arguments
# v = volume(3,10,height=5)
# print(v)

#  TUPLE 
# tuple is immutable once declared cant chnage their values 

# in tuple length is also not modified 

# t1 = tuple(range(1,7))
# print(t1)

# t1 = tuple([1,7])
# print(t1)

#  Traversal 
# t1 = (1,2,3,4,5,6.7)
# for x in t1:
#     print(x)

# Tuple comprehensions
# t1= tuple(x**2 for x in range(1,5))
# print(t1)

# t7=tuple(x.lower() for x in 'PYTHon')
# print(t7)

# t8= tuple(x for x in 'Ab#*&%vbmg' if x.isalpha())
# print(t8)

# t8= (*(x for x in 'Ab#*&%vbmg' if x.isalpha()),)
# print(t8)

# Tuple indexing and slicing 

# t1 = (1,2,3,4,5,6,7,8,9)
# t2 = t1[2:5]
# print(t2)

# concatenation and repetition 

# t1=(1,2,3,4)
# t2= ('a','b','c','d')
# t3 = t1+t2
# print(t3)

# t1=(1,2,3,4)
# t2= t1 * 3
# print(t2)

#  packing and unpacking

# t1=(1,2,3,4,5)
# *a,b,c=t1
# print(a,b,c)


# t1=(1,2,3,4,5)
# a,*b,c=t1
# print(a,b,c)


# Palindrome of an string 

# text = 'radar'

# is_palindrome = (text == text[::-1])

# print('is palindrpme',is_palindrome)

# Functions

# def volume(l=1,b=1,h=1):
#     v=l*b*h
#     return v
# v = volume()
# print(v)

# Positional and Keyword arguments

# def fun(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)

# fun(5,10,c=4,d=1,e=2,f=3)
# print(fun)

# def fun(a,b,c,/,*,d,e,f):
#         pos-only  key-only

#  variable length positional arguments 

# ex:- print()

# print(10,1.25,"hello",True)
# below args with * will take as many arguments as possible just like print function 
# 
# def fun(*args):
#     for x in args:
#         print(x)

# fun(2,3,4,'hello',1.25)

# def fun(*args):
#     print(args)

# fun(1,2,3,4)

# 
# def fun(*args):
#     for x in args:
#         if type(x)==int:
#             print(x)

# fun(2,3,4,'hello',1.25)

# 
# def fun(a,b,*args):
#     print(a,b,args)

# fun(2,3,4,'hello',1.25)

# unpacking using * symbol
# def fun(*args):
#     print(args,len(args))

# l1 =[10,20,30]
# fun(*l1)

# 
# def fun(*args):
#     print(args,len(args))

# l1 =[10,20,30]
# fun(l1)

#  variable length key-word only arguments 
# def fun(**kwargs):
#     print(kwargs)

# fun(a=1,b=2,c=3)
#  it will form dictionary will take keys and gives its values 

#  double **kwargs is used for variable key_oword only lenth arguments
# def fun(**kwargs):
#     for item in kwargs.items():
#         if item[1]==2:
#             print(item[0])

# fun(a=1,b=2,c=3)
# here items refer to keys as a,b,c 
#  a:1 will defined as; a as 0 : and its value 1 as 1;

#  cant have arguments after keyword args

# def fun(a,b,**kwargs):
#     print(a,b,kwargs)

# fun(1,2,c=3)

#  multiple results

# def fun(a,b,c):
#     sum = a+b+c
#     prod = a*b*c
#     return sum,prod

# print(fun(5,6,7))

# def result(m1,m2,m3):
#     total = m1+m2+m3
#     average =total/3

#     if average >=45:
#         grade='pass'

#     else :
#         grade='fail'

#     return total,average,grade

# print(result(55,66,46))


#  iterators and generators 
# iterator = iter (built in function in python)
# next

# l1 = [1,2,3]
# it =iter(l1)
# my = next(it)
# print(my)
# my=next(it)
# print(my)

# it works on tuple too and not on set 

# l1 = (1,2,3)
# it =iter(l1)
# my = next(it)
# print(my)

# in dictionary it will only give an keys but not values 

# l1 = {1:'one',2:'two',3:'three'}
# it =iter(l1)
# my = next(it)
# print(my)

# #  on strings 

# l1 = 'hello'
# it =iter(l1)
# my = next(it)
# print(my)

#  in range function



# r = range(3,10)

# it =iter(r)
# my = next(it)
# print(my)
# my = next(it)
# print(my)
# my = next(it)
# print(my)


