import streamlit as st

def app():
    st.header("jiji, joud and farah wanted to celebrate this occasion with us and requested me to place them somewhere in the website, so here they are 😁😁😁")
    col1 ,col2,col3=st.columns(3)
    with col1:
        st.image("./Images/jiji.JPEG",width=200)
    with col2:
        st.image("./Images/joud.jpg",width=200)
    with col3:
        st.image("./Images/farah.jpg",width=200)