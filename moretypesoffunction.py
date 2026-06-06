#data type TUPLE

#How to convert a list into tuple.
# a=[1,2,3,4,5,6]
# leo=tuple(a)
# print(leo)

# ordered nature of tuple
# a=(4,4,5,4,6)
# print(a[3])

# #immutable nature of tuple
# a=(1,2,3,4,5)
# a[3]=5             #wrong 
# print(a)      
 
# #mthds of tuple
# a=(1,2,3,4,5,2,2,6)
# print(a.count(2))
# print(a.index(3)
# def students():
#     return "my name is nitya bhatia",3434       # packing and unpacking of tuple.
# b=students()
# intro,no=b
# print(intro)                                    # use of tuple..
# print(no)
# print(type(students()))

#set data type
#set is represented by {}
# a=[2,2,2,4,4,4,6,6,6,7,8,4,4,6,8,0,0]   # set removes duplicates
# b=set(a)                                # unique nature of it.
# print(b)

#hash use
# a={2,3,4,(6571577)}     #we can store only hashable aka immutable thing here 
# b="qweghedqjhg"                    #we can't store items like list..
# print(hash(b))    

#set doen't work on indexes....
#so loop can't work on sets and if we have only one way to run a loop
# l={26,2,3,4,5,6,67,7,}
# for i in l:
#     print(i)

#mthds of set
#1 add
# s={2,3,4,5,9}
# s.add(10)
# print(s)
#2 clear
# # s.clear()
#3.discard- to remove a thing  and remove() is same as discard
# s.discard(9)
# print(s)
# #4.pop - to remove random thing.
# a=s.pop()
# print(s)
# print(a)
# #difference
# s1={1,2,3,4}
# s2={3,4,5,6,7}
# print(s1-s2)
# print(s2.difference(s1))
# difference update =  (-=) this mthd directly saves value in s2 no need of variable.
# s2-=s1
# print(s2)
#intercection-(&)
# print(s2&s1)
# #or
# s2&=s1
# print(s2)
# s3={6,7}
# is subset  <= and returns True or False
# print(s3<=s2)    >=
#super set
# print(s2>=s3)
#symmetric difference   ^  or ^=
# print(s1.symmetric_difference(s2))
# s1^=s2
# print(s1)
#union   |
# print(s1|s2)
# s1|=s2
# print(s1)
