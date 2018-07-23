"""
This module demo inheritance example 

super() :

python 2.7 -> base class must be inherting object class then only we can use super(deviceclass,self).__init__(args) this will work both 2.7 and 2.8

python 3.0 -> super().__init__(first,last) -> woll work no need to give self, and also no need to import from object class
"""


class Person(object):
	def __init__(self, first, last):
		self.firstname = first
		self.lastname = last

	def Name(self):
		return self.firstname + " " + self.lastname


class Employee(Person):

	def __init__(self, first, last, staffnum):
		super(Employee,self).__init__(first, last)
		self.staffnumber = staffnum
#		super().__init__(first, last)

	def GetEmployee(self):
		return self.Name() + ", "+ self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

