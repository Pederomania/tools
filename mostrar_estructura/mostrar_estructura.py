import os

def listar_contenido(ruta):
    """
    Muestra en consola la estructura de carpetas y archivos de la ruta indicada.
    Excluye carpetas ocultas y la carpeta 'venv'.
    """
    print(f"📁 Contenido de: {ruta}\n")

    # Recorre la ruta de manera recursiva
    for raiz, carpetas, archivos in os.walk(ruta):
        # Filtrar carpetas: excluir ocultas y 'venv'
        carpetas[:] = [d for d in carpetas if not d.startswith('.') and d != 'venv']

        # Filtrar archivos ocultos
        archivos = [f for f in archivos if not f.startswith('.')]

        # Calcular nivel de indentación según profundidad
        nivel = raiz.replace(ruta, '').count(os.sep)
        indent = '    ' * nivel
        print(f"{indent}📂 {os.path.basename(raiz)}/")  # Carpeta actual

        # Mostrar archivos de la carpeta
        subindent = '    ' * (nivel + 1)
        for archivo in archivos:
            print(f"{subindent}📄 {archivo}")

if __name__ == "__main__":
    # Ruta que quieras inspeccionar
    # Por defecto usa la carpeta actual desde donde se ejecuta el script
    # cambiar por ruta_objetivo = "tu/ruta/a/inspeccionar"
    ruta_objetivo = os.getcwd() 
    listar_contenido(ruta_objetivo)

