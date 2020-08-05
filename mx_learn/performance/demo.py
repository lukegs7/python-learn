class Person:
    host = None

    def __init__(self):
        pass

    def get_name(self):
        print(dir(self))
        return self.host


class Student(Person):
    host = '123123'

    def __init__(self):
        super(Student, self).__init__()
        # self.host = 'geshuai'
        pass


c = Student()
print(c.get_name())
print(c.__dict__)
# d = Student()
# c.host = 123123123
# print('name is :', c.get_name())
# print('name is :', d.get_name())
