# Mostrar Estructura

Este script muestra en consola la estructura de carpetas y archivos de una ruta indicada.  
Filtra carpetas ocultas y la carpeta `venv` para una visualización limpia.

## Uso

1. Clonar o descargar el repositorio.
2. Abrir terminal y situarse en la carpeta donde está el script.
3. Ejecutar:

```bash
python mostrar_estructura.py
```

Por defecto, mostrará la estructura de la carpeta actual.
También puedes inspeccionar cualquier otra ruta modificando la variable ruta_objetivo en el script:

```
ruta_objetivo = "ruta/a/inspeccionar"
listar_contenido(ruta_objetivo)
```

## Ejemplo de salida

```
📁 Contenido de: proyecto_ejemplo

📂 proyecto_ejemplo/
    📂 src/
        📄 main.py
        📄 utils.py
    📂 data/
        📄 dataset.csv
    📄 README.md
```

## Compatibilidad

```
Python 3.x
Funciona en Windows, Linux y MacOS.
```
