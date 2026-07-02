
list_arry = [1, 0.5, 'hello', 1+5j, 1.7e2, -12, "welcome"]

print("Initial list: ", list_arry)
print("Data type ", type(list_arry))

for i in list_arry:
    print (type(i))

tuple_1 = (1, 0.5, 'hello', 1+5j, 1.7e2, -12, "welcome")

print("Initial tuple: ", tuple_1)
print("Data type: ", type(tuple_1))

str_1 = 'Hello'
str_2 = "World"

print("String 1: ", str_1)
print("Data Type of String 1: ", type(str_1))

print("String 2: ", str_2)
print("Data type of String 2 ", type(str_2))

r = range(2,21,2)

print("Range : ", r)
print("Range the List : ", list(r))
print("Data type : ", type(r))

set_1 = {"mango", "Apple", "banana", "cherry"}
set_2 = set(["Avacado", "Pineapple", "Pappaya"])

print("display set 1: ", set_1)
print("Data type of set 1: ", type(set_1))
print("display set 2: ", set_2)
print("Data type of set 2 :", type(set_2))

list_3 = ["Chickoo", "Orange", "Sitaphal", "Pomogranate"]

f_1 = frozenset(list_3)

print("Initial f_1 : ", f_1)
print("data type of f_1 : ", type(f_1))

person_1 = {
    'name': 'Alex',
    'age': 25,
    'Gender': 'Female'
}

print("Persona details : ", person_1)
print("Data type of person_1 : ", type(person_1))

s = "Welcome to the Jungle"
print("Display String: ", s)
print("length of the string ", len(s))
print("0 position ", s[0])
print("20 positon ", s[20])
print("last positon ", s[-1])

# print("print only welcome ", s[0:7])
print("print only ", s[11:15])

str1 = "boilingpoint"
print("previous string: ", str1)

str1 = "B" + str1[1:7] + " P" + str1[8:]
print("before string: ", str1)

msg="Hello"

print("before delete the variable ", msg)
del msg
# print("After delete the variable ", msg)

give_str = "Welcome to world"

print("Given String ", give_str)

new_str = "W" + give_str[-4:]
print("world --> World ", new_str)

new_str1 = give_str.replace("world","the Dehradun")
print("new_str1 ", new_str1)

print("Total number of characters in new_str1 ", len(new_str1))

a = "abcdef"
print("Total number of characters in a ", len(a))

print("Upper case characters in a ", a.upper())

print("lower case characters in a ", a.lower())

print("Capitalize case characters in a ", a.capitalize())

fun = " Havingfunn  "

print("remove white space in fun", fun.strip())

specific_char = "####Hi###"
print("remove white space in fun", specific_char.strip("#"))

movie = "The Tarzan the wonder car"
price = 200.00
seat = "F12"

print(f"{movie} ticket price is {price} and seat number is {seat}")