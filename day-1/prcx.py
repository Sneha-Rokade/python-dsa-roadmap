
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