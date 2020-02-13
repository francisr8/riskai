import random
class Simulator:
    def __init__(self, times):
        self.times = times
        self.troopsAttack = 0
        self.troopsDefense = 0
        self.xlist = []
        self.ylist = []

    def run(self):
        for i in range(self.times):
            randomAttacker = random.random()
            randomDefender = random.random()
            self.troopsAttack = random.randint(1,25)
            self.troopsDefense = random.randint(1,25)
            '''
            if randomAttacker <= 0.7:
                self.troopsAttack = random.randint(1, 5)
            elif randomAttacker > 0.7 and randomAttacker < 0.85:
                self.troopsAttack = random.randint(5, 10)
            elif randomAttacker > 0.85 and randomAttacker < 0.95:
                self.troopsAttack = random.randint(10, 20)
            else:
                self.troopsAttack = random.randint(20, 50)

            if randomDefender <= 0.7:
                self.troopsDefense = random.randint(1, 5)
            elif randomDefender > 0.7 and randomDefender <= 0.85:
                self.troopsDefense = random.randint(5, 10)
            elif randomDefender > 0.85 and randomDefender <= 0.95:
                self.troopsDefense = random.randint(10, 20)
            else:
                self.troopsDefense = random.randint(20, 50)
            '''
            self.xlist.append([self.troopsAttack, self.troopsDefense])

            while self.troopsAttack >= 1 and self.troopsDefense >= 1:
                self.simulate()

        return self.xlist, self.ylist


    def simulate(self):
        dicesAttacker, dicesDefender = self.checkNumberOfDices(self.troopsAttack, self.troopsDefense)
        attackList = self.throwDice(dicesAttacker)
        defendList = self.throwDice(dicesDefender)
        attackLose, defendLose = self.compareDices(attackList, defendList)
        self.troopsAttack -= attackLose
        self.troopsDefense -= defendLose
        if self.troopsAttack == 0:
            self.ylist.append(0)
        elif self.troopsDefense == 0:
            self.ylist.append(1)


    def compareDices(self, attackList, defendList):
        number = min(len(attackList), len(defendList))
        attackLose = 0
        defendLose = 0
        for i in range(number):
            if attackList[i] > defendList[i]:
                defendLose += 1
            else:
                attackLose += 1
        return attackLose, defendLose

    def throwDice(self, number):
        list = []
        for i in range(number):
            list.append(random.randint(1,6))
        list = sorted(list,reverse=True)
        return list

    def checkNumberOfDices(self, troops1, troops2):
        dice1 = 0
        dice2 = 0
        if troops1 == 1:
            dice1 = 1
        elif troops1 == 2:
            dice1 = 2
        elif troops1 >= 3:
            dice1 = 3

        if troops2 == 1:
            dice2 = 1
        elif troops2 == 2:
            dice2 = 2
        elif troops2 >= 3:
            dice2 = 3
        return dice1, dice2
