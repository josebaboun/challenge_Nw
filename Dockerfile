# Define la imagen base
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la API al contenedor
COPY api /app

# Instala las dependencias de la API
RUN pip install -r /app/requirements.txt

# Expone el puerto en el que la API escucha
EXPOSE 5500

# Define el comando para ejecutar la API
CMD ["python", "/app/app.py"]
