class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name + " " + str(self.age))


Person1 = person("Allan", 14)
Person2 = person("Yang", 18)
