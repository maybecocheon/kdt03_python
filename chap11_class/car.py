###클래스 작성 실습::
# Vehicle: 기본 클래스, 색상, 중량, 가격을 속성으로 가짐.> color, weight, price
# Car: Vehicle을 상속하며, 엔진과 탑승자 수를 추가로 가짐. > engine, passengers
# Truck: Vehicle을 상속하며, 바퀴 수와 중량을 추가로 가짐. > wheels, load_weight

# Vehicle 클래스 정의
class Vehicle:
    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price
    
    def show(self):
        print(f'{self.color}, {self.weight}, {self.price}')


# Car 클래스 (Vehicle의 서브클래스)
class Car(Vehicle):
    def __init__(self, color, weight, price, engine, passengers):
        super().__init__(color, weight, price)
        self.engine = engine
        self.passengers = passengers
    
    def show(self):
        super().show()
        print(f'{self.engine}, {self.passengers}')

# Truck 클래스 (Vehicle의 서브클래스)
class Truck(Vehicle):
    def __init__(self, color, weight, price, wheels, load_weight):
        super().__init__(color, weight, price)
        self.wheels = wheels
        self.load_weight = load_weight
    
    def show(self):
        super().show()
        print(f'{self.wheels}, {self.load_weight}')

    if __name__ == '__main__':

        # Car 객체 5개 생성
        car_list = [
            Car("Red", 1500, 20000, "V6", 4),
            Car("Blue", 1400, 25000, "V8", 5),
            Car("Black", 1600, 30000, "Electric", 4),
            Car("White", 1200, 18000, "Hybrid", 4),
            Car("Green", 1300, 22000, "V6", 5)
        ]

        # Truck 객체 5개 생성
        truck_list = [
            Truck("Yellow", 3000, 40000, 8, 10000),
            Truck("Blue", 3200, 45000, 10, 12000),
            Truck("White", 2800, 35000, 6, 8000),
            Truck("Black", 3500, 50000, 12, 15000),
            Truck("Red", 3400, 48000, 10, 14000)
        ]

        # 생성된 객체들 출력 - show()를 사용한 출력 코딩 
        print("Cars:")
        for car in car_list:
            car.show()


        print("\nTrucks:")
        for truck in truck_list:
            truck.show()
