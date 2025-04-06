# Usa una imagen base de Python con la versión 3.13.2
FROM python:3.13.2-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia solo los archivos de código fuente al contenedor
COPY rag_components/ rag_components/
COPY main.py .
COPY .env .  # Copia el archivo .env (si lo usas para la API key)

# Define el comando que se ejecutará cuando se inicie el contenedor
CMD ["python", "main.py"]