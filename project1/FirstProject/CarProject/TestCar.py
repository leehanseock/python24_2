from project1.FirstProject.CarProject.Car import Car
from project1.FirstProject.CarProject.Truck import Truck

if __name__ == '__main__':
    tr = Truck("붕붕이", 3900, "용달블루", 2500)
    tr.load(700)
    tr.info()
    tr.run()