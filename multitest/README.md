# MultiTest PyTorch

Este script realiza una batería de pruebas sobre el entorno PyTorch, CPU/GPU y operaciones tensoriales.  
Es útil para verificar instalación, rendimiento, autograd, entrenamiento y guardado de modelos.

## Pruebas incluidas

1. Instalación y versión de PyTorch, detección de GPU/CPU
2. Tensores y operaciones básicas (matmul, element-wise)
3. Test de autograd (gradientes)
4. Mini entrenamiento lineal (y = 4x + 1)
5. Mini red neuronal simple (y = x² + 2x + 1)
6. Optimización y reproducibilidad
7. Stress test de memoria GPU
8. Operaciones combinadas forward+backward+update
9. Guardado y carga de modelos
10. Precisión y consistencia CPU vs GPU

## Uso

1. Clonar o descargar el repositorio.
2. Situarse en la carpeta del script:
```bash
cd multitest
```
Nota: Para pruebas GPU, se requiere CUDA compatible. El script funciona en CPU si no hay GPU disponible.

## Ejemplo de salida
```
MULTITEST PYTORCH 
[1] Test instalación y versión
Torch version: 2.1.2
CUDA disponible: True
Usando dispositivo: cuda
GPU: NVIDIA RTX 4060
...
✅ MULTITEST COMPLETADO
```

## Compatibilidad
```
Python 3.x
PyTorch 2.x
Windows, Linux, MacOS
```
