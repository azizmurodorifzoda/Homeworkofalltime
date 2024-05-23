class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}")

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def display_info(self):
        print(f"Dog's Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years old")
        print("Tricks: " + ", ".join(self.tricks) if self.tricks else "No tricks learned yet")


my_dog = Dog("Buddy", "Golden Retriever", 3)
my_dog.bark()
my_dog.add_trick("Sit")
my_dog.add_trick("Shake hands")
my_dog.display_info()
