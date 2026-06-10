# there are two types of errors:- fixable and unfixable
#1.unfixable error
# syntax error
# indentation error
#tab error-mixing tabs and spaces

#2.fixable error which are also known as exception
#zero division error   dividing a no. by 0
# TypeError            concatinating a string and a int
# ValueError            giving input a string when u have to give int
# FileNotFoundError

# exception handling
# a=int(input('enter a no.'))
# b=int(input("enter another no."))
# try:
#     print(a/b)
# except Exception as err: 
#     print(f"sorry an error ocurred as dividing by {err}")
# else:
#     print("no error occured")
# finally:
#     print("i will run no matter whether the error occur or not.")
# n=input("enter your name")
# print(n)
# # error:- raise
# a=int(input("enter your age"))
# if a<18:
#     raise TypeError("you are not eligible")
# print("you are eligible")


#file handling.
#to create a new file using code  using x
# open("leo.txt","x")

# to create a new file using w and also write 
# file=open("rose.py","w")
# data=input("what u want to write")
# file.write(data)
# file=open("leo.txt","w")
# data=input("what do u want to write")
# file.write(data)
#read
file=open("leo.txt","a")
print(file.read())
