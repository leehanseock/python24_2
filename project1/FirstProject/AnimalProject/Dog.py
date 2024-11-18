from project1.FirstProject.AnimalProject.Animal import Animal

class Dog(Animal):
    def shout(self):
        print(f"{self.name} 멍멍~")