# for i in range(1,11):
#     if i==45:
#         break
#     print(i)
#     #use of break in for loop

#printing hello word n times

# n=int(input("enter any no."))
# for i in range(n):
#     print("hello")

# # print natural no. from 1 to n
# n=int(input("enter a no."))
# for i in range(1,n+1):
#     print(i)

# print n down to 1 . Reverse the loop.
# n=int(input("enter a no."))
# for i in range(n,0,-1):
#     print(i)

# print the multiplication table of a no.like 5*1=5

# n=int(input("enter a no."))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

#sum of first n natural no.

# n=int(input("enetr a no."))
# a=0
# for i in range(1,n+1):
#     a=a+i
# print(a)

# #factorial of a no.
# n=int(input("enter a no."))
# a=1
# for i in range(1,n+1):
#     a=i*a
# print(a)

# # print sum of all even and odd terms seperately
# n=int(input("enter a no."))
# e=0
# o=0
# for i in range(1,n+1):
#     if i%2==0:
#         e=e+i
#     else:
#         o=o+i
# print(f"the sum of even terms are {e} and sum of odd terms are {o}")

# # print all factors of a no.
# n=int(input("enter a no."))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# #check if a no is perfect or not
# n=int(input("enter a no."))
# f=0
# for i in range(1,n):
#      if n%i==0:
#           f=f+i
# if n==f:
#      print("perfect no.")
# else:
#      print("not a perfect no.")

# to check if a no. is prime or not.
# n=int(input("enter a no."))
# s=0
# for i in range(1,n+1):
#     if n%i==0:
#         s+=1
# if s==2:
#     print("prime no.")
# else:
#     print("noty a prime no.")

# reverse a string witout using built in fn

# n=(input("enter a string"))
# # for i in range(len(n)-1,-1,-1):
# #     print(n[i])

# # check if a string is palindrome or not
# n=input("enter a string.")
# s=""
# for i in range(len(n)-1,-1,-1):
#     s=s+n[i]
# if s==n:
#     print("palindrome string.")
# else:
#     print("not a palindrome string")

# #count letters , digits and special characters in a string
# n=input("enter a string")
# d=0
# char=0
# sp=0
# for i in range(len(n)):
#     if 65<= ord(n[i]) <=90 or 97<=ord(n[i])<=122:
#         char=char+1
#     elif 48<=ord(n[i])<=57:
#         d=d+1
#     else:
#         sp=sp+1
# print(f"no. of digits is {d}, no of special characters is {sp} and no. of alphabet is {char}")

       
