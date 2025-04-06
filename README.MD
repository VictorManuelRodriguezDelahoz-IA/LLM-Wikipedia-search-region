Pasos :

1. Scrapping de la fuente de wikipedia
2. Tratamiento del dato
3. Embbeding
4. Ingreso en la base de datos vectorial
5. Funcion de llamada de usuario
6. Creacion del agente RAG
7. Volver modular el codigo
8. Aplicar linters y pretiers
9. Crear docker
10. Buscar la manera de exponer en la web de la manera mas optima
11. Organizar los cambios bien en git

Detalles:
-La base de datos vectorial en Chroma esta guardada en disco, despues cuando la pasemos a produccion tendremos que cambiar esta logica para darle la ruta de guardado en un servicio de base de datos en la nube. Podriamos considerar dejar un servidor dedicado o una base de datos vectorial como pinecone para exponer estos datos estando arriba.