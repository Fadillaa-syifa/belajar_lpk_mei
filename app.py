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
import streamlit as st

left, middle, right = st.columns(3)
if left.button("Plain button", width="stretch"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", width="stretch"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")
import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")
import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
