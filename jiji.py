import streamlit as st

def app():
    st.header("jiji and joud wanted to celebrate this occasion with us and requested me to place them somewhere in the website, so here they are 😁😁😁")
    col1 ,col2=st.columns(2)
    with col1:
        st.image("./Images/jiji.JPEG",width=300)
    with col2:
        st.image("./Images/joud.jpg",width=300)