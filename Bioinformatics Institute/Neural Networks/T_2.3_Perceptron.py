import numpy as np

X = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]], dtype=float)
Y = np.array([1, 1, 0], dtype=float)
w = np.array([0, 0, 0], dtype=float)

class Perceptron():
    def __init__(self, w, x, y) -> None:
       self.w = w
       self.x = x
       self.y = y

    def update_weights(self, i):
        new_w = self.w * self.x[i]
        pred = 0
        if np.sum(new_w) > 0:
            pred = 1
        if pred > self.y[i]:
            self.w -= self.x[i]
        if pred < self.y[i]:
            self.w += self.x[i]

    def run(self):
        for i in range(len(self.x)):
            self.update_weights(i)

p = Perceptron(w, X, Y)
p.run()
p.w
