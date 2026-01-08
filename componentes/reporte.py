import streamlit as st
import pandas as pd
import openpyxl
from datetime import datetime

def paginareporte():
    with st.container():
        st.subheader("Ribs Burger de Venezuela")
        st.title("Reportes de Ventas")  
    df = None
    with st.container():
        # capturar valor del dolar
        st.write("---")
        # Título de la aplicación
        st.header("Selecciona una Fecha")
        # Input de fecha
        fecha_seleccionada = st.date_input("Elige una fecha", datetime.today())
        st.header("Valor del Dolar para el reporte de venta")
        dolar = st.number_input("Ingrese el valor del dólar:", min_value=0.00, max_value=900.00, value=0.00)
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
            
            # Contar el número de celdas distintas a ""
            numero_tickets = df[0][df[0] !=""].count()#nunique()
            
            # agregando fila de monto total por producto
            valores_exentos = ['RUTA CORTA','RUTA MEDIA','RUTA LARGA']
            df[10] = df.apply(
                lambda row: round((row[9] * (1/dolar*1.16)),2) if row[4] not in valores_exentos else round((row[9] * (1/dolar)),2), axis=1
            )
            # agrupando los items o productos x si mmismos y sumando sus cantidades
            df =df.groupby(4).agg({7: 'sum', 10: 'sum'}).reset_index() 
            df[3] = df.apply(
                lambda row: round((row[10] / row[7]),2) , axis=1
            )
            # agregando encabezados a la tabla
            nuevos_encabezados = ['PRODUCTOS','CANTIDADES', 'TOTAL','PRECIO'] 
            df.columns = nuevos_encabezados
            
            # visualizando los resultados
            #col1, col2 = st.columns(2)
            # with col1:
            # with col2:
            # visualizar sumatorias de cantidades y ventas
            suma_cantidades = round(df['CANTIDADES'].sum(),2)
            st.write(f"Total de cantidades vendidas: {suma_cantidades}")
            
            suma_total_venta =round(df['TOTAL'].sum(),2)
            st.write(f"Total de la venta: {suma_total_venta}")
            
            st.write(f"Número de ticket del día: {numero_tickets}")
            
            # visualizar tabla
            st.dataframe(df)
            
            # Filtrar productos de helados
            helados_cali = ['BARQUILLA','MALTEADA','COPA DE HELADO','TINITA DE 1 PORCION','TINITA DE 2 PORCIONES']
            df_helados = df[df['PRODUCTOS'].isin(helados_cali)]
            st.write("---")
            st.header("Ventas de helados")
            st.dataframe(df_helados)
            
            # visualizar sumatorias de cantidades y ventas de helados
            suma_cantidades_helados = round(df_helados['CANTIDADES'].sum(),2)
            suma_total_venta_helados =round(df_helados['TOTAL'].sum(),2)
            st.write(f"Total de cantidades clientes: {suma_cantidades_helados}")
            st.write(f"Total de la venta de helado: {suma_total_venta_helados}")
            # Número de teléfono (incluyendo código de país, pero sin el +)
            telefono = "5804148981405"  # Reemplaza con el número de destino
            mensaje = f"*Fecha reporte Helados: {fecha_seleccionada}*%0ATotal venta: {suma_total_venta_helados}%0ATotal clientes: {suma_cantidades_helados}"
            # Codifica el mensaje para que sea seguro para URL
            mensaje_encoded = mensaje.replace(" ", "%20")
            # Crea la URL de WhatsApp
            url_whatsapp = f"https://api.whatsapp.com/send?phone={telefono}&text={mensaje_encoded}"
            # Inserta un enlace en Streamlit
            st.markdown(f"[Enviar reporte a WhatsApp]({url_whatsapp})")

