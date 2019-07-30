class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("I am " + self.name + " and I'm " + str(self.age) + " years old.")


person1 = person("Allan", 12)

print(person1.greeting())
