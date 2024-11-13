import streamlit as st

from componentes.contacto import paginacontacto
from componentes.mesoneros import paginamesoneros
from componentes.reporte import paginareporte

st.set_page_config(
    page_title="Reportes Ribs", 
    page_icon="img/ribs.ico",
    layout="centered" 
)
    

def menu():
    # Crear el menú lateral
    USER=st.secrets["USER"]
    st.sidebar.write(f"Bienvenido {USER}")
    st.sidebar.image("img/ribs.jpg",width=140, use_container_width=True)
    st.sidebar.divider()
    # Lista de páginas
    indice = {
        "Inicio": paginareporte,
        "Mesoneros": paginamesoneros,
        "Contacto": paginacontacto,
    }
    st.sidebar.title("Menú")
    menu = st.sidebar.radio("Navega a:", list(indice.keys()))
    indice[menu]()

menu()




