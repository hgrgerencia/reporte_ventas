import streamlit as st
import pandas as pd
import openpyxl

def paginamesoneros():
    st.title("Reporte de mesoneros")
    with st.container():
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

            # cambiar por nombres de mesoneros
            df.loc[df[6] == 'MESONERO01', 6] = 'LILIANNYS GRACIA'
            df.loc[df[6] == 'MESONERO02', 6] = 'EDUARDO GARCIA'
            df.loc[df[6] == 'MESONERO03', 6] = 'ELIAS SANCHEZ'
            df.loc[df[6] == 'MESONERO04', 6] = 'ADRIANA ANDRADE'
            df.loc[df[6] == 'MESONERO05', 6] = 'GURIS GUTIERREZ'
            df.loc[df[6] == '200', 6] = 'CAJA'
            df.loc[df[6] == 200, 6] = 'CAJA'
            df.loc[df[6] == '100', 6] = 'CAJA'
            df.loc[df[6] == 100, 6] = 'CAJA'
            # agrupando los items o productos x si mmismos y sumando sus cantidades
            df =df.groupby(6).agg({7: 'sum', 9: 'sum'}).reset_index() 
            # agregando encabezados a la tabla
            nuevos_encabezados = ['VENDEDOR','CANTIDADES', 'TOTAL'] 
            df.columns = nuevos_encabezados
            # visualizar sumatorias de cantidades y ventas
            suma_cantidades = round(df['CANTIDADES'].sum(),2)
            suma_total_venta =round(df['TOTAL'].sum(),2)
            st.write(f"Total de cantidades vendidas: {suma_cantidades}")
            st.write(f"Total de la venta: {suma_total_venta}")
            # visualizar tabla
            st.dataframe(df)

    

