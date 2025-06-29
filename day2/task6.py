# 1. 定义 Car 类
class Car:
    def __init__(self, brand, speed=0):
        """初始化汽车属性"""
        self.brand = brand  # 品牌
        self.speed = speed  # 当前速度

    def accelerate(self, m):
        """加速 m 次，每次增加 10"""
        for _ in range(m):
            self.speed += 10
        print(f"{self.brand} 加速 {m} 次后，当前速度: {self.speed} km/h")

    def brake(self, n):
        """刹车 n 次，每次减少 10，速度不低于 0"""
        for _ in range(n):
            if self.speed >= 10:  # 可以正常减速
                self.speed -= 10
            else:  # 速度已低于10，直接减到0
                self.speed = 0
                break
        print(f"{self.brand} 刹车 {n} 次后，当前速度: {self.speed} km/h")

    def show_speed(self):
        """显示当前速度"""
        print(f"{self.brand} 的当前速度: {self.speed} km/h")


# 2. 创建 Car 实例并操作
print("普通汽车操作:")
my_car = Car("Toyota", 60)
my_car.show_speed()  # 显示初始速度
my_car.accelerate(3)  # 加速3次
my_car.brake(2)  # 刹车2次
my_car.brake(5)  # 尝试刹车5次（实际只能刹到0）

print("\n" + "=" * 50 + "\n")  # 分隔线


# 3. 定义 ElectricCar 子类
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        """初始化电动汽车属性"""
        super().__init__(brand, speed)  # 调用父类初始化
        self.battery = battery  # 电量百分比

    def charge(self):
        """充电，电量增加20%，不超过100%"""
        self.battery = min(100, self.battery + 20)
        print(f"{self.brand} 充电后电量: {self.battery}%")

    def show_battery(self):
        """显示当前电量"""
        print(f"{self.brand} 当前电量: {self.battery}%")


# 测试电动汽车
print("电动汽车操作:")
tesla = ElectricCar("Tesla", 40, 30)
tesla.show_speed()  # 显示速度
tesla.show_battery()  # 显示电量
tesla.accelerate(2)  # 加速
tesla.brake(1)  # 刹车
tesla.charge()  # 充电
tesla.charge()  # 再次充电（不会超过100%）