import streamlit as st

st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

# Título
st.title("🌡️ Conversor de Temperatura")
st.write("Convierte fácilmente entre Celsius y Fahrenheit")

# Selección de conversión
opcion = st.radio(
    "Seleccione la conversión:",
    ("Celsius ➡️ Fahrenheit", "Fahrenheit ➡️ Celsius")
)

# Entrada del valor
valor = st.number_input("Ingrese el valor a convertir:", step=0.1)

# Conversión según la opción elegida
if opcion == "Celsius ➡️ Fahrenheit":
    resultado = (valor * 9/5) + 32
    st.success(f"{valor} °C equivalen a {resultado:.2f} °F")

elif opcion == "Fahrenheit ➡️ Celsius":
    resultado = (valor - 32) * 5/9
    st.success(f"{valor} °F equivalen a {resultado:.2f} °C")

