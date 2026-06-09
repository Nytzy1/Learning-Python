#data type: dictionaries
# a={}
# # print(type(a))
# a={10:20,20:30,30:40,40:50}    # key works as custom indexing......
# print(a)
# print(a[30])

#vanilla python....

# how to create a new key value pair......
# a[50]=60
# print(a)                  #directly stored
#updating a value
# a[10]=100
# print(a)

# methods of dictionaries
#1.clear
# a.clear()
# print(a)
#2.from keys  # basically ceate a new dictionary
# q=a.fromkeys([10,20,30,40,50],100)
# print(q)
#3.get
# q=a.get(10)
# print(q)
# #4.items
# q=a.items()    #in this and get and from keys values are not directly saved you gotta create a variable.
# # print(q)
# #5.values and keys
# print((a.keys()))
# print(a.values())
# #6.pop and pop item
# print(a.pop(20))
# print(a)
# print(a.popitem())
# print(a)
# #7.set default
# print(a.setdefault(900,3000))
# # print(a)
# 8.update
# print(a.update({20:2000,76:774}))
# print(a)
#9.values
# print(a.values())




