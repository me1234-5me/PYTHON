
class student:
  def __init__(self, name, age,clsnumber):
    self.name = name
    self.age = age
    self.clsnumber =clsnumber


  def myfunc(self):
    print("Hello my name is " + self.name +self.age + self.clsnumber)
p1 = student("John", "20","1123")

print(p1)
p1.myfunc()
