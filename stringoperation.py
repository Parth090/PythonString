char = "my name is aditya and i am working as a software developer"
print(char.title())
print(len(char))
print(char[0:5])
print(char.find("zo"))
print(char.replace("name", "hello"))
print(char)
print(char.split())


num = 0
count = 0
for i in range(num, 20):
    if i % 2 == 0:
        continue
    count = count + 1
print("Count of odd number is " + str(count))
print(f"count of odd number is {count}")
print("Count of odd number is %d" % (count))

time = input("Enter time in HH:MM:SSFM :")
if len(time) is 10:
    hh = int(time[0:2])
    mm = int(time[3:5])
    ss = int(time[6:8])
    ff = time[8:10]
    ff = ff.upper()
    if time[8:10].upper() == ff:
        hh = hh + 12
        print(f"{hh}:{mm}:{ss}PM")
    else:
        hh = hh
        print(f"{hh}:{mm}:{ss}AM")
else:
    print("Invalid format enter")

# for i in range(1,6):
#     print(str(i) * i)

# a
# bb
# ccc
# dddd

# alphabets = 'abcd'
# for i in range(0,4):
#     print(alphabets[i] * (i+1))

# a = 1

# while a < 10:
#     print(a, end="")
#     a += 1


# num = int(input('Enter number to check it is composite :'))
# count = 0
# for i in range(1,num+1):
#     if num % i == 0:
#         print('{} is factor of {}'.format(i,num))
#         count = count + 1
# if count > 2:
#     print(f'{num} is composite number with {count} factor')
# else:
#     print('Prime number')

# het = [1, "python" , "Mukherjee" , 67 , [10,"hyd" , "bom"]]
# print(type(het))
# print(het[4][1])
# het.append(800)
# print(het)
# het.insert(0,['aditya','whats', 600])
# print(het)
# het[1] = 'hii'
# print(het)
# op = []
# op_1 = []
# op_2 = []

# for i in het:
#     if type(i) is not list:
#         op.append(i)
#     else:
#         for j in i:
#             op.append(j)

# for i in op:
#     if type(i) is int:
#         op_1.append(i)
#     else:
#         op_2.append(i)
# print(op)
# print(op_1)
# print(op_2)


# l1 = [100 , 300 , "python" , "hyd" , 39]

# l2 = []
# l3 = []
# for i in l1:
#     if type(i) is int:
#         l2.append(i)
#     else:
#         l3.append(i)
# print(l2)
# print(l3)

# l1 = [4,5,6]
# l2 = [4,6,8]
# sum = []
# for i in range(0,len(l1)):
#     sum.append(l1[i] + l2[i])
# print(sum)

# square of even numbers

# sqr_even = []
# num = int(input('Enter number :'))
# for i in range(1,num+1):
#     if i % 2 == 0:
#         sqr_even.append(i**2)
# print(sqr_even)

# emp = {"name" :"Mukherjee" , "tech" : "python" , "age" : 100, (1,2,3) : 'hello' }

# print(emp)
# print(emp['name'])
# emp['subject'] = ["python", "java","c++"]
# c = "c#", "javascript","angular"
# c = list(c)
# emp['subject'] = c
# print(emp)
# print(emp.keys())
# print(emp.values())
# print(emp.items())
# for i in emp.items():
#     print(i[1])

# d = {1:1,2:4,3:9.....10:100}
# n -- >10
# d = {}
# for i in range(1,11):
#     d[i] = i**2
# print(d)

# d = ['hee']
# d1 = ['one','two','three']
# z = zip(d,d1)
# print(z)
# z = dict(z)
# print(z)

##spoint --> 10
##epoint --> 20
##10 , 12 , 14 , 15 , 16 , 18 , 20
##{10:[1,2,5,10] , 12:[1,2,3,4,6,12] . .. . 20:[1,2,4,5,10,20]}


# num_1 = int(input('Enter first number :'))
# num_2 = int(input('Enter second number :'))
# d = {}
# for i in  range(num_1,num_2+1):
#     if i % 2 == 0:
#         d[i] = [ j  for j in range(1,i+1)  if i % j == 0]
# print(d)

# d= {'i' : 3 , 'love': 4, 'python': 6}

# d = {}
# stmt = 'i love python'
# for i in stmt.split():
#     d[i] = len(i)
# print(d)

# stmt = 'i love python'
# d = { word:len(word) for word in stmt.split() if len(word) > 4}
# print(d)

# num_1 = int(input("Enter first number :"))
# num_2 = int(input("Enter second number :"))

# def add(num_1,num_2):
#     res = num_1 + num_2
#     print(res)
#     return res
# def sub(num_1,num_2):
#     res = num_1 - num_2
#     print(res)
#     return res
# def div(num_1,num_2):
#     res = num_1 / num_2
#     print(res)
#     return res
# def mul(num_1,num_2):
#     res = num_1 * num_2
#     print(res)
#     return res


# print(type(add))

