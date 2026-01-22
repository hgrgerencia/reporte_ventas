import streamlit as st

from componentes.contacto import paginacontacto
from componentes.mesoneros import paginamesoneros
from componentes.reporte import paginareporte

st.set_page_config(
    page_title="Reportes Ribs", 
    page_icon="img/ribs.ico",
    layout="centered" 
)

hide_st_style = """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
    

def menu():
    # Crear el menú lateral
    USER=st.secrets["USER"]
    st.sidebar.write(f"Bienvenido... ")
    st.sidebar.image("img/ribs.jpg",width=140)
    st.sidebar.divider()
    USUARIO = st.sidebar.text_input("Nombre usuario: ")
    # Lista de páginas

    indice = {
            "Inicio": paginareporte,
            "Mesoneros": paginamesoneros,
            "Contacto": paginacontacto
        }
    st.sidebar.title("Menú")
    menu = st.sidebar.radio("Navega a:", list(indice.keys()))
    indice[menu]()

    
menu()





