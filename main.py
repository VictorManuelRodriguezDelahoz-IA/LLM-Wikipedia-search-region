import os
from rag_components import data_loading, embedding, vector_db, retrieval, generation

# Configuración (ajusta según tu proyecto)
url = "https://es.wikipedia.org/wiki/Geograf%C3%ADa_de_Colombia"
modelo_nombre_embeddings = 'all-MiniLM-L6-v2'
nombre_coleccion = "departamentos_capitales"
persistencia = True  # Si quieres guardar la base de datos en disco
ruta_persistencia = "./wikipedia_search_db"

# 1. Cargar y preparar los datos
df = data_loading.cargar_datos(url)
if df is None:
    exit()
documentos = data_loading.preparar_datos(df)
if documentos is None:
    exit()

# 2. Cargar el modelo de embeddings y generar los embeddings
modelo_embeddings = embedding.cargar_modelo_embeddings(modelo_nombre_embeddings)
if modelo_embeddings is None:
    exit()
embeddings = embedding.generar_embeddings(documentos, modelo_embeddings)
if embeddings is None:
    exit()

# 3. Conectar/Crear la base de datos vectorial y agregar los datos
coleccion = vector_db.conectar_o_crear_coleccion(nombre_coleccion, persistencia, ruta_persistencia)
if coleccion is None:
    exit()
ids = [f"doc_{i}" for i in range(len(documentos))]
if not vector_db.agregar_datos_coleccion(coleccion, embeddings, documentos, ids):
    exit()

# 4. Obtener la consulta del usuario (esto es un ejemplo, puedes obtenerla de otra manera)
consulta_usuario = "Cual es la capital de Santander?"
print(consulta_usuario)

# 5. Recuperar los documentos relevantes
documentos_relevantes = retrieval.recuperar_documentos_relevantes(
    consulta_usuario, coleccion, modelo_embeddings
)

# 6. Generar la respuesta
if documentos_relevantes:
    respuesta = generation.generar_respuesta_simple(consulta_usuario, documentos_relevantes)
    print("\nRespuesta:\n", respuesta)
else:
    print("No se encontraron documentos relevantes.")