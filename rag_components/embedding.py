from sentence_transformers import SentenceTransformer

def cargar_modelo_embeddings(modelo_nombre='all-MiniLM-L6-v2'):
    """
    Carga el modelo de Sentence Transformers.

    Args:
        modelo_nombre (str, optional): El nombre del modelo a cargar.
                                       Por defecto es 'all-MiniLM-L6-v2'.

    Returns:
        SentenceTransformer: El modelo cargado, o None si hay un error.
    """
    try:
        model = SentenceTransformer(modelo_nombre)
        print(f"Modelo '{modelo_nombre}' cargado exitosamente.")
        return model
    except Exception as e:
        print(f"Error al cargar el modelo '{modelo_nombre}': {e}")
        return None


def generar_embeddings(documentos, modelo):
    """
    Genera embeddings para una lista de documentos.

    Args:
        documentos (list): Una lista de strings, donde cada string representa un documento.
        modelo (SentenceTransformer): El modelo de Sentence Transformers a utilizar.

    Returns:
        list: Una lista de embeddings (arrays NumPy), o None si hay un error.
    """
    try:
        embeddings = modelo.encode(documentos)
        return embeddings
    except Exception as e:
        print(f"Error al generar los embeddings: {e}")
        return None