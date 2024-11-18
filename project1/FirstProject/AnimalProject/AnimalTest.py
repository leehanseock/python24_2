from project1.FirstProject.AnimalProject.Animal import Animal
from project1.FirstProject.AnimalProject.Dog import Dog
from project1.FirstProject.AnimalProject.Cat import Cat

if __name__ == '__main__':
    d = Dog("마음이")
    c = Cat("나비")
    d.run()
    c.shout()
    d.shout()