# class student:
#     def __init__(self) -> None:
#         None

#     def __iter__(self,*args):
#         return self

#     def __next__(self, *args):
#         if input('__'):
#             return 'a'
#         else:
#             raise StopIteration
            
# for i in student():
#     print(i)  



#______________________________________________


# class Student:
#     objects = []
#     counter = 0

#     def __init__(self, f_name):
#         self.f_name = f_name
#         self.objects.append(self)

#     def __iter__(self):

#         return self
    
#     def __next__(self):
#         try:
#             object = self.objects[self.counter]
#             self.counter += 1
#             return object
#         except IndexError:
#             self.counter = 0
#             raise StopIteration

# Student('rahmatillo')
# Student('elmurod')
# Student('noila')
# Student('ali')

# for student in Student('alisher'):
#     print(student)



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





















