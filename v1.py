import streamlit as st
import pandas as pd
from difflib import SequenceMatcher

# Cargar el archivo Excel
df = pd.read_excel("registros_ficticios.xlsx", engine="openpyxl")

# Función para calcular similitud entre dos textos
def calcular_similitud(a, b):
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()

# Título de la aplicación
st.title("Catálogo de Refacciones")

# Entrada de búsqueda
descripcion_input = st.text_input("🔍 Descripción a buscar")
umbral_similitud = st.slider("📊 Umbral de similitud", min_value=0.0, max_value=1.0, value=0.98, step=0.01)

# Procesar búsqueda
if descripcion_input:
    resultados = []
    for _, row in df.iterrows():
        sim = calcular_similitud(descripcion_input, row["Descripción"])
        if sim >= umbral_similitud:
            resultados.append(row)

    if resultados:
        st.success(f"Se encontraron {len(resultados)} coincidencias con al menos {int(umbral_similitud*100)}% de similitud.")
        st.dataframe(pd.DataFrame(resultados))
    else:
        st.warning("No se encontraron coincidencias. Puedes solicitar el alta de un nuevo material.")
        st.subheader("📋 Solicitud de Alta de Nuevo Material")
        with st.form("alta_material"):
            nueva_parte = st.text_input("Número de parte")
            nuevo_codigo = st.text_input("Código único")
            nuevo_sistema = st.text_input("Sistema")
            nueva_categoria = st.text_input("Categoría")
            nueva_descripcion = st.text_input("Descripción")
            fecha_solicitud = st.date_input("Fecha de solicitud")
            fecha_envio = st.date_input("Fecha de envío de solicitud")
            fecha_confirmacion = st.date_input("Fecha de confirmación")
            fecha_creacion = st.date_input("Fecha de creación")
            numero_contrato = st.text_input("Número de contrato")
            solicitante = st.text_input("Solicitante")
            enviar = st.form_submit_button("Enviar solicitud")

        if enviar:
            st.success("✅ Solicitud enviada correctamente (simulada).")
