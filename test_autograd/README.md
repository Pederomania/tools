# Test Autograd PyTorch

Este script prueba el sistema de **autograd** de PyTorch, que permite calcular gradientes automáticamente.  
Es útil para verificar que tu entorno PyTorch está correctamente configurado y que los gradientes se calculan como se espera.

## Por qué hacemos este test

Autograd es el motor de diferenciación automática de PyTorch.  
Este test demuestra:

1. Que PyTorch reconoce el dispositivo (CPU/GPU).  
2. Cómo se definen parámetros "entrenables" (`requires_grad=True`).  
3. Cómo se realiza un forward simple.  
4. Cómo se ejecuta backward para obtener gradientes.

## Uso

1. Clonar o descargar el repositorio.
2. Ir a la carpeta del script:
```bash
cd test_autograd
```

## Ejecutar:

```bash
python test_autograd.py
```

## Ejemplo de salida:

```
Dispositivo: cuda
Resultado y: 49.0
Gradiente de w: 28.0
Gradiente de b: 14.0
```

## Compatibilidad

```
Python 3.x
PyTorch 2.x
Funciona en Windows, Linux y MacOS
```
