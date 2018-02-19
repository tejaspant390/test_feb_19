"""
Define an Student class and initialize it with name and section.
  Now, make a classmethod that takes in a string parameter "name-A" which creates an instance and
  returns the instance based on parameter.
  [Hint: use @classmethod decorator]
"""

class Student(object):
    def __int__(self, name, section):
        self.name = name
        self.section = section

    @classmethod
    def get_stu_from_string(cls, inp):
        name, section = (inp.split("_"))
        return cls(name, section)


stu = Student.get_stu_from_string("name_xyz")
print(stu.__dict__)
