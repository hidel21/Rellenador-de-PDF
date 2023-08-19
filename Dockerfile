# Usar una imagen base de Python (en este caso, Python 3.9)
FROM python:3.9

# Establecer un directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de tu aplicación al contenedor
COPY . .

# Establecer el comando por defecto para tu contenedor
CMD ["python", "./script-reader.py"]

EXPOSE 5000