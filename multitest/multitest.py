import torch
import time

print("="*60)
print("MULTITEST PYTORCH - ENTORNO GSE")
print("="*60)

# -------------------------------
# 1️⃣ Test instalación y versión
# -------------------------------
print("\n[1] Test instalación y versión")
print(f"Torch version: {torch.__version__}")
cuda_available = torch.cuda.is_available()
print(f"CUDA disponible: {cuda_available}")

# Selección de dispositivo: GPU si está disponible, si no CPU
device = "cuda" if cuda_available else "cpu"
print(f"Usando dispositivo: {device}")

if cuda_available:
    print(f"GPU: {torch.cuda.get_device_name(0)}")

# -------------------------------
# 2️⃣ Test tensores y operaciones básicas
# -------------------------------
print("\n[2] Test tensores y operaciones básicas")
size = 4096
a = torch.randn(size, size)
b = torch.randn(size, size)

# CPU matmul
start = time.time()
c_cpu = a @ b
cpu_time = time.time() - start
print(f"CPU matmul {size}x{size}: {cpu_time:.4f} s")

# GPU matmul
if cuda_available:
    a_gpu = a.to(device)
    b_gpu = b.to(device)
    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    max_diff = (c_cpu - c_gpu.cpu()).abs().max().item()
    print(f"GPU matmul {size}x{size}: {gpu_time:.4f} s")
    print(f"Diferencia máxima CPU vs GPU: {max_diff:e}")

# Operaciones element-wise
start = time.time()
d = torch.sin(a) + torch.exp(b)
elem_time = time.time() - start
print(f"Operaciones element-wise CPU: {elem_time:.4f} s")

if cuda_available:
    start = time.time()
    d_gpu = torch.sin(a_gpu) + torch.exp(b_gpu)
    torch.cuda.synchronize()
    elem_gpu_time = time.time() - start
    print(f"Operaciones element-wise GPU: {elem_gpu_time:.4f} s")

# -------------------------------
# 3️⃣ Test autograd (gradientes)
# -------------------------------
print("\n[3] Test autograd")
w = torch.tensor(3.0, device=device, requires_grad=True)
b = torch.tensor(1.0, device=device, requires_grad=True)
x = torch.tensor(2.0, device=device)
y = (x*w + b)**2
y.backward()
print(f"Forward y = {y.item()}")
print(f"Gradiente w: {w.grad.item()}, Gradiente b: {b.grad.item()}")
w.grad.zero_()
b.grad.zero_()

# -------------------------------
# 4️⃣ Mini entrenamiento lineal: y = 4x + 1
# -------------------------------
print("\n[4] Mini entrenamiento lineal y = 4x + 1")
x_data = torch.linspace(-5, 5, 100, device=device)
y_real = 4*x_data + 1
w = torch.randn(1, device=device, requires_grad=True)
b = torch.randn(1, device=device, requires_grad=True)
lr = 0.05
steps = 20

for step in range(steps):
    y_pred = x_data*w + b
    loss = ((y_pred - y_real)**2).mean()
    loss.backward()
    with torch.no_grad():
        w -= lr*w.grad
        b -= lr*b.grad
    w.grad.zero_()
    b.grad.zero_()
    if step % 5 == 0 or step == steps-1:
        print(f"Paso {step:02d} | Loss: {loss.item():.6f} | w: {w.item():.4f} | b: {b.item():.4f}")

# -------------------------------
# 5️⃣ Mini red neuronal: y = x^2 + 2x + 1
# -------------------------------
print("\n[5] Mini red neuronal para y = x^2 + 2x + 1")
class MiniNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = torch.nn.Linear(1, 5)
        self.out = torch.nn.Linear(5, 1)
        self.act = torch.nn.Tanh()
    def forward(self, x):
        x = self.act(self.hidden(x))
        return self.out(x)

model = MiniNN().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
x_train = torch.linspace(-3, 3, 100).unsqueeze(1).to(device)
y_train = x_train**2 + 2*x_train + 1

for step in range(20):
    optimizer.zero_grad()
    y_pred = model(x_train)
    loss = ((y_pred - y_train)**2).mean()
    loss.backward()
    optimizer.step()
    if step % 5 == 0 or step == 19:
        print(f"Paso {step:02d} | Loss: {loss.item():.6f}")

# -------------------------------
# 6️⃣ Test optimizadores y reproducibilidad
# -------------------------------
print("\n[6] Test optimizadores y reproducibilidad")
torch.manual_seed(42)
x_seed = torch.randn(10,1, device=device)
y_seed = 2*x_seed + 1
w_seed = torch.randn(1, device=device, requires_grad=True)
b_seed = torch.randn(1, device=device, requires_grad=True)
opt = torch.optim.Adam([w_seed,b_seed], lr=0.1)
for _ in range(5):
    opt.zero_grad()
    y_pred = x_seed*w_seed + b_seed
    loss = ((y_pred - y_seed)**2).mean()
    loss.backward()
    opt.step()
print(f"w_seed: {w_seed.item():.4f}, b_seed: {b_seed.item():.4f}")

# -------------------------------
# 7️⃣ Stress test de memoria GPU
# -------------------------------
print("\n[7] Stress test de memoria GPU")
try:
    stress_size = 8192
    a_stress = torch.randn(stress_size, stress_size, device=device)
    b_stress = torch.randn(stress_size, stress_size, device=device)
    torch.cuda.synchronize()
    start = time.time()
    c_stress = a_stress @ b_stress
    torch.cuda.synchronize()
    print(f"Stress test GPU {stress_size}x{stress_size} completado en {time.time()-start:.4f}s")
except RuntimeError as e:
    print("Error de memoria:", e)

# -------------------------------
# 8️⃣ Operaciones combinadas
# -------------------------------
print("\n[8] Operaciones combinadas (forward+backward+update)")
w_combo = torch.randn(2,2, device=device, requires_grad=True)
b_combo = torch.randn(2,2, device=device, requires_grad=True)
x_combo = torch.randn(2,2, device=device)
for i in range(5):
    y_combo = torch.sin(x_combo @ w_combo + b_combo)
    loss_combo = (y_combo**2).mean()
    loss_combo.backward()
    with torch.no_grad():
        w_combo -= 0.1*w_combo.grad
        b_combo -= 0.1*b_combo.grad
    w_combo.grad.zero_()
    b_combo.grad.zero_()
print(f"Última loss combinada: {loss_combo.item():.6f}")

# -------------------------------
# 9️⃣ Guardado y carga de modelos
# -------------------------------
print("\n[9] Guardado y carga de modelos")
torch.save(model.state_dict(), "mininn_test.pt")
model_loaded = MiniNN().to(device)
model_loaded.load_state_dict(torch.load("mininn_test.pt"))
print("Modelo guardado y recargado correctamente.")

# -------------------------------
# 🔟 Precisión y consistencia CPU vs GPU
# -------------------------------
print("\n[10] Precisión CPU vs GPU")
if cuda_available:
    x_cpu = torch.randn(1000,1000)
    x_gpu = x_cpu.to(device)
    cpu_res = x_cpu.exp()
    torch.cuda.synchronize()
    gpu_res = x_gpu.exp()
    torch.cuda.synchronize()
    diff = (cpu_res - gpu_res.cpu()).abs().max().item()
    print(f"Diferencia máxima CPU vs GPU en exp(): {diff:e}")

print("\n✅ MULTITEST COMPLETADO")

