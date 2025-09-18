"""
Problema 2
En resumen identificar la extensión de un archivo y mapearla a su tipo MIME correspondiente
"""

# Diccionario de extensiones a MIME
mime_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

nombre_archivo = input("Nombre del archivo: ").strip()

partes = nombre_archivo.split(".")

# Extraer extensión o usar None si no existe
if len(partes) > 1:
    extension = partes[-1].lower()  # Último elemento en minúsculas
else:
    extension = None  # No tiene extensión

# Obtener tipo MIME (o valor por defecto)
tipo_mime = mime_types.get(extension, "application/octet-stream")

print(f"Tipo MIME: {tipo_mime}")
