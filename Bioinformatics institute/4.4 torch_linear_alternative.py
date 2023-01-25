# Implement the functionality of torch.nn.Linear and check it out!
import torch

x = torch.tensor([[10., 20.]])
fc = torch.nn.Linear(2, 3)

# Weights of fc-layer are stored in fc.weight, biases are stored in fc.bias
w = torch.tensor([[11., 12.], [21., 22.], [31., 32]])
fc.weight.data = w

b = torch.tensor([[31., 32., 33.]])
fc.bias.data = b
fc_out = fc(x)

# Let's get analogous output with matrix operations:
# x * w^T + b
fc_out_alternative =  x @ w.transpose(0,1)+ b   
print(fc_out == fc_out_alternative)
