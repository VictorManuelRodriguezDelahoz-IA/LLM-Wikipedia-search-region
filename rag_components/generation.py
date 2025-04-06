def generar_respuesta_simple(consulta, documentos_contexto):
    """
    Genera una respuesta simple extrayendo información de los documentos de contexto.

    Args:
        consulta (str): La consulta del usuario.
        documentos_contexto (list): Una lista de documentos (strings) relevantes.

    Returns:
        str: Una respuesta simple basada en la información encontrada, o un mensaje indicando que no se encontró información clara.
    """
    if not documentos_contexto:
        return "No se encontraron documentos relevantes para responder a tu pregunta."

    respuesta = f"Basándome en la información encontrada:\n"
    for i, doc in enumerate(documentos_contexto):
        respuesta += f"{i+1}. {doc}\n"

    return respuesta