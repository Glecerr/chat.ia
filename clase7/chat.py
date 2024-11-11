import streamlit as st
from groq import Groq

modelos = ["llama3-8b-8192","llama3-70b-8192","mixtral-8x7b-32768"]
modelo_en_uso = ""
cliente_usuario = ""
clave_secreta = ""
mensaje = ""

def crear_usuario():
    #LE ASIGNAMOS LA CLAVE A UNA VARIABLE
    clave_secreta = st.secrets["CLAVE_API"]
    #RETORNAMOS LA CLAVE COMO "api_key"
    return Groq(api_key=clave_secreta)

#ASIGNAR MODELO
def configurar_modelo(cliente, modelo, mensaje_de_entrada):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role" : "user", "content" : mensaje_de_entrada}],
        stream = True
    )

def configurar_pagina():
    #LA PESTAÑA
    st.set_page_config("Mi chat IA")
    #TITULO DE LA PAGINA
    st.title("Mi chat IA")
    #SIDEBAR
    st.sidebar.title("Panel de Modelos")
    #SELECTOR DE MODELOS
    m = st.sidebar.selectbox("Modelos", modelos, 0)
    #DEVUELVO EL VALOR DE LO SELECCIONADO
    return m

#INICIALIZAR ESTADO SI EL ESTADO NO EXISTE
def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

#INICIALIZAMOS EL ESTADO "MENSAJES"
inicializar_estado()

#INICIALIZAMOS LA PAGINA
modelo_en_uso = configurar_pagina()

#INICIALIZAMOS EL CLIENTE USUARIO CON LA API KEY
cliente_usuario = crear_usuario()

#EL USUARIO TIENE QUE ESCRIBIR ALGO
mensaje = st.chat_input()

#SI ESCRIBE ALGO, SE INICIALIZA EL MODELO
if mensaje:
    configurar_modelo(cliente_usuario, modelo_en_uso, mensaje)
    print(mensaje)
