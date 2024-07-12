import streamlit as st
from datetime import datetime
def app():
# Title and header
    
    st.title(" 😘😘😘😘😘😘😘😘😘😘😘 Happy one year anniversary my love   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")
    st.header("This is a part of my gift to celebrate this magical day")

# Anniversary date
    anniversary_date = datetime(2023, 7, 13)  # Replace with your actual anniversary date
    today_date = datetime.now()
    days_together = (today_date - anniversary_date).days

# Display the message
    st.write(f"Today marks {days_together} days since we started our beautiful journey together.")

# Adding a special message
    st.subheader("To My Dearest semsem 💕💕")
    st.write("""
    This amazing journey started a year ago, and it has been nothing short of wonderful. 
    Every moment with you has been a treasure, and I look forward to spend my entire life beside you.

    You are my sunshine on a rainy day, my comfort in times of need, and my best friend. 
    I am so grateful to have you in my life, and I cherish every moment we spend together.

    I love you in ways that words can not describe, you are one of a kind and there is none like you.
    Your eyes light up my entire world, and your smile brings out the inner child in me, it just fills me with joy.

    You are just perfect beyond explaination, God's greatest creation.  
    I love everything about you, the way you walk, the way you talk, your hands OHH your hands
    everytime I touch them, it brings me inner peace, it makes me feel like I own the world. I adore your hands


         
    I lloveeee Youuuuuu 🌹🌹😘😘😘
    

    """)

# Display a lovely image
    st.title("Let me take you to a trip down memory lane")
    st.header("where I show you some of our favorite memories")
    st.header("there is a button in the top left corner of the screen, press it")





