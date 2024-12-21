import torch
from torchvision.models import resnet18, ResNet18_Weights
model = resnet18(weights=ResNet18_Weights.DEFAULT)
data = torch.rand(1, 3, 128, 128)
labels = torch.rand(1, 1000)

prediction = model(data)
print(prediction.sum().item())
