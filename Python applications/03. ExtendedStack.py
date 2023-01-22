# Implement a data structure that is an extended stack structure. 
# It is necessary to support adding an element to the top of the stack, 
# removing from the top of the stack, and it is necessary to support the operations 
# of addition, subtraction, multiplication, and integer division. 

class ExtendedStack(list):
    def sum(self):
        # addition
        self.append(self.pop() + self.pop())

    def sub(self):
        # subtraction
         self.append(self.pop() - self.pop())


    def mul(self):
        # multiplication
        self.append(self.pop() * self.pop())

    def div(self):
        # integer division
        self.append(self.pop() // self.pop())

def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0