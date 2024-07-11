import streamlit as st
from PIL import Image
def app():
    st.header("This past year")
    st.write("""
You have filled my entire life with joy, luck and peace. Each day I've spent felt like a dream; the type of dream
you never want to wake up from. Each day with you by my side is a blessing from god almighty. 
You are the bightest and only star that shines my nights. 
             """)
    st.write("""
And just like Chandler once said to Monica:
"when you get upset about the little things, I think that I'm pretty good at making you feel better about that,
and that is good. So, people will say that you are high maintenance, but it is ok, because I love maintaining you."
            """)
    st.write("""
Now enough of the talk, let us wrap our first year together with some of our favorite memories, but one last thing 
before we get going, let me remind you that, I LOVE YOUUUUU MORE THAN ANYTHING and ANYONE IN THIS WORLD❤️❤️❤️❤️🌹🌹🌹😘😘😘
            """)
#------------------------------------------------------------------------------------------------
    st.header("First pic you took of yourself on my old rusty phone")
    st.write("Yet, it couldn't but get you looking as beatiful as you have ever been")
    st.image("./Images/1st_myphone.png",caption="10/8/2023",width=300)
#--------------------------------------------------------------------------------------------------
    st.header("First fit check")
    st.write("you had me leave the coffe house for a while just to admire the look")
    st.image("./Images/1st_fit.PNG",caption="18/8/2023",width=300)
#--------------------------------------------------------------------------------------------------------
    st.header("First time seeing baby semsem")
    st.write("The cutest baby to ever grace planet earth")
    col1, col2 = st.columns(2)  # Creates columns with equal width
    with col1:
        st.image("./Images/bobo1.jpg", width=300,caption="15/8/2023")
    with col2:
        st.image("./Images/bobo2.png", width=300,caption="15/11/2023")
#----------------------------------------------------------------------------------------------------------
    st.header("Our first video call")
    st.write("I was jumping with joy when you called, even though I've had just woken up")
    st.image("./Images/1st_vid_call.PNG", width=300,caption="27/12/2023")
#----------------------------------------------------------------------------------------------------------
    st.title("Our car moments")
    st.write("where we celebrated anniversaries, laughed, ate, fought, and most of our lovely times are spent here")
    col1, col2,col3= st.columns(3)  # Creates columns with equal width
    with col1:
        st.image("./Images/car1.JPEG", width=180,caption="4/1/2024")
    with col2:
        st.image("./Images/car2.JPEG", width=170,caption="3/12/2023")
    with col3:
        st.image("./Images/car3.JPG", width=160,caption="7/1/2024")


    st.header("Our 5th month anniversary")
    st.write("we wore the duck hoodies, and ate your favorite cakes at backseat while it was pouring rain outside")
    col4,col5,col6=st.columns(3) 
    with col4:
        st.image("./Images/5month.jpg", width=200,caption="13/12/2023")
    with col5:
        st.image("./Images/5m.JPEG", width=210,caption="13/12/2023")
    with col6:
        st.image("./Images/5m1.jpg", width=180,caption="13/12/2023")

    
    st.header("Our 6th month anniversary")
    st.write("where you got me my grey jacket & I got you our first son and daughter")
    col4,col5,col6=st.columns(3) 
    with col4:
        st.image("./Images/6month.JPEG", width=200,caption="10/1/2024")
    with col5:
        st.image("./Images/6m2.JPEG", width=210,caption="10/1/2024")
    with col6:
        st.image("./Images/6m3.JPEG", width=180,caption="10/1/2024")

#----------------------------------------------------------------------------------------------------------

    st.header("More car pics")
    st.write("which I completely adore BTW !!!")
    col4,col5,col6=st.columns(3) 
    with col4:
        st.image("./Images/last day Y4S1.jpg", width=220,caption="last day of first semester 4th year \n 6/2/2024")
    with col5:
        st.image("./Images/shmagh.jpg", width=210,caption="8/2/2024")
    with col6:
        #st.image(r"C:\Users\user\Desktop\web\images\shmagh2.PNG", width=210,caption="8/2/2024")
        st.image("./Images/shmagh2.PNG", width=210,caption="8/2/2024")
#----------------------------------------------------------------------------------------------------------
    st.header("venture lab days")
    st.write("a little secret, I used to go to these meetings just to spend time with you")
    st.image("./Images/venture.JPEG",width=300,caption="4/12/2023")
#----------------------------------------------------------------------------------------------------------
    st.header("The most beatiful woman to ever walk Earth")
    st.write("I love this picture a looottttt")
    st.image("./Images/lovely.JPEG",width=300,caption="20/12/2023")
#----------------------------------------------------------------------------------------------------------
    st.title("Our GP photos")
    st.header("GP1 pics")
    st.write("I am still waiting on them BTW, so please if you don't mind upload them right here")
    uploaded_file = st.file_uploader("Upload it please!!!!", type=None)  # Allow all file types

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Thank you 3asooolti for uploading it", width=300)
            st.write("Wallah it will not be saved anywhere I promise😂😂😂😂")
        except Exception as e:
            st.error(f"Error: The uploaded file might not be a valid image.")
    
    st.header("GP2 pics")
    st.write("To this day I am really proud of you, and I still can't get over how amazing the entire look was (I am super lucky)")
    col1,col2=st.columns(2)

    with col1:
        st.image("./Images/dis.jpg",width=300,caption="31/5/2024")
    with col2:
        st.image("./Images/dis2.JPEG",width=300,caption="31/5/2024")

    st.header("this nearly concludes the journey we have been through")
    st.write(r"there is still more if you could please scroll to the top and check the 'and how it is going' tab")
    st.write("sorry for the inconvenience, but streamlit has no button to navigate through pages")    