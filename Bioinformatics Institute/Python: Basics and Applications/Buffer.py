# Implement a class Buffer that will accumulate the elements of a sequence 
# and print the sum of quintuples of consecutive elements as they accumulate.
# One of the requirements for the class is that it should not store more elements than it really needs, 
# i.e. it should not store elements that are already included in the five for which the sum was deduced. 

class Buffer:
    def __init__(self):
        self.sum = 0
        self.arr = []


    def add(self, *a):
        # add next part of the sequence
        for el in a:
            self.arr.append(el)
            self.sum += el
            if len(self.arr) == 5:
                print(self.sum)
                self.sum = 0
                self.arr = []
            
            
    def get_current_part(self):
        return self.arr
