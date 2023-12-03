import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from difflib import get_close_matches
from rapidfuzz import process

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

def get_best_match(user_input, choices, method="difflib"):
    if method == "difflib":
        matches = get_close_matches(user_input, choices)
        if matches:
            return matches[0], 100  # difflib no proporciona puntajes, así que se establece en 100
        else:
            return None, 0
    elif method == "rapidfuzz":
        result = process.extractOne(user_input, choices)
        return result[0], result[1]
    else:
        return None, 0

def main():
    st.title("Proof of concept: DataHarbor ID/ML")

    st.write("### Expresión Matemática - Coeficiente de Similitud de Coseno:")
    st.write("$$Similarity(A, B) = \\frac{2 \\times LCS(A, B)}{len(A) + len(B)}$$")

    nombres = ["Jefersson Jimenez Cardona", "Jefersson Gimenez Carmona", "Jennny Castellano", "Victor Hoyos", "Juan Sebastian Palomares"]
    correos = ["jefejica@gmail.com", "Prueba@hotmail.com", "jefejica@hotmail.com"]
    cedulas = ["1020439778", "11524367891"]

    nombre_usuario = st.sidebar.text_input("Ingrese el nombre:", "")
    correo_usuario = st.sidebar.text_input("Ingrese el correo:", "")
    cedula_usuario = st.sidebar.text_input("Ingrese la cédula:", "")

    aproximacion_nombre, puntaje_nombre = get_best_match(nombre_usuario, nombres, method="rapidfuzz")
    aproximacion_correo, puntaje_correo = get_best_match(correo_usuario, correos, method="rapidfuzz")
    aproximacion_cedula, puntaje_cedula = get_best_match(cedula_usuario, cedulas, method="rapidfuzz")

    st.subheader("Resultado de Aproximación para Nombre:")
    st.write(f"Entrada del usuario: {nombre_usuario}")
    st.write(f"Mejor coincidencia: {aproximacion_nombre}")
    st.write(f"Puntaje de coincidencia: {puntaje_nombre}")

    st.subheader("Resultado de Aproximación para Correo:")
    st.write(f"Entrada del usuario: {correo_usuario}")
    st.write(f"Mejor coincidencia: {aproximacion_correo}")
    st.write(f"Puntaje de coincidencia: {puntaje_correo}")

    st.subheader("Resultado de Aproximación para Cédula:")
    st.write(f"Entrada del usuario: {cedula_usuario}")
    st.write(f"Mejor coincidencia: {aproximacion_cedula}")
    st.write(f"Puntaje de coincidencia: {puntaje_cedula}")

    plot_data = {"Nombre": puntaje_nombre, "Correo": puntaje_correo, "Cédula": puntaje_cedula}

    fig, ax = plt.subplots()
    ax.plot(list(plot_data.keys()), list(plot_data.values()), marker='o', linestyle='-', color='b')
    ax.set_title("Score de Coincidencia")
    ax.set_ylabel("Puntaje")
    ax.set_xlabel("Métrica")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
