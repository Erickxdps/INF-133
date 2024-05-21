def render_libro_list(libros):
    # Representa una lista de libros como una lista de diccionarios
    return [
        {
            "titulo": libro.titulo,
            "autor": libro.autor,
            "species": libro.edicion,
            "age": libro.disponibilidad,
        }
        for libro in libros
    ]
# Titulo, Autor, Edición y Disponibilidad

def render_libro_detail(libro):
    # Representa los detalles de un libro como un diccionario
    return {
            "titulo": libro.titulo,
            "autor": libro.autor,
            "species": libro.edicion,
            "age": libro.disponibilidad,
        }
