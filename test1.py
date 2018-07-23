
"""
# Include in the class a method called IsFemale() 
which returns a boolean depending if person is a female.#
Example class instantiationPerson1 = Person("Mary", "Female", 20)Person2 = Person("Bill", "Male",   35)
"""
class Person(object):

    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    
    def IsFemale(self):
        if self.gender == "Famale":
            return True
        else:
            return False


class SoftwareEng(Person):
    """
    # Example class instantiationSWE1 = SoftwareEngineer("Mary", "Female", 20,
    ["Java", "Python"])
    SWE2 = SoftwareEngineer("Bill", "Male", 35, ["Java", "C++"])
    """
    def __init__(self, name, gender, age, *lan):
        self.language = lang
        Person(nane,gender,age)

    def does_job(self):
        if 'java' in self.language :
            return True
        else: return False





        

