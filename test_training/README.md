# Test Training PyTorch

Este script realiza un **mini entrenamiento lineal** en PyTorch usando descenso de gradiente manual.  
La función objetivo es `y = 4x + 1`, y el script muestra cómo:

1. Definir parámetros entrenables.
2. Calcular forward y loss.
3. Hacer backward para obtener gradientes.
4. Actualizar parámetros manualmente.
5. Resetear gradientes en cada paso.

## Uso

1. Clonar o descargar el repositorio.
2. Ir a la carpeta del script:
```bash
cd test_training
```

## Ejecutar:

```bash
python test_training.py
```

## Ejemplo de salida

```
Dispositivo: cuda
Paso 00 | Loss: 159.173859 | w: 3.3536 | b: 0.1323
Paso 01 | Loss: 4.305468 | w: 3.9031 | b: 0.2190
...
Paso 19 | Loss: 0.000001 | w: 3.9999 | b: 1.0000
```

## Compatibilidad

```
Python 3.x
PyTorch 2.x
Funciona en CPU o GPU (Windows, Linux, MacOS)
```
