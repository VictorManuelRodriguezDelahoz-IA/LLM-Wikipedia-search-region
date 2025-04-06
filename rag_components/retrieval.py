from sentence_transformers import SentenceTransformer
import chromadb

def recuperar_documentos_relevantes(consulta, coleccion, modelo_embeddings, num_resultados=2):
    """
    Recupera los documentos más relevantes de la base de datos vectorial para una consulta.

    Args:
        consulta (str): La consulta del usuario en texto plano.
        coleccion (chromadb.Collection): La colección de ChromaDB que contiene los embeddings.
        modelo_embeddings (SentenceTransformer): El modelo de Sentence Transformers para generar embeddings de la consulta.
        num_resultados (int): El número de documentos más relevantes a recuperar (por defecto es 3).

    Returns:
        list: Una lista de los documentos (strings) más relevantes, o None si hay un error.
    """
    try:
        # Generar el embedding de la consulta
        consulta_embedding = modelo_embeddings.encode([consulta])

        # Buscar en la base de datos vectorial
        resultados = coleccion.query(
            query_embeddings=consulta_embedding,
            n_results=num_resultados
        )

        # Devolver los documentos recuperados
        documentos_recuperados = resultados['documents'][0]
        return documentos_recuperados

    except Exception as e:
        print(f"Error durante la recuperación de documentos: {e}")
        return None