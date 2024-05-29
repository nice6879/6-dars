class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, city='{self.city}')"

class odam:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def __iter__(self):
        return iter(self.people)

    def filter(self, holat):
        return filter(holat, self.people)

f = odam()
f.add_person(Person("alice", 30, "Toshkent"))
f.add_person(Person("hasanboy", 25, "Samarqand"))
f.add_person(Person("hasanboy", 22, "fargona"))

print("iteratorlar:")
for person in f:
    print(person)

print(" 25 yoshdan kattalar:")
for person in f.filter(lambda p: p.age > 25):
    print(person)

print(" samarqandlik :")
for person in f.filter(lambda p: p.city == "Samarqand"):
    print(person)
