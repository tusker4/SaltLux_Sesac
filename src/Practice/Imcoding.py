class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        # self.damage = damage
        print("{0}유닛을 생성했습니다.[속도 : {1}]".format(self.name, self.speed))
        # print("체력: {0}, 공격력: {1}".format(self.hp, self.damage))

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 {self.speed} 속도로 이동합니다.")


class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name}: {location}방향으로 적군을 공격합니다.")

    def damaged(self, damage):
        print(f"{self.name}: {damage}만큼 데미지를 입었습니다.")
        self.hp -= damage
        print(f"현재남은 체력은 {self.hp}")
        if self.hp <= 0:
            print(f"{self.name}이 파괴되었습니다.")


class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed

    def fly(self, location):
        print("[공중 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 {self.flying_speed} 속도로 날아갑니다.")


class FlyAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
        super().__init__()

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
supply_depot = BuildingUnit("보급고", 500, "7시")

def game_start():
    print("게임을 시작합니다")

def game_over():
    pass

# 유닛들
soldier1 = AttackUnit("보병", 40, 5, 1)
soldier2 = AttackUnit("보병", 40, 5, 1)
tank = AttackUnit("탱크", 150, 35, 2)
Wraice = FlyAttackUnit("레이스", 80, 5, 10)
Wraice2 = FlyAttackUnit("업글레이스", 80, 5, 10)
vulture = AttackUnit("벌쳐", 80, 20, 10)


Wraice2.cloaking = True
if Wraice2.cloaking is True:
    print(f"{ Wraice2.name}는 은폐중입니다.")

tank.attack("5시")
soldier1.damaged(50)
vulture.move("3시")
Wraice.fly("2시")
