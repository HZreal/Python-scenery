# 烤地瓜
class SweetPotato():
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []
    def cook(self,time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'
       #else:
       #    self.cook_state = '烤糊了'
    def add_condiments(self,condiments):
        self.condiments.append(condiments)


    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟,状态是{self.cook_state},你选的调料是{self.condiments}'

digua1 = SweetPotato()
print(digua1)

digua1.cook(2)   #烤2分钟
digua1.add_condiments('胡椒粉')
print(digua1)

digua1.cook(2)   #再烤2分钟
digua1.add_condiments('孜然粉')
print(digua1)

digua1.cook(3)   #再烤3分钟
digua1.add_condiments('辣椒粉')
print(digua1)

































































































































