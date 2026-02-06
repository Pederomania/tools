import torch

# Selección de dispositivo: GPU si está disponible, si no CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Dispositivo:", device)

# -------------------------------
# Datos de entrenamiento
# -------------------------------
# y = 4x + 1
x = torch.linspace(-5, 5, 100, device=device)
y_real = 4 * x + 1

# -------------------------------
# Parámetros entrenables
# -------------------------------
# Inicializados al azar a propósito
w = torch.randn(1, device=device, requires_grad=True)
b = torch.randn(1, device=device, requires_grad=True)

# -------------------------------
# Hiperparámetros
# -------------------------------
lr = 0.05  # learning rate
steps = 20  # número de pasos de entrenamiento

# -------------------------------
# Bucle de entrenamiento
# -------------------------------
for step in range(steps):
    # Forward: predicción lineal
    y_pred = x * w + b

    # Cálculo de la pérdida (MSE)
    loss = ((y_pred - y_real) ** 2).mean()

    # Backward: cálculo de gradientes
    loss.backward()

    # Actualización de parámetros (gradiente descendente manual)
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    # Resetear gradientes
    w.grad.zero_()
    b.grad.zero_()

    print(
        f"Paso {step:02d} | Loss: {loss.item():.6f} | "
        f"w: {w.item():.4f} | b: {b.item():.4f}"
    )

