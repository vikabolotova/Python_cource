class Apple:
    status = {'Цветение': 0, 'Зеленое': 1 , 'Красное': 2}

    def __init__(self, index):
        self.index = index
        self.status = self.status['Цветение']

    def grow(self):
        if self.status < 2:
            self.status += 1

    def zrelost(self):
        if self.status == 2:
            return True
        else:
            return False

class AppleTree:

    def __init__(self,*apples):
        self.apples = list(apples)



    def grow_tree(self):
        for apple in self.apples:
            apple.grow()

    def all_apples_ready(self):
        for apple in self.apples:
            if not apple.zrelost():
                return False
        return True


    def harvest_del(self):
            self.apples = []


class Gardener:

    def __init__(self, name, *plants):
        self.name = name
        self.plants = list(plants)

    def take_care_of_plants(self):
        for plant in self.plants:
            plant.grow_tree()


    def harvest(self):
        if all(tree.all_apples_ready() for plant in self.plants):
            for plant in self.plants:
                plant.harvest_del()
            print("Урожай собран.")
        else:
            print("Не все яблоки созрели. Урожай не может быть собран.")


 #       if self.plants.all_apples_ready():
  #          print('Урожай собран')
  #          self.plants.harvest_del()
   #     else:
   #         print("Яблоки еще не дозрели")


apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)
apple4 = Apple(4)
apple5 = Apple(5)

tree = AppleTree(apple1, apple2, apple3, apple4, apple5)

gardener = Gardener("Сергей", tree)

gardener.take_care_of_plants()
gardener.take_care_of_plants()
gardener.take_care_of_plants()
gardener.harvest()

