# Implement the MoneyBox to work with a virtual piggy bank.
# Each piggy bank has a limited capacity, which is expressed as an integer - the number of coins 
# that can be put into the piggy bank. 
# The class should maintain information about the number of coins in the piggy bank, 
# provide the ability to add coins to the piggy bank, 
# and find out if it is possible to add some more coins to the piggy bank without exceeding its capacity. 

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0


    def can_add(self, v):
        if self.coins + v > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            return True
        else:
            return False
