# def rightAngle(row):
#     for i in range(1,row-1):
#         print("*" * i)
#
# rightAngle(6)

# def inverted_right_angled_triangle(rows):
#     for i in range(rows,0, -1):
#         print('*' * i)
#
# inverted_right_angled_triangle(5)

# a = ['rahul','sharma','harsha']
# x = tuple(a) #list to tuple conversion
# print(x)

# x = ("rahul","sharma","harsha","sharma")
# y = list(x)
# y[0] = 'harshu'
# x = tuple(y)
# print(x) #tuple to list and list to tuple

# dic = {"name":"rahul","surname":"sharma"}
# DicToArray_KEY = list(dic.keys())
# print(DicToArray_KEY)
# DicToArray_VALUE = list(dic.values())
# print(DicToArray_VALUE) ##dic to array

#array to Dictionary
key_items = ['a','b','c']
value_items = [1,2,3]

dic_merge = dict(zip(key_items,value_items))
print(dic_merge)