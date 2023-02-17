import streamlit as st 

from utils import authentication, side_bar_colored,progress_bar
from streamlit_extras.switch_page_button import switch_page
import time
from st_on_hover_tabs import on_hover_tabs



side_bar_colored()

# st.markdown(page_background, unsafe_allow_html=True)



col1,col2,col3 = st.columns((1,2,1))
with col2:
    col1_,col2_,col3_ = st.columns((1,2,1))
    with col2_:
        st.image('./img/logo_2.png')
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

    authentication_flag,name,last_name,role,date_login = authentication(user=user_input,password=password_input)
    if authentication_flag == False:
        l1,l2,l3 = st.columns((1,2,1))
        with l2:
            st.warning('Please checkout your credentials', icon = '💀')
    else:
        st.session_state['auth_'] = True
        st.session_state['name'] = name
        st.session_state['last_name'] = last_name
        st.session_state['role'] = role
        st.session_state['date_login'] = date_login
        placeholder.empty()
        l_1,l_2,l_3 = st.columns((1,2,1))
        with l_2:
            st.success('Login Success, loading...', icon = '💥')
            st.info(f'Welcome: {name} {last_name} \n \n Role: {role}')
            progress_bar('Loading the information...Please Wait')
            
        switch_page("Classrooms")




