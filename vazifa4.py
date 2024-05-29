class f:
    def __init__(self, name):
        self.name = name
        self.id = id(self)

class obyeckt:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def __iter__(self):
        return (obj.id for obj in self.objects)

collection = obyeckt()
collection.add_object(f("Object 1"))
collection.add_object(f("Object 2"))
collection.add_object(f("Object 3"))

print("Iterable object using iterator (IDs):")
for obj_id in collection:
    print(obj_id)
