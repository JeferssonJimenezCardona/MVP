import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from fuzzywuzzy
# from fuzzywuzzy import process
st.set_page_config(
    page_title="Fuzzy Matching con Streamlit",
    page_icon=":mag:",
    layout="wide",
    initial_sidebar_state="expanded",  # Expande la barra lateral por defecto
)
color_negro = "#000000"
color_blanco = "#FFFFFF"
st.markdown(
    f"""
    <style>
        body {{
            background-color: {color_negro};
            color: {color_blanco};
        }}
        .reportview-container {{
            background-color: {color_negro};
            color: {color_blanco};
        }}
        .sidebar .sidebar-content {{
            background-color: {color_negro};
            color: {color_blanco};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
def main():
    st.title("Proof of concept: DataHarbor ID/ML")
    # Gráfico explicativo
    # st.subheader("Algoritmo de Aproximación:")
    # Expresión matemática de la similitud en formato Markdown
    st.write("### Expresión Matemática - Coeficiente de Similitud de Coseno:")
    st.write("$$Similarity(A, B) = \\frac{2 \\times LCS(A, B)}{len(A) + len(B)}$$")
    nombres = ["Jefersson Jimenez Cardona", "Jefersson Gimenez Carmona","Jennny Castellano", "Victor Hoyos", "Juan Sebastian Palomares"]
    correos = ["jefejica@gmail.com", "Prueba@hotmail.com","jefejica@hotmail.com"]
    cedulas = ["1020439778", "11524367891"]
    nombre_usuario = st.sidebar.text_input("Ingrese el nombre:", "")
    correo_usuario = st.sidebar.text_input("Ingrese el correo:", "")
    cedula_usuario = st.sidebar.text_input("Ingrese la cédula:", "")    
    aproximacion_nombre = process.extractOne(nombre_usuario, nombres)
    aproximacion_correo = process.extractOne(correo_usuario, correos)
    aproximacion_cedula = process.extractOne(cedula_usuario, cedulas)
    st.subheader("Resultado de Aproximación para Nombre:")
    st.write(f"Entrada del usuario: {nombre_usuario}")
    st.write(f"Mejor coincidencia: {aproximacion_nombre[0]}")
    st.write(f"Puntaje de coincidencia: {aproximacion_nombre[1]}") 
    st.subheader("Resultado de Aproximación para Correo:")
    st.write(f"Entrada del usuario: {correo_usuario}")
    st.write(f"Mejor coincidencia: {aproximacion_correo[0]}")
    st.write(f"Puntaje de coincidencia: {aproximacion_correo[1]}")
    st.subheader("Resultado de Aproximación para Cédula:")
    st.write(f"Entrada del usuario: {cedula_usuario}")
    st.write(f"Mejor coincidencia: {aproximacion_cedula[0]}")
    st.write(f"Puntaje de coincidencia: {aproximacion_cedula[1]}")  

    # st.subheader("Algoritmo de Aproximación:")
    # # Expresión matemática de la similitud en formato Markdown
    # st.write("### Expresión Matemática de Similitud:")
    # st.write("$$Similarity(A, B) = \\frac{2 \\times LCS(A, B)}{len(A) + len(B)}$$")
    plot_data = {"Nombre": aproximacion_nombre[1],
                 "Correo": aproximacion_correo[1],
                 "Cédula": aproximacion_cedula[1]}  
    # fig, ax = plt.subplots()
    # sns.barplot(x=list(plot_data.keys()), y=list(plot_data.values()), palette="Blues_d", ax=ax)
    # ax.set_title("Score de Coincidencia")
    # ax.set_ylabel("Puntaje")
    # ax.set_xlabel("Eje X ")
    # st.pyplot(fig)

    plot_data = {"Nombre": aproximacion_nombre[1],
                 "Correo": aproximacion_correo[1],
                 "Cédula": aproximacion_cedula[1]}

    fig, ax = plt.subplots()
    ax.plot(list(plot_data.keys()), list(plot_data.values()), marker='o', linestyle='-', color='b')
    ax.set_title("Score de Coincidencia")
    ax.set_ylabel("Puntaje")
    ax.set_xlabel("Métrica")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
