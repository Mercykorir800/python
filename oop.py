# class Student:
#    name="Mercy"
#     age=23
# #object
# student1=Student()
# print(f"Name of student: {student1.name}")

class Student:
    def _init_(self,name,age):
        self.name=name
        self.age=age
student1=Student("Mercy",23)
student2=Student("Cherop",19)

print(student1.name)