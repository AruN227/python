#Function
def printList( myList ):
    print("This is my List: ", myList)


myList = ["Arun","Selva","Mani","Karthi"]
printList(myList)

#Keyword argument
my_student=[]
def funkey(name,age):
   
    stu_dic = {'name': name,'age':age}
    my_student.append(stu_dic)

funkey(name = "Arun",age = 23)
funkey(name="Selva",age= 24)

print("list ",my_student)


#Passing list
def greet_users(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)
usernames = ['Arun', 'selva', 'mani']
greet_users(usernames)


#function to motiffy List

def modify_list(printed,unprinted):
    while printed:
        modify_printed = printed.pop()
        print("changes: ",modify_printed)
        unprinted.append(modify_printed)
    

printed = ["Cake","Milk","Chocolate"]
unprinted = []

modify_list(printed,unprinted)
print(unprinted)

#Collecting an arbitrary number of arguments
def build_profile(first, last, **user_info):
    profile = {'first': first, 'last':last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_0 = build_profile('albert', 'einstein',location='princeton')
user_1 = build_profile('marie', 'curie',location='paris', field='chemistry')

print(user_0)
print(user_1)

