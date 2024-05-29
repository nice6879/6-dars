class iterator:
    def __init__(self, data):
        self.data = data
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks >= len(self.data):
            raise StopIteration
        qiymat = self.data[self.indeks]
        self.indeks += 1
        return qiymat

mening_royxatim = [1, 2, 3, 4, 5]
iterators = iterator(mening_royxatim)

print("hi:")
for qiymat in iterators:
    print(qiymat)

