class Student:
    pass

s=Student()
print(s)

class Student:
    name="Karthik kennedy"

studname = Student()
print(studname.name)

class Stu:
    name='kennedy'
    def change_name(self,new_name):
        self.name=new_name


ob=Stu()
print(ob.name)
ob.change_name('karthik')
print(ob.name)

class Employee:
    empCount=0;
    def __init__(self,name,id):
        self.name=name
        self.id=id
        Employee.empCount += 1
    def diplayCount(self,name,id):
        self.name=name
        self.id=id
        print("Total employee %d" ,Employee.empCount)
        print('Name ',ob1.name,',',ob1.id)
    def change_name(self,new_name):
        self.name=new_name

ob1=Employee("ram",100)
ob2=Employee("Lax",101)
ob1.diplayCount('Thanviga',1000);
#ob2.diplayCount();
print(ob1.name)
print(ob2.name)
ob1.change_name("ramkumar")
ob2.change_name("Laxmankumar")
print(ob1.name)
print(ob2.name)
