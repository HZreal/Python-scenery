# 搬家具
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return f'家具的名字是{self.name}, 家具的占地面积是{self.area}'

class House():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []
    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area = self.free_area - item.area
        else:
            print('该房屋面积不足以放置该家具！')
    def __str__(self):
        return f'该房子地理位置在{self.address},房屋面积是{self.area},剩余面积还有{self.free_area},搬进的家具有{self.furniture}'

sofa = Furniture('沙发',50)
bed = Furniture('单人床',30)
bighouse = House('北京',500)
print(sofa)
print(bed)
print(bighouse)
bighouse.add_furniture(sofa)
print(bighouse)
bighouse.add_furniture(bed)
print(bighouse)

digger = Furniture('挖掘机',575)
bighouse.add_furniture(digger)
print(bighouse)






















