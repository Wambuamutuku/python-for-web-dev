from datatypes import student


class person:
     #properties/Variables/ Attributes/ Characteristics
     def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

         #behaviour/Methods/Function
         def study(self):
             print("student is studying")

student1 = person("hussein", 23, "male")
print(student1.name, student1.age, student1.gender)

student2 = person("Alex", 34, "male")
print(student2.name, student2.age, student2.gender)

student3 = person("Leah", 45, "female")
print(student3.name, student3.age, student3.gender) 





