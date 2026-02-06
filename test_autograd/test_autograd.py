import torch

# Selección de dispositivo: GPU si está disponible, si no CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Dispositivo:", device)

# -------------------------------
# Parámetros "entrenables"
# -------------------------------
w = torch.tensor(3.0, device=device, requires_grad=True)
b = torch.tensor(1.0, device=device, requires_grad=True)

# Dato de entrada
x = torch.tensor(2.0, device=device)

# -------------------------------
# Forward: función simple y = (x*w + b)^2
# -------------------------------
y = (x * w + b) ** 2
print("Resultado y:", y.item())

# -------------------------------
# Backward: cálculo de gradientes
# -------------------------------
y.backward()  # Calcula gradientes automáticamente
print("Gradiente de w:", w.grad.item())
print("Gradiente de b:", b.grad.item())

