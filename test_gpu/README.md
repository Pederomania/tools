# Test Torch CUDA

Este script verifica si PyTorch puede acceder a CUDA y muestra la GPU que se está usando.  
Es útil para comprobar que tu entorno está listo para ejecutar código en GPU.

## Uso

1. Clonar o descargar el repositorio.
2. Ir a la carpeta del script:
```bash
cd test_torch_cuda
```

## Ejecutar:
```
python test_torch_cuda.py
```

## Ejemplo de salida
```
CUDA disponible: True
GPU usada: NVIDIA RTX 4060
```
o si no hay GPU disponible:
```
CUDA disponible: False
GPU usada: CPU
```

## Compatibilidad
```
Python 3.x
PyTorch 2.x
Windows, Linux, MacOS
```
