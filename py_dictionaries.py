my_list = [{"Name" : "Arun", "Age": 23},{"Name" : "Selva", "Age" : 24}]


print("Sorted by Age: ")
print(sorted(my_list, key = lambda i:i['Age']))

print("Desending order")
print(sorted(my_list, key = lambda i: i['Age'],reverse=True))

