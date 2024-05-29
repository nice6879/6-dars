
class Student:
    objects = []
    
    def __init__(self, f_name):
        self.f_name = f_name
        self.__class__.objects.append(self)
        self._index = 0 
    
    def __iter__(self):
        self._index = 0  
        return self
    
    def __next__(self):
        if self._index < len(self.__class__.objects):
            result = self.__class__.objects[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

Student('rahmatillo')
Student('elmurod')
Student('noila')
Student('ali')

for student in Student('alisher'):
    print(student.f_name)