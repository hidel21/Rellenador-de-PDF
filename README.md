# 📄 Rellenador de PDF desde Base de Datos

Esta herramienta fue desarrollada en Python y permite automatizar el proceso de completar formularios PDF utilizando datos de una base de datos MySQL. 

## 🌟 Características

- **Conexión a MySQL**: Establece una conexión con una base de datos MySQL.
- **Manipulación de PDFs**: Rellena formularios PDF automáticamente con datos específicos.
- **Interfaz gráfica**: Facilita la interacción con el usuario gracias a `streamlit`.

## 🛠 Instalación y uso

1. Asegúrate de tener todas las dependencias instaladas.
2. Modifica los parámetros de conexión a la base de datos con tus credenciales y configuración real.
3. Ejecuta el script y sigue las instrucciones en la interfaz gráfica.

## 🐳 Despliegue con Docker

### Requisitos

- [Docker](https://www.docker.com/get-started) instalado en tu máquina.

### Instrucciones

1. **Dockerfile**:

   Si aún no tienes un Dockerfile, aquí tienes una plantilla:

   ```plaintext
   # Usar una imagen base de Python (en este caso, Python 3.9)
   FROM python:3.9

   # Establecer un directorio de trabajo
   WORKDIR /usr/src/app

   # Copiar requirements.txt y luego instalar
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copiar todos los archivos
   COPY . .

   # Comando por defecto para el contenedor
   CMD ["python", "./script-reader.py"]

   EXPOSE 5000
   ```

2. **Construir la imagen**:

   ```bash
   docker build -t pdf_reader_image .
   ```

3. **Ejecutar la aplicación**:

   ```bash
   docker run -p 5000:5000 pdf_reader_image
   ```

4. **Acceso**:

   Abre tu navegador y dirígete a `http://localhost:5000`.

---
