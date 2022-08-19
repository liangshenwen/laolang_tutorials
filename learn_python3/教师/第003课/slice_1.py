class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        print("key is : " + str(index))
        if isinstance(index, slice):
            return self.data[index]
        elif isinstance(index, int):
            return self.data[index]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=type(self)))

    def __setitem__(self, key, value):
        print("key is:", key, "value is :", value)
        self.data[key] = value


lst = MyList(["My", "name", "is", "007"])

print(lst[3])
print(lst[:2:])

lst[len(lst):len(lst)] = [".", "Yes", "I", "Do"]
print(lst[:])

