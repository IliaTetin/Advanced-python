class Perceptron:

    def __init__(self, w, b):
        """
        w - weights (m, 1),  m - number of vars
        b - number
        """
        
        self.w = w
        self.b = b

    def forward_pass(self, single_input):
        """
        Returns the output of perceptron by taking a single example
        single_input - excample vector (m, 1).
        returns number (0 or 1) or boolean (True/False)
        """
     
        result = 0
        for i in range(0, len(self.w)):
            result += self.w[i] * single_input[i]
        result += self.b
        
        if result > 0:
            return 1
        else:
            return 0

    def vectorized_forward_pass(self, input_matrix):
        """
        Returns the output of perceptron by taking several examples
        input_matrix - matrix of examples (n, m), every row - separate example,
        n - number of examples, m - number of variables
        Returns vector (n, 1) with perceptron answers
        (vector elements - boolean or int (0 or 1))
        """
        ## Your code here
        
        res = input_matrix.dot(self.w) + self.b
        is_positive = res > 0
        return is_positive

    
    def train_on_single_example(self, example, y):
        """
       input vector (examples), shape (m, 1) 
        inputs correct answer (0 or 1 or boolean),
        renews perceptron's weights according to an example
        returns error before changing weights (0 or 1)
        """
        ## Your code here
        
        arr = self.vectorized_forward_pass(example.T)
        error = y - arr
        self.w += error * example
        self.b += error
        return error
