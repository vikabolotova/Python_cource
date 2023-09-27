import random

class Apple:
    status1 = {'Цветение': 0, 'Зеленое': 1 , 'Красное': 2}

    def __init__(self, index):
        self.index = index
        self.status = self.status1['Цветение']
        self.unharvested_apple = 0

    def grow(self):
        if self.status < 2:
            self.status += 1
        else:
            self.unharvested_apple += 1

    def is_dead(self):
        return self.unharvested_apple >= 3  # Если счетчик достиг 3, яблоко считается мертвым


    def zrelost(self):
        if self.status == 2:
            return True
        else:
            return False

class AppleTree:

    def __init__(self,*apples, age=1):
        self.apples = list(apples)
        self.age = age


    def grow_tree(self):
        self.age += 1

        if self.age <= 2:
            return

        if self.age >= 5:
            return

        if self.age >= 10:
            self.apples = []


        for apple in self.apples:
            apple.grow()

        chance_of_new_apple = 0.3
        if random.random() < chance_of_new_apple:
            new_apple = Apple(len(self.apples) + 1)
            self.apples.append(new_apple)


    def all_apples_ready(self):
        for apple in self.apples:
            if not apple.zrelost():
                return False
        return True


    def harvest_del(self):
        ripe_apples = []
        for apple in self.apples:
            if apple.zrelost():
                ripe_apples.append(apple)
        if len(ripe_apples) == len(self.apples):
            self.apples = []
            return True
        else:
            print("Предупреждение: Нельзя собрать урожай, пока не все яблоки созрели.")
            return False


class Gardener:

    def __init__(self, name, *plants):
        self.name = name
        self.plants = list(plants)

    def take_care_of_plants(self):
        for plant in self.plants:
            plant.grow_tree()


    def harvest(self, *plants):
        if all(plant.all_apples_ready() for plant in self.plants):
            for plant in self.plants:
                plant.harvest_del()
            print("Урожай собран.")
        else:
            print("Не все яблоки созрели. Урожай не может быть собран.")

    def garden_statistics(self):
        tree_count = len(self.plants)
        tree_ages = {}
        for index, plant in enumerate(self.plants):
            tree_name = f'Дерево {index + 1}'
            tree_age = plant.age
            tree_ages[tree_name] = tree_age

        apple_count = 0

        apple_stages = {'Цветение': 0, 'Зеленое': 0, 'Красное': 0}

        for plant in self.plants:
            apple_count += len(plant.apples)
            for apple in plant.apples:
                stage = apple.status
                stage_name = {v: k for k, v in Apple.status1.items()}[stage]
                apple_stages[stage_name] += 1

        return {
            'Кол-во деревьев, их возраст': tree_ages,
            'Кол-во яблок и их стадии': apple_stages,
            'Кол-во яблок': apple_count
        }




apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
apple4 = Apple(4)
apple5 = Apple(5)

tree1 = AppleTree(apple1, apple2, apple3, apple4, apple5)
tree2 = AppleTree(apple2,  apple4, apple5)
tree3 = AppleTree( apple4, apple5)


gardener = Gardener("Сергей1", tree1, tree2, tree3)


print("Статистика перед уходом за растениями:")
print(gardener.garden_statistics())


gardener.take_care_of_plants()
gardener.take_care_of_plants()
gardener.take_care_of_plants()
gardener.take_care_of_plants()
gardener.take_care_of_plants()
gardener.take_care_of_plants()

print("Статистика после ухода за растениями:")
print(gardener.garden_statistics())


gardener.harvest()


print("Статистика после сбора урожая:")
print(gardener.garden_statistics())


