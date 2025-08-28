import streamlit as st

st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

# Título del aplicativo
st.title("🌡️ Conversor de Temperatura")
st.write("Transforma grados Celsius a Fahrenheit")

# Entrada del usuario
celsius = st.number_input("Ingrese la temperatura en °C:", value=0.0, step=0.1)

# Conversión
fahrenheit = (celsius * 9/5) + 32

# Mostrar resultado
st.success(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")
