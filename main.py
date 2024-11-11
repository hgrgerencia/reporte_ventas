# pip install streamlit streamlit-lottie Pillow openpyxl
import streamlit as st
import pandas as pd
import openpyxl as xl

def pagina_home():
    with st.container():
        st.subheader("Ribs Burger de Venezuela")
        st.title("Reportes de Ventas")  
    df = None
    with st.container():
        st.write("---")
        st.header("Cargue su archivo excel")
        df = st.file_uploader("Cargue su archivo excel", type=["xlsx"])
        col1, col2 = st.columns(2)
        if df is not None:
            df = pd.read_excel(df, header=None)
            df =df.groupby( 4)[7].sum().reset_index()
            nuevos_encabezados = ['PRODUCTOS','CANTIDADES'] 
            df.columns = nuevos_encabezados
            with col1:
                st.dataframe(df)
            with col2:
                suma_cantidades =df['CANTIDADES'].sum()
                st.write(f"Total de cantidades vendidas: {suma_cantidades}")

def pagina_acerca_de():
    st.title("Acerca de")
    st.write("Esta aplicación está creada con Streamlit y tiene un menú interactivo.")

def pagina_contacto():
    st.title("Contacto")
    st.write("Puedes contactarnos a través del correo: ejemplo@dominio.com")

# Lista de páginas
paginas = {
    "Inicio": pagina_home,
    "Acerca de": pagina_acerca_de,
    "Contacto": pagina_contacto,
}

# Crear el menú lateral
st.sidebar.title("Menú")
pagina_seleccionada = st.sidebar.radio("Navega a:", list(paginas.keys()))

# Ejecutar la función de la página seleccionada
paginas[pagina_seleccionada]()



