import chromadb

def conectar_o_crear_coleccion(nombre_coleccion="wikipedia_search_db", persistencia=True, ruta_persistencia="./wikipedia_search_db"):
    """
    Conecta o crea una colección en ChromaDB.

    Args:
        nombre_coleccion (str, optional): El nombre de la colección.
                                          Por defecto es "wikipedia_search_db".
        persistencia (bool, optional): Indica si la base de datos debe ser persistente en disco.
                                       Por defecto es True.
        ruta_persistencia (str, optional): La ruta para la base de datos persistente.
                                           Por defecto es "./wikipedia_search_db".

    Returns:
        chromadb.Collection: La colección de ChromaDB, o None si hay un error.
    """
    try:
        if persistencia:
            client = chromadb.PersistentClient(path=ruta_persistencia)
        else:
            client = chromadb.Client()
        collection = client.get_or_create_collection(name=nombre_coleccion)
        print(f"Colección '{nombre_coleccion}' creada o cargada.")
        return collection
    except Exception as e:
        print(f"Error al conectar/crear la colección: {e}")
        return None


def agregar_datos_coleccion(coleccion, embeddings, documentos, ids):
    """
    Añade los embeddings y documentos a la colección de ChromaDB.

    Args:
        coleccion (chromadb.Collection): La colección de ChromaDB.
        embeddings (list): Una lista de embeddings.
        documentos (list): Una lista de documentos.
        ids (list): Una lista de IDs para los documentos.

    Returns:
        bool: True si los datos se agregaron correctamente, False si hubo un error.
    """
    try:
        coleccion.add(
            embeddings=embeddings,
            documents=documentos,
            ids=ids
        )
        print(f"Se han añadido {coleccion.count()} documentos a la colección '{coleccion.name}'.")
        return True
    except Exception as e:
        print(f"Error al agregar los datos a la colección: {e}")
        return False