# addres = add(num_1,num_2)
# subres = sub(addres,num_2)
# divres = div(subres,num_2)
# mulres = mul(divres,num_2)


# mul(div(sub(add(num_1,num_2),num_2),num_2),num_2)


# def avg(*abc):
#     s = 0
#     for i in abc:
#         s = s + i
#     s = s/len(abc)
#     return s


# s = avg(10,30)
# print(s)

# d = {'name' : 'aditya','age':25, 'addr': 'vns'}

# for key , value in d.items():
#     print(key,value)


# emp = {"name" :"Mukherjee" , (1,2,3) : "python" , "age" : 100 }

# print(emp['name'])
# print(emp.get('phone','Dont exist'))
# emp['name'] = "aditya"
# emp['phone'] = '9760133838'
# print(emp)
# emp.update({'name': 'aditya','phone': '9760133838'})
# print(emp)
# for key,value in emp.items():
#     print(key,value)


# def myFun(x):
#     x = 20
#     return x


# x = 30
# z = myFun(x)
# print(z)

# def myFunc(x):
#     x = [1,2,3]
#     return x
#     # x[0] = 70

# lst = [12,13,14,15,16,17]
# myFunc(lst)
# print(lst)

# def myFunc(*args):
#     print(type(args))
#     for arg in args:
#         print(arg)


# myFunc('hello', 'how', 'are','you')

# def myFun(**kwargs):
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print("%s===%s"%(key,value))


# myFun(firstname = 'aditya',lastname='mukherjee',age =25,location='varanasi')


# def myFun(firstname,lastname="mukherjee"):
#     print('first name :' + firstname + ' last name :' + lastname)

# myFun('aditya','singh')

# import antigravity
# import my_module

# courses = ["python","java","c#","javascript","angular"]
# index_value = my_module.find_index(courses,'angular')
# print(index_value)

# from my_module import find_index,test
# import sys
# courses = ["python","java","c#","javascript","angular"]
# index_value = find_index(courses,'angular')
# print(index_value)
# print(test)
# print(sys.path)

# def find_index(to_courses,search):
#     for i, value in enumerate(to_courses):
#         if value == search:
#             print('Index of searched value is %d'%(i) )
#             return i

#     else:
#         return -1


# courses = ["python","java","c#","javascript","angular"]
# index_value = find_index(courses,'angular')

# strn = 'hello how are you'
# strn1 = ''
# for i in range(len(strn)-1, -1, -1):
#     if strn[i] in ['a','e','i','o','u']:
#         continue
#     strn1 = strn1 + strn[i]


# print(strn1)

# Working with OS module

# import os

# print(os.getcwd())

# os.chdir(r'C:\Users\Lenovo\Desktop')
# print(os.listdir())


# words = ['cat','monkey','dog']

# for i in words[:]:
#     if len(i) > 3:
#         words.insert(0,i)
# print(words)

# for i in range(2,2):
#     print(i)

# 0, 1, 1, 2,3,5,8,12
# ͞pythonbestforbeginners͟

# words = 'pythonbestforbeginners'
# result = ''

# for word in range(0,len(words)):
#     if word % 2 == 0:
#         continue
#     result = result + words[word]
# print(result)

# words = 'helloi9eihowfare5yo9u'
# print(words.isalnum())


# Python oops
###################


class Employee:

    raiseamount = 1.04
    no_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"
        Employee.no_of_employee += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def raise_amount(self):
        self.pay = int(self.pay * self.raiseamount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raiseamount = amount

    @classmethod
    def form_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print("Not Work day")
            return False
        print("Work day")
        return True


class Developer(Employee):
    raiseamount = 2.04

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            print(self.employees)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())


dev1 = Developer("akash", "singh", 50000, "python")
print(dev1.email)
print(dev1.pay)
dev1.raise_amount()
print(dev1.pay)
print(dev1.prog_lang)

mg1 = Manager("venkat", "krishna", 90000, [dev1])
print(mg1.email)
mg1.add_emp(dev1)
mg1.print_emp()

print(Employee.no_of_employee)
emp1 = Employee("aditya", "mukherjee", 70000)
emp2 = Employee("navneet", "nayak", 40000)
print(Employee.no_of_employee)
print(emp1.email)
print(emp1.fullname())
print(Employee.fullname(emp1))
# print(emp2.pay)
# emp2.raise_amount()
# print(emp2.pay)

print(Employee.set_raise_amount(1.09))
# emp1.raiseamount = 1.08
print(Employee.raiseamount)
print(emp1.raiseamount)
print(emp2.raiseamount)
print(emp1.__dict__)

emp_str_1 = "shibin-munappaly-30000"

# first , last, pay = emp_str_1.split('-')
# new_emp1 = Employee(first,last,pay)
new_emp1 = Employee.form_string(emp_str_1)
print(new_emp1.fullname())

import datetime

my_date = datetime.date(2019, 12, 14)

print(Employee.is_workday(my_date))
