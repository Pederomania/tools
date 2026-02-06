import torch

# Verifica si CUDA está disponible
cuda_available = torch.cuda.is_available()
print("CUDA disponible:", cuda_available)

# Mostrar nombre de la GPU si está disponible, si no indica CPU
gpu_name = torch.cuda.get_device_name(0) if cuda_available else "CPU"
print("GPU usada:", gpu_name)

