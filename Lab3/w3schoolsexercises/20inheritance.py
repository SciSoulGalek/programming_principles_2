#something i wrote
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year 

  def info(self):
    print(self.firstname, self.lastname, self.graduationyear)
x = Person("John", "Doe")
y = Student("Galek", "Ryszhanov", 2023)
x.printname()
y.info()
#ex1
class Student(Person):
 pass
#ex2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
