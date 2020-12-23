import random
"""
Монстр и битва 

принцесса
"""



class Char:
    def __init__(self, name, health, geo_x, geo_y, power, speed, money):
        self.name=name
        self.health=health
        self.geo_x=geo_x
        self.geo_y=geo_y
        self.power=power
        self.speed=speed
        self.money=money
    
    def attack(self):
        return self.power
    
    def up(self):
        print("Ваш персонаж сделал шаг вперед\n")
        self.geo_y=self.geo_y+self.speed
    
    def right(self):
        print("Ваш персонаж сделал шаг вправо\n")
        self.geo_x=self.geo_x+self.speed
        
    def down(self):
        print("Ваш персонаж сделал шаг назад\n")
        self.geo_y=self.geo_y-self.speed
    
    def left(self):
        print("Ваш персонаж сделал шаг налево\n")
        self.geo_x=self.geo_x-self.speed
        
    def damage_for_hero(self, damage):
        self.health=self.health-damage

class Chest:
    def __init__(self, name, geo_x, geo_y, money):
        self.name=name 
        self.geo_x=geo_x
        self.geo_y=geo_y
        self.money=money
  
        
class Monster:
    geo_x = 5
    geo_y = 5
    def __init__(self, name, health, geo_x, geo_y, power, speed, money):
        self.name=name
        self.health=health
        self.geo_x=geo_x
        self.geo_y=geo_y
        self.power=power
        self.speed=speed 
        self.money=money
    
    def damage_for_monster(self,damage):
        print("Монстр получает урон:\t", damage)
        self.health=self.health-damage
    
    def damage_from_monster(self):
        print("Вы получаете урон:\t", self.power)
        
"""
Блок создания персонажа
"""
monster1=Monster("Бес", 100, 1, 1, 5, 0, 20)
dragon=Monster("Дракон", 500, 3, 3, 15, 0, 2000)
chest1=Chest("Сундук", 2, 2, 300)

while(True):
    print("Введите имя персонажа")
    char_name = input()
    print("Выберите класс: Воин, Маг, Шут")
    char_class = input()
    if (char_class == 'воин'):
        h1=Char(char_name, 100, 0, 0, 10, 1, 0)
    elif (char_class == 'маг'):
        h1=Char(char_name, 100, 0, 0, 10, 1, 0)
    elif (char_class == 'шут'):
        h1=Char(char_name, 100, 0, 0, 10, 1, 0)
    else:
        print("Произошла ошибка!")
        break
    for i in range(10):
        print("\n")
    print("\n----------------------",
        "\nВашего персонажа зовут: ", char_name,
          "\nКласс персонажа: ", char_class,
          "\n----------------------")
    break

while(True):
    print("На данный момент вы находитесь на координатах \nx:",
          h1.geo_x, " y:", h1.geo_y)
    print("Куда вы пойдёте?")
    temp_coord = input()
    if (temp_coord == 'влево'):
        h1.left()
    elif (temp_coord == 'вправо'):
        h1.right()
    elif (temp_coord == 'вверх'):
        h1.up()
    elif (temp_coord == 'вниз'):
        h1.down()
    else:
        print("Произошла ошибка!")
    
    if (h1.geo_x == chest1.geo_x) and (h1.geo_y == chest1.geo_y):
        print("Вы нашли ", chest1.name, "!")
        h1.money += chest1.money
        print("Теперь у Вас ", h1.money, "монет.")
        chest1.geo_x = 1000
        
    
    
    """
    Проверяем наличие монстра в клетке
    """
    if (h1.geo_x == monster1.geo_x) and (h1.geo_y == monster1.geo_y):
        print("Битва")
        break
        
while(True):
    if (monster1.health <= 0):
        print("Вы победили монстра! \nВаша награда: ", monster1.money, "золотых.")
        print("Вы получили новый уровень! Теперь у вас 150 хп!")
        h1.money += monster1.money
        h1.health = 150
        input()
        break
    else:
    
        print("Битва героя ", h1.name, " и монстра ", monster1.name)
        print("Ваше хп: ", h1.health, "Хп монстра: ", monster1.health)
        monster1.damage_from_monster()
        h1.damage_for_hero(monster1.power)
        print("Атака/побег?")
        temp_reaction = input()
        if (temp_reaction == 'атака'):
            crit = random.randint(0,1)
            if crit == 1:
                print('---------------------------------')
                print('!!!Вы нанесли критический удар!!!')
                print('---------------------------------')
                h1.power += 15
                monster1.damage_for_monster(h1.power)
                h1.power -= 15
            else:
                monster1.damage_for_monster(h1.power)
        elif (temp_reaction == 'побег'):
            break
        else:
            print("Произошла ошибка!")
            
while(True):
    print("На данный момент вы находитесь на координатах \nx:",
          h1.geo_x, " y:", h1.geo_y)
    print("Куда вы пойдёте?")
    temp_coord = input()
    if (temp_coord == 'влево'):
        h1.left()
    elif (temp_coord == 'вправо'):
        h1.right()
    elif (temp_coord == 'вверх'):
        h1.up()
    elif (temp_coord == 'вниз'):
        h1.down()
    else:
        print("Произошла ошибка!")
    
    if (h1.geo_x == chest1.geo_x) and (h1.geo_y == chest1.geo_y):
        print("Вы нашли ", chest1.name, "!")
        h1.money += chest1.money
        print("Теперь у Вас ", h1.money, "монет.")
        chest1.geo_x = 1000
    """
    Проверяем наличие босса в клетке
    """
    if (h1.geo_x == dragon.geo_x) and (h1.geo_y == dragon.geo_y):
        print("У логова дракона вы находите зачарованный меч!")
        break
    
while(True):
    if (dragon.health <= 0):
        print("Вы победили босса и спасли принцессу! \nВаша награда: ", monster1.money, "золотых.")
        h1.money += dragon.money
        input()
        break
    else:
        print("Битва героя ", h1.name, " и монстра ", dragon.name)
        print("Ваше хп: ", h1.health, "Хп монстра: ", dragon.health)
        if(h1.health<0):
            print("Конец игры")
        else:
            h1.power = 75
            dragon.damage_from_monster()
            h1.damage_for_hero(dragon.power)
            print("Атака/побег?")
            temp_reaction = input()
            if (temp_reaction == 'атака'):
                crit = random.randint(0,1)
                if crit == 1:
                    print('---------------------------------')
                    print('!!!Вы нанесли критический удар!!!')
                    print('---------------------------------')
                    h1.power += 15
                    dragon.damage_for_monster(h1.power)
                    h1.power -= 15
                else:
                    dragon.damage_for_monster(h1.power)
            elif (temp_reaction == 'побег'):
                break
            else:
                print("Произошла ошибка!")
            
for i in range(10):
    print("\nКОНЕЦ")


        
    
