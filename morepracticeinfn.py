# def multiply(a,b,c,d):
#     print(a*b*c*d)
# multiply(1,23,32,1)
# # these are position arguments.

# #default arg
# def addn(a,b,c,d=8): #you have to give default values after d otherwise eror will occur.
#     print(a+b+c+d)
# addn(2,3,4,2)

# #keyword argument
# def subtraction(a,b,c):
#     print(a-b-c)
# subtraction(a=1,c=3,b=3)

# # #data structures
# #list
# a=[23,4,5,6]
# a[2]=3
# print(a)
# mutable and ordered nature of list
# a=[1,1,1,1,1]
#duplicate nature of list.

# #transversing on values
# a=[1,2,3,4]
# for i in a:
#     print(i)

# # #transvering on index
# # a=[1,2,3,4]
# # for i in range(0,len(a)):
# #     print(a[i])

# #mthds of list
# #1 append
# a=[1,2,3,4]
# a.append(99)
# a.append("hello")
# # print(a)

# #insert
# a=[1,2,3,5]
# a.insert(3,4)
# print(a)

#use of return
# def hi():
#     return"yqwqdfdq"
# print(hi())

#use of pop
# a=[1,2,3,67,5]
# c=a.pop(3)
# d=a.pop()
# print(a,d,c)

#use of remove 
# a=[1,2,3,5,5] 
# a.remove(5)
# print(a)

# #use of clear
# a=[4,5,6,7]
# a.clear()
# print(a)

# #sort in asc
# a=[1,2,674,3,423,4,5,46]
# a.sort()
# print(a)

#sort in des

# a=[1,3,23,4,35,4,66,5]
# a.sort(reverse=True)
# print(a)

#print all positive and negative no. seperately
# a=[1,-3,4,5,-2,-8]
# neg=[]
# pos=[]
# for i in a:
#     if i>=0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(pos)
# print(neg)

#print avg of all the no.

# l=[10,20,30,40]
# sum=0
# for i in l:
#     sum=i+sum
# avg=sum/len(l)
# print(avg)

# find the greatest element and print its index
# a= [4, 8, 2, 9, 1]
# b= a[0]
# for i in range(len(a)):
#     if a[i]>b:
#         b=a[i]
#         c=i
# print(f"The largest no.is {b} at index {c} ")

# #find the second greatest no.
# a=[4, 6, 2, 9, 7,1]
# lar=a[0]
# seclar=a[0]
# for i in a:
#     if i>lar:
#         seclar=lar
#         lar=i
#     elif i>seclar:
#         seclar=i
# print(seclar)

# check if the list is already nsorted or not
# a= [1, 3,8, 5, 7]
# for i in range(len(a)):
#     if a[i]>a[i+1]:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")







