from random import randint, choice

# Родительский класс для игроков
class Player(object):
    # Инициализация игрока
    def __init__(self, health, name):
        self.health = health
        self.name = name
        self.endGame = True

    # Мега удар
    def mega_hit(self, per):
        valueHit = randint(18,25)
        print("Игорок: %s Наносит удар: %s Игроку %s" % (self.name, valueHit, per.name))
        per.health = per.health - valueHit

    # Средний удар
    def medium_hit(self, per):
        valueHit = randint(10, 35)
        print("Игорок: %s Наносит удар: %s Игроку %s" % (self.name, valueHit, per.name))
        per.health = per.health - valueHit

    # Самолечение
    def heal_health(self, per):
        pass

    # Рандомный выбор события
    def choose_action(self, per):
        listAction = [self.mega_hit, self.medium_hit, self.heal_health]
        currentAction = choice(listAction)
        currentAction(per)
        per.get_health()
        print(per)
        print(self)

    # Взять и проверить здоровье не меньше ли 0
    def get_health(self):
        if(self.health > 0):
            return self.health
        else:
            self.health = 0
            self.endGame = False
            print("+" * 20)
            print("Игорок: %s был повержен" % (self.name))
            print("+" * 20)

    # Если здоровье 0 - завершить игру
    def get_end(self):
        return self.endGame

    def __str__(self):
        return "Игорок: %s Здоровье: %s" % (self.name, self.health)

# Унаследованный класс Компьютер
class Computer(Player):

    # Переопределеям метод самолечения
    def heal_health(self, per):
        if (self.health >= 35):
            valueHit = randint(1, 2)
            self.health = self.health + valueHit

        else:
            valueHit = randint(2, 3)
            self.health = self.health + valueHit
        print("Игорок: %s Увеличил силы на: %s" % (self.name, valueHit))

# Унаследованный класс Игрок
class Person(Player):

    # Переопределеям метод самолечения
    def heal_health(self, per):
        valueHit = randint(1, 2)
        self.health = self.health + valueHit
        print("Игорок: %s Увеличил силы на: %s" % (self.name, valueHit))


# Основная функция
def new_game():
    heath = 100
    player = 'Computer'
    player1 = "Yura"
    # Создаем экземпляр класса Компьютер
    Asus = Computer(heath,player)
    # Создаем экземпляр класса Игрок
    Student = Person(heath, player1)
    # Все игроки
    players = [Student, Asus]
    print("Начало игры")
    # Пока здоровье кого-то не закончится
    while(Student.get_end() & Asus.get_end()):
        # Случайный игрок
        currentPlayers = choice(players)
        index = players.index(currentPlayers)
        print(currentPlayers)
        players.remove(currentPlayers)
        noCurrentPlayers = players[0]
        # Случайное действие
        f = input("Type any key to continue")
        currentPlayers.choose_action(noCurrentPlayers)
        players.append(currentPlayers)
        print("=" * 20)




new_game()