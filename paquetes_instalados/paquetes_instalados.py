from importlib.metadata import distributions

# Formato para mostrar nombre y versión de cada paquete
PACKAGE_FORMAT = "{name}=={version}"

def list_installed_packages():
    """
    Lista todas las librerías instaladas en el entorno Python actual
    y las imprime en consola con su versión.
    """
    for dist in distributions():
        # Nombre del paquete (si no existe metadata, usa el nombre interno)
        name = dist.metadata.get("Name", dist.name)
        version = dist.version
        print(PACKAGE_FORMAT.format(name=name, version=version))

if __name__ == "__main__":
    # Ejecuta la función principal
    list_installed_packages()
