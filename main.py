import streamlit as st
import pandas as pd
import openpyxl

def pagina_home():
    with st.container():
        st.subheader("Ribs Burger de Venezuela")
        st.title("Reportes de Ventas")  
    df = None
    with st.container():
        # capturar valor del dolar
        st.write("---")
        st.header("Valor del Dolar para el reporte de venta")
        dolar = st.number_input("Ingrese el valor del dólar:", min_value=0.00, max_value=100.00, value=0.00)
        # capturando el archivo excel a analizar
        st.write("---")
        st.header("Cargue su archivo excel")
        df = st.file_uploader("Cargue su archivo excel", type=["xlsx"])

        
        if df is not None:
            # cargar excel y pasarlo al datafame
            df = pd.read_excel(df, header=None)
            # limpiando el dataframe de los item de valor cero
            indices_a_eliminar = df[(df[4] == 'EXT. CEBOLLA') | (df[4] == 'EXT. LECHUGA') | (df[4] == 'EXT. TOMATE')].index
            df = df.drop(indices_a_eliminar)
            # agregando fila de monto total por producto
            valores_exentos = ['RUTA CORTA','RUTA MEDIA','RUTA LARGA', 'CAJA PARA LLEVAR', 'CAJA PARA LLEVAR COSTILLA']
            df[10] = df.apply(
                lambda row: round((row[9] * (1/dolar*1.16)),2) if row[4] not in valores_exentos else round((row[9] * (1/dolar)),2), axis=1
            )
            # agrupando los items o productos x si mmismos y sumando sus cantidades
            df =df.groupby(4).agg({7: 'sum', 10: 'sum'}).reset_index() 
            # agregando encabezados a la tabla
            nuevos_encabezados = ['PRODUCTOS','CANTIDADES', 'TOTAL'] 
            df.columns = nuevos_encabezados
            
            # visualizando los resultados
            #col1, col2 = st.columns(2)
            # with col1:
            # with col2:
            # visualizar sumatorias de cantidades y ventas
            suma_cantidades = round(df['CANTIDADES'].sum(),2)
            suma_total_venta =round(df['TOTAL'].sum(),2)
            st.write(f"Total de cantidades vendidas: {suma_cantidades}")
            st.write(f"Total de la venta: {suma_total_venta}")
            # visualizar tabla
            st.dataframe(df)

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



