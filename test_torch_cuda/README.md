# Test Torch CUDA

Este script compara el rendimiento de CPU vs GPU para multiplicación de matrices grandes en PyTorch.  
Sirve para comprobar:

1. Disponibilidad de CUDA y GPU.
2. Velocidad de operaciones matriciales en CPU y GPU.
3. Precisión de los resultados entre CPU y GPU.

## Uso

1. Clonar o descargar el repositorio.
2. Ir a la carpeta del script:
```bash
cd test_torch_cuda
```

## Ejecutar:

```bash
python test_torch_cuda.py
```

## Ejemplo de salida

```
Torch version: 2.1.2
CUDA disponible: True
GPU: NVIDIA RTX 4060
Tiempo CPU: 12.345 s
Tiempo GPU: 0.678 s
Diferencia máxima CPU vs GPU: 1.2e-07
```
Nota: Si no hay GPU disponible, el script se ejecuta solo en CPU y la diferencia máxima será cero.

## Compatibilidad

```
Python 3.x
PyTorch 2.x
Windows, Linux, MacOS
```
