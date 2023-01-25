# Complete the code from 4.4 so that the weight and bias gradient matches the same gradient in your function. 

# Sample Input : anything 
# Sample Output :
# fc_weight_grad: tensor([[10., 20.], [10., 20.], [10., 20.]])
# our_weight_grad: tensor([[10., 20.], [10., 20.], [10., 20.]])
# fc_bias_grad: tensor([[1., 1., 1.]])
# out_bias_grad: tensor([[1., 1., 1.]]) 

import torch

x = torch.tensor([[10., 20.]])
fc = torch.nn.Linear(2, 3)
w = torch.tensor([[11., 12.], [21., 22.], [31., 32]])
fc.weight.data = w
b = torch.tensor([[31., 32., 33.]])
fc.bias.data = b
fc_out = fc(x)

# Sum fc layer to get a scalar:
fc_out_summed = fc_out.sum()

# Calculate gradients fc_out_summed:
fc_out_summed.backward()
weight_grad = fc.weight.grad
bias_grad = fc.bias.grad

# Now, calculate the same without fc layer:
w.requires_grad_(True)
b.requires_grad_(True)

# Alternative out:
# SUM{x * w^T + b}
our_formula =  torch.sum(x @ w.transpose(0,1)  + b) # 
our_formula.backward()

print('fc_weight_grad:', weight_grad)
print('our_weight_grad:', w.grad)
print('fc_bias_grad:', bias_grad)
print('out_bias_grad:', b.grad)
