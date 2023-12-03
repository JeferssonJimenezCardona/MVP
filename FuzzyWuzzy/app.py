import streamlit as st
import matplotlib.pyplot as plt
from fuzzywuzzy import process

# Set Streamlit page configuration
st.set_page_config(
    page_title="Fuzzy Matching con Streamlit",
    page_icon=":mag:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define color variables
color_negro = "#000000"
color_blanco = "#FFFFFF"

# Set custom styling with Markdown
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

    # Display mathematical expression for cosine similarity
    st.write("### Expresión Matemática - Coeficiente de Similitud de Coseno:")
    st.write("$$Similarity(A, B) = \\frac{2 \\times LCS(A, B)}{len(A) + len(B)}$$")

    # Sample data
    nombres = ["Jefersson Jimenez Cardona", "Jefersson Gimenez Carmona", "Jennny Castellano", "Victor Hoyos", "Juan Sebastian Palomares"]
    correos = ["jefejica@gmail.com", "Prueba@hotmail.com", "jefejica@hotmail.com"]
    cedulas = ["1020439778", "11524367891"]

    # User input
    nombre_usuario = st.sidebar.text_input("Ingrese el nombre:", "")
    correo_usuario = st.sidebar.text_input("Ingrese el correo:", "")
    cedula_usuario = st.sidebar.text_input("Ingrese la cédula:", "")

    # Fuzzy matching
    aproximacion_nombre = process.extractOne(nombre_usuario, nombres)
    aproximacion_correo = process.extractOne(correo_usuario, correos)
    aproximacion_cedula = process.extractOne(cedula_usuario, cedulas)

    # Display results
    display_results("Nombre", nombre_usuario, aproximacion_nombre)
    display_results("Correo", correo_usuario, aproximacion_correo)
    display_results("Cédula", cedula_usuario, aproximacion_cedula)

    # Plot scores
    plot_data = {"Nombre": aproximacion_nombre[1], "Correo": aproximacion_correo[1], "Cédula": aproximacion_cedula[1]}
    plot_scores(plot_data)

def display_results(title, user_input, fuzzy_match):
    st.subheader(f"Resultado de Aproximación para {title}:")
    st.write(f"Entrada del usuario: {user_input}")
    st.write(f"Mejor coincidencia: {fuzzy_match[0]}")
    st.write(f"Puntaje de coincidencia: {fuzzy_match[1]}")

def plot_scores(plot_data):
    fig, ax = plt.subplots()
    ax.plot(list(plot_data.keys()), list(plot_data.values()), marker='o', linestyle='-', color='b')
    ax.set_title("Score de Coincidencia")
    ax.set_ylabel("Puntaje")
    ax.set_xlabel("Métrica")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
