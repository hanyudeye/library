import torch

# 创建一个 3x3 的全零张量
zero_tensor = torch.zeros(3, 3)
print(zero_tensor)

# 创建一个 3x3 的随机张量
random_tensor = torch.rand(3, 3)
print(random_tensor)

# 张量的加法
result = zero_tensor + random_tensor
print(result)