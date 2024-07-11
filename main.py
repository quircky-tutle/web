#import streamlit as st
#from streamlit_option_menu import option_menu
#import home, pics,between

#st.set_page_config(page_title="Anniversay website")

#class MultiAPP:
#    def __init__(self):
#        self.apps=[]
#    def add_app(self,title,function):
#        self.apps.append({
#            "title":title,
#            "function": function
#        })
#    def run():
#        with st.sidebar:
#             app=option_menu(
#                 menu_title="Contents",
#                 options=['Words from my heart',"A trip down memory lane"]
#             )
#        
#        if app=="Words from my heart":
#            home.app()
#        #if app=="A trip down memory lane":
#            #pics.app()
#        elif app == "A trip down memory lane":
#            submenu = option_menu(
#                menu_title="A trip down memory lane",
#                options=['How it started and how it is going', 'And what is between', 'Submenu 3'],
#                icons=['star', 'star', 'star'],  # Optional icons
#                menu_icon="cast",  # Optional icon for the submenu
#                default_index=0,
#                orientation="horizontal"
#            )
 #           
 #           if submenu == "How it started and how it is going":
  #              pics.app() # Replace with your actual function
   #         elif submenu == "And what is between":
    #            between.app()  # Replace with your actual function
     #       #elif submenu == "Submenu 3":
      #          #submenu3_function()  # Replace with your actual function
#app = MultiAPP()
#app.run()












import streamlit as st
from streamlit_option_menu import option_menu
import home, pics, between, now, jiji

st.set_page_config(page_title="Anniversary website")



class MultiAPP:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="What is in here",
                options=['Words from my heart', "A trip down memory lane","Special Request"],
                icons=['heart','clock',"star"]
            )
        
        if app == "Words from my heart":
            home.app()
        elif app == "A trip down memory lane":
            submenu = option_menu(
                menu_title="A trip down memory lane",
                options=['How it started', 'what is in between', 'And how is it going'],
                icons=['star', 'star', 'star'],  # Optional icons
                menu_icon="cast",  # Optional icon for the submenu
                default_index=0,
                orientation="horizontal"
            )
            
            if submenu == "How it started":
                pics.app()  # Replace with your actual function
            elif submenu == "what is in between":
                between.app()  # Replace with your actual function
            # Uncomment and replace with your actual function if needed
            elif submenu == "And how is it going":
                 now.app()  # Replace with your actual function
        if app =="Special Request":
            jiji.app()
# Initialize and run the app
app = MultiAPP()
app.run()
