import streamlit as st

st.set_page_config(
  page_title="Silver Expert",
  page_icon="🧊",
  layout="centered"
)

# Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
st.write("Hello, *World!* :sunglasses:")
title = st.text_input("Movie title", "Avengers End Game")
st.write("The current movie title is", title)
import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
