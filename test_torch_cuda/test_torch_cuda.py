import torch
import time

# -------------------------------
# Información del entorno
# -------------------------------
print("Torch version:", torch.__version__)
cuda_available = torch.cuda.is_available()
print("CUDA disponible:", cuda_available)

device = "cuda" if cuda_available else "cpu"
if cuda_available:
    print("GPU:", torch.cuda.get_device_name(0))

# -------------------------------
# Tamaño de las matrices
# -------------------------------
size = 4096  # 4096x4096 para notar diferencias de tiempo

# -------------------------------
# Test CPU
# -------------------------------
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu  # Multiplicación de matrices
cpu_time = time.time() - start
print(f"Tiempo CPU: {cpu_time:.3f} s")

# -------------------------------
# Test GPU
# -------------------------------
a_gpu = a_cpu.to(device)
b_gpu = b_cpu.to(device)

if cuda_available:
    torch.cuda.synchronize()  # Sincroniza antes de medir
start = time.time()
c_gpu = a_gpu @ b_gpu
if cuda_available:
    torch.cuda.synchronize()  # Sincroniza después de calcular
gpu_time = time.time() - start
print(f"Tiempo GPU: {gpu_time:.3f} s")

# -------------------------------
# Verificación de precisión
# -------------------------------
max_diff = (c_cpu - c_gpu.cpu()).abs().max().item()
print("Diferencia máxima CPU vs GPU:", max_diff)

