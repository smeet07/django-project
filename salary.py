class Person(object):

    # __init__ is known as the constructor          
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name,"with id number",self.idnumber)


    # child class 


class salaried(Person):
    def __init__(self, name, idnumber, post,salary):
        self.post = post
        self.salary = salary

        # invoking the __init__ of the parent class  
        Person.__init__(self, name, idnumber)

    def displaysalaried(self):
        print("has salary",self.salary)

class nonsalaried(Person):
    def __init__(self, name, idnumber, post,salary):
        self.post = post
        self.salary=salary

        Person.__init__(self, name, idnumber)
    def displaynonsalaried(self):
        print("has salary",self.salary)

a=str(input("enter name :"))
b=int(input("enter id :"))
c=str(input("enter post :"))
if c=="manager":
    salary=100000
    employee=salaried(a,b,c,salary)
    employee.display()
    employee.displaysalaried()
elif c=="secretary":
    salary=50000
    employee=salaried(a,b,c,salary)
    employee.display()
    employee.displaysalaried()
elif c=="sales employee":
    x=int(input("enter the number of sales made :"))
    salary=50000+(x*1000)
    employee=salaried(a,b,c,salary)
    employee.display()
    employee.displaysalaried()
elif c=="factory worker":
    x = int(input("enter the hours worked :"))
    salary = x * 1000
    employee=nonsalaried(a,b,c,salary)
    employee.display()
    employee.displaynonsalaried()
else:
    print('no such post')







