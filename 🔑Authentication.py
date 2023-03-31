import streamlit as st 

from utils import authentication, side_bar_colored
from streamlit_extras.switch_page_button import switch_page
import time


from db import get_user, authentication


# side_bar_colored()

# st.markdown(page_background, unsafe_allow_html=True)

st.set_page_config(page_title='CO2 Control',page_icon="./img/logo_1.png",initial_sidebar_state="collapsed", layout='wide')


col1_,col2_,col3_ = st.columns((1,0.5,1))
col1,col2,col3 = st.columns((1,2,1))
with col2_:
    st.image('./img/logo_1.png', use_column_width=True)
with col2:
    # with col2_:
    #     st.info('CO2 Control')
    st.write('---')
    st.markdown("<h1 style='text-align: center; color: #000000;'>👤 <br> CO2 Control Authentication </h1>", unsafe_allow_html=True)
    st.write('---') 
    placeholder = st.empty()
    auth = placeholder.form('auth')

st.session_state['auth_'] = False


with auth:
    auth.subheader('Login 🔐')
    auth.write(' ')
    user_input = auth.text_input('Username')
    auth.write(' ')
    password_input = auth.text_input('Password',type='password', max_chars=15)
    auth.write(' ')
    submit = auth.form_submit_button('Login',type = 'primary')

if submit:
    if get_user(user_input) != None:

        auth_flag,password,name,last_name,role,date_login,user_name = authentication(user_name_input=user_input,password_input=password_input)
    
        if auth_flag == False:
            l1,l2,l3 = st.columns((1,2,1))
            with l2:
                st.warning('Please checkout your credentials', icon = '💀')
        else:
            st.session_state['auth_'] = True
            st.session_state['name'] = name
            st.session_state['last_name'] = last_name
            st.session_state['role'] = role
            st.session_state['date_login'] = date_login
            st.session_state['key'] = user_name
            placeholder.empty()
            l_1,l_2,l_3 = st.columns((1,2,1))
            with l_2:
                st.success('Login Success, loading...', icon = '💥')
                st.info(f'Welcome: {name} {last_name} \n \n Role: {role}')
                time.sleep(3)
            switch_page("Classrooms")
    else:
        l1,l2,l3 = st.columns((1,2,1))
        with l2:
            st.error('The user dont exist, please contact to the @Administrator', icon = '💀')





hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)