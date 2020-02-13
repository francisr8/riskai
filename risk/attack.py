class Attack:
  def __init__(self, troops1, troops2, dices1, dices2):
    self.troops1 = troops1
    self.troops2 = troops2
    self.dices1 = dices1
    self.dices2 = dices2

  def calculate(self):
    return str(int(self.troops2 + self.troops1))

  def calculateProbabilityDice(self):
    return 45