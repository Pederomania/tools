import zipfile
import json
from pathlib import Path

# -------------------------------
# Configuración
# -------------------------------
EXTS_VALIDAS = {".py", ".js", ".md", ".txt", ".json"}
SEP = "\n" + "=" * 110 + "\n"

# -------------------------------
# Funciones auxiliares
# -------------------------------

def es_json_minificado(texto: str) -> bool:
    """
    Heurística para detectar JSON minificado:
    - Pocas líneas para su tamaño.
    - Comienza con { o [.
    """
    t = texto.strip()
    if not t:
        return False
    if not (t.startswith("{") or t.startswith("[")):
        return False
    lineas = t.count("\n") + 1
    if len(t) > 300 and lineas <= 3:
        return True
    if len(t) > 2000 and lineas < 10:
        return True
    return False

def pretty_print_json(texto: str) -> str:
    """
    Formatea un JSON para hacerlo legible.
    Si falla, devuelve el texto original.
    """
    try:
        obj = json.loads(texto)
        return json.dumps(obj, ensure_ascii=False, indent=2)
    except Exception:
        return texto

# -------------------------------
# Función principal
# -------------------------------
def zip_a_txt(zip_path: str):
    """
    Convierte un archivo ZIP en un solo archivo TXT.
    - Filtra por extensiones válidas.
    - Formatea JSON minificado.
    """
    zip_path = Path(zip_path)

    if not zip_path.exists():
        raise FileNotFoundError(f"No existe: {zip_path}")
    if zip_path.suffix.lower() != ".zip":
        raise ValueError("El archivo no es .zip")

    salida_txt = zip_path.with_suffix(".txt")

    with zipfile.ZipFile(zip_path, "r") as z:
        archivos = sorted(z.namelist())

        with open(salida_txt, "w", encoding="utf-8") as out:
            out.write(f"ZIP: {zip_path.name}\n")
            out.write(f"Total entradas: {len(archivos)}\n")
            out.write(SEP)

            for nombre in archivos:
                # Saltar carpetas
                if nombre.endswith("/"):
                    continue

                ext = Path(nombre).suffix.lower()
                if ext not in EXTS_VALIDAS:
                    continue

                out.write(f"ARCHIVO: {nombre}\n")
                out.write("-" * 110 + "\n")

                try:
                    contenido = z.read(nombre).decode("utf-8", errors="replace")
                except Exception as e:
                    out.write(f"[ERROR leyendo {nombre}: {e}]\n")
                    out.write(SEP)
                    continue

                # Formatear JSON minificado
                if ext == ".json" and es_json_minificado(contenido):
                    contenido = pretty_print_json(contenido)

                out.write(contenido.rstrip() + "\n")
                out.write(SEP)

    print(f"Generado: {salida_txt}")

# -------------------------------
# Ejecutable desde línea de comandos
# -------------------------------
if __name__ == "__main__":
    # >>> PON AQUÍ TU RUTA ZIP <<<
    ZIP_PATH = r"C:\Users\tu_Usuario\tu_ruta\nombre_del_archivo.zip"
    zip_a_txt(ZIP_PATH)
