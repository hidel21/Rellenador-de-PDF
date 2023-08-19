import mysql.connector
import PyPDF2
import streamlit as st

# Conexión a la base de datos
def conectarse_bd():
    conn = mysql.connector.connect(
        host='tu_host',
        user='tu_usuario',
        password='tu_contraseña',
        database='tu_base_de_datos'
    )
    return conn

# Función para rellenar y descargar el PDF
def rellenar_y_descargar_pdf(archivo_pdf, datos):
    lector = PyPDF2.PdfFileReader(archivo_pdf)
    escritor = PyPDF2.PdfFileWriter()

    pagina = lector.getPage(0)
    campos_formulario = pagina['/Annots'][0].getObject()

    for campo, valor in datos.items():
        if campo in campos_formulario:
            campos_formulario[campo].update({
                PyPDF2.generic.NameObject("/V"): PyPDF2.generic.createStringObject(str(valor))
            })

    escritor.addPage(pagina)

    # Guardar el PDF rellenado con un nuevo nombre
    ruta_pdf_rellenado = 'pdf_rellenado_rapido_sin_riesgo.pdf'
    with open(ruta_pdf_rellenado, 'wb') as pdf_rellenado:
        escritor.write(pdf_rellenado)

    return ruta_pdf_rellenado

# Interfaz gráfica con Streamlit
st.title("Rellenar PDF desde Base de Datos")

# Selección de archivo PDF
archivo_pdf = st.file_uploader("Seleccionar archivo PDF", type=["pdf"])

if archivo_pdf is not None:
    st.write("¡Archivo PDF cargado exitosamente!")
    
    try:
        with conectarse_bd() as conn:
            cursor = conn.cursor()
            
            consulta = "SELECT fecha_peticion, ... FROM nombre_tabla LIMIT 1"
            cursor.execute(consulta)
            datos_tuple = cursor.fetchone()
            
            # Convertir la tupla a un diccionario
            datos = {col: val for col, val in zip(cursor.column_names, datos_tuple)}
            
            if datos:
                # Mostrar los datos de la base de datos
                st.write("Datos obtenidos de la base de datos:")
                for campo, valor in datos.items():
                    st.write(f"{campo}: {valor}")

                # Botón para rellenar y descargar el PDF
                if st.button("Rellenar y Descargar PDF"):
                    ruta_pdf_rellenado = rellenar_y_descargar_pdf(archivo_pdf, datos)
                    st.success(f"El PDF rellenado se guardó en: {ruta_pdf_rellenado}")
            else:
                st.warning("No se encontraron datos en la base de datos.")

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
