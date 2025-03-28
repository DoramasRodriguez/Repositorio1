import fitz  # PyMuPDF
import re  # Expresiones regulares

doc = fitz.open("D:\Escritorio\Repositorio1\Tarea 6 (BOE)\oposiciones.pdf")

# Expresión regular para buscar "jurista"
pattern = re.compile(r'\bjurista\b', re.IGNORECASE)

# Buscar en cada página
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text("text")
    
    # Buscar coincidencias con la expresión regular
    matches = pattern.findall(text)
    
    if matches:
        print(f"Encontrado en la página {page_num + 1}: {len(matches)} veces")