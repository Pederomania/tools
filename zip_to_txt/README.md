# ZIP a TXT

Este script convierte un archivo ZIP que contiene múltiples archivos en un solo archivo `.txt`.  
Filtra por extensiones válidas y formatea JSON minificado para hacerlo legible.

## Funcionalidades

- Convierte `.zip` en un `.txt` unificado.
- Filtra solo archivos con extensiones válidas: `.py`, `.js`, `.md`, `.txt`, `.json`.
- Detecta JSON minificado y lo formatea automáticamente.
- Ignora carpetas y archivos ocultos.

## Uso

1. Clonar o descargar el repositorio.
2. Ir a la carpeta del script:
```bash
cd zip_to_txt
```
Modificar la variable ZIP_PATH en el script con la ruta de tu archivo .zip.


## Ejecutar:

```bash
python zip_to_txt.py
```

## Ejemplo de salida en txt

```
ZIP: nombre_del_archivo.zip
Total entradas: 12
==============================================================================================================

ARCHIVO: ejemplo.py
--------------------------------------------------------------------------------------------------------------
print("Hola Mundo")
==============================================================================================================

ARCHIVO: config.json
--------------------------------------------------------------------------------------------------------------
{
  "clave": "valor",
  "lista": [1,2,3]
}
==============================================================================================================

```

## Compatibilidad

```
Python 3.8+
Windows, Linux, MacOS
```
