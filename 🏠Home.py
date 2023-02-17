import streamlit as st 

from utils import authentication, side_bar_colored,progress_bar
from streamlit_extras.switch_page_button import switch_page
import time
from st_on_hover_tabs import on_hover_tabs




st.set_page_config(page_title='CO2 Control',page_icon="./img/logo_1.png",initial_sidebar_state="collapsed", layout='wide')


side_bar_colored()

# st.markdown(page_background, unsafe_allow_html=True)



col1,col2,col3 = st.columns((1,2,1))
with col2:
    col1_,col2_,col3_ = st.columns((1,1,1))
    with col2_:
        st.image('./img/logo_1.png')
    st.write('---')
    st.markdown("<h1 style='text-align: center; color: #000000;'>📚 <br> CO2 Monitoring System in Classrooms </h1>", unsafe_allow_html=True)
    st.write('---') 
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    
    """)
    placeholder = st.empty()
    auth = placeholder.form('auth')

st.session_state['auth_'] = False



