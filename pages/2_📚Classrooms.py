import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from utils import side_bar_colored,button_customized,progress_bar,new_user
import hydralit_components as hc
import time
from datetime import datetime

side_bar_colored()

button_customized()


# =====================
# Session Manager
# =====================
# st.session_state['name'] = 'name'
# st.session_state['last_name'] = 'last_name'
# st.session_state['role'] = 'role'




# ===========================
# Authentication FAILED
# ===========================
if 'auth_' not in st.session_state or st.session_state['auth_'] == False:

    col1_,col2_,col3_ = st.columns((1,2,1))
    with col2_:
        l1,l2,l3 = st.columns((1,2,1))
        with l2:
            st.image('./img/logo_1.png')
        st.write('---')
        st.markdown("<h3 style='text-align: center; color: #000000;'>Classrooms Information 📊</h3>", unsafe_allow_html=True)
        st.write('---') 

        st.error('You need to Log in', icon = '💀')
        col1,col2,col3 = st.columns(3)
        with col2:
            go_to_login = st.button('go to login', type = 'primary')
    
    
    if go_to_login:
        switch_page('Authentication')


# ===========================
# Authentication VALIDATED
# ===========================
elif st.session_state['auth_'] == True:
    # st.title('LOGO HERE')
    st.image('./img/logo_1.png')
    name = st.session_state['name']
    last_name = st.session_state['last_name']
    role = st.session_state['role']
    date_login = st.session_state['date_login']
    # =================================
    # NAME-LASTNAME | ROLE DISPLAY
    # =================================
    l1,l2,l3,l4,l5 = st.columns((1,1,1,1,0.6))
    with l4:
        st.info(f'{name} {last_name}', icon = '👤')
    with l5:
        st.info(f'{role}', icon = '📍')

    # ==================
    # NAVIGATION BAR
    # ==================

    # ------------------------
    # Administrator Role
    # ------------------------
    if role == 'Administrator':
        menu_data = [
                {'icon': "👨‍🎓", 'label':"User Management",'ttip':"View all users management!"},#no tooltip message
                {'icon': "➕", 'label':"Add Classroom",'ttip':"Add Classrooms!"}, #can add a tooltip message
                {'icon': "👤", 'label':"Profile",'ttip':"Profile Settings"}, #can add a tooltip message
                {'icon': "👨‍💻", 'label':"About",'ttip':"The Team!"}, #can add a tooltip message
                {'icon': "🏠", 'label':"Home",'ttip':"Go to Home!"}, #can add a tooltip message
        ]
        # we can override any part of the primary colors of the menu

        over_theme = {'txc_inactive': '#FFFFFF'}
        menu_id = hc.nav_bar(menu_definition = menu_data, home_name = 'Classrooms', override_theme = over_theme)

    # ------------------------
    # Other Role
    # ------------------------
    else:
        menu_data = [
                {'icon': "👤", 'label':"Profile",'ttip':"Profile Settings"}, #can add a tooltip message
                {'icon': "👨‍💻", 'label':"About",'ttip':"The Team!"}, #can add a tooltip message
                {'icon': "🏠", 'label':"Home",'ttip':"Go to Home!"}, #can add a tooltip message
        ]
        # we can override any part of the primary colors of the menu

        over_theme = {'txc_inactive': '#FFFFFF'}
        menu_id = hc.nav_bar(menu_definition = menu_data, home_name = 'Classrooms', override_theme = over_theme)

    #get the id of the menu item clicked
    # st.info(f"{menu_id=}")
    # st.write(st.session_state)


    # =====================
    # CLASSROOMS DISPLAY
    # =====================
    def new_row_classroom(aula:str, hour_last_lecture:str, date_last_lecture:str, value=int,delta = int):
        c1,c2, = st.columns((4,1))
        if value >500:
            with c1:
                st.button(f'{aula} | Ultima lectura: {hour_last_lecture} {date_last_lecture}')
            
            with c2:
                st.metric(label=f"CO2 Levels 🚨🚨", value=f"{value} ppm", delta=f"{delta} ppm")
        else:
            with c1:
                st.button(f'{aula} | Ultima lectura: {hour_last_lecture} {date_last_lecture}')
            
            with c2:
                st.metric(label=f"CO2 Levels", value=f"{value} ppm", delta=f"{delta} ppm")

        st.write('---')
    


    if menu_id == 'Classrooms':
        st.title('Classrooms Realtime Information 📈')
        st.write('---')
        st.write('')
        st.write('')
        new_row_classroom(aula='AULA 1', hour_last_lecture='10:10 am', date_last_lecture = '23/01/2023',value= 520, delta=-10)
        new_row_classroom(aula='AULA 2', hour_last_lecture='12:50 am', date_last_lecture = '23/01/2023',value= 720, delta=20)
        new_row_classroom(aula='AULA 3', hour_last_lecture='15:70 am', date_last_lecture = '23/01/2023',value= 470, delta=-50)
        new_row_classroom(aula='AULA 4', hour_last_lecture='17:30 am', date_last_lecture = '23/01/2023',value= 560, delta=40)

        st.caption('The records with the symbol 🚨🚨, means levels of CO2 above 500 ppm')
    # =====================
    # HOME
    # =====================
    elif menu_id == 'Home':
        st.title(' ')
        switch_page('Home')
    

    # =====================
    # PROFILE
    # =====================
    elif menu_id == 'Profile':
        st.write('---')
        st.write(' ')
        st.write(' ')
        a1,a2,a3 = st.columns((0.3,1,1))
        with a1:
            st.image('img/usuario.png')

        with a2:
            name = st.session_state['name']
            last_name = st.session_state['last_name']
            role = st.session_state['role']
            # st.title('👤')
            # st.markdown("<h1 style='text-align: center; color: #000000;'>👤</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: left; color: #000000;'>👤 | {name} {last_name}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: left; color: #000000;'>📍 | {role}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: left; color: #000000;'>🖌 | User Since: {date_login}</h3>", unsafe_allow_html=True)
            st.write(' ')
            st.write(' ')
            change_password = st.button('Change Password', type='primary')
            if change_password:
                st.warning('TODO')

    # =====================
    # User Management
    # =====================
    elif menu_id == 'User Management':
        st.title('User Management 👨‍🎓')
        st.write('---')
        st.write(' ')
        st.write(' ')

        d1,d2,d3 = st.columns(3)
        with d2:
            placeholder_2 = st.empty()
            user_management_form = placeholder_2.form('User', clear_on_submit=True)
            with user_management_form:

                user_management_form.subheader('Add New User 👤')
                user_management_form.write(' ')

                user_nick_name = user_management_form.text_input('User Name')
                user_management_form.write(' ')

                user_name = user_management_form.text_input('Name')
                user_management_form.write(' ')

                user_last_name = user_management_form.text_input('Last Name')
                user_management_form.write(' ')

                user_password = user_management_form.text_input('Password',type='password', max_chars=15)
                user_management_form.write(' ')

                user_role = user_management_form.selectbox('Role',('Administrator', 'Viewer'))

                    
                user_date_registration = datetime.now().strftime('%d-%m-%Y')
                create_new_user_button = user_management_form.form_submit_button('Sign Up',type = 'primary')

                if create_new_user_button:
                    flag_exists = new_user(user = user_nick_name,password = user_password,name = user_name,last_name = user_last_name,role = user_role,date_login = user_date_registration)
                    if flag_exists == 'The user already exists':
                        st.error(f'{flag_exists}',  icon='💀')
                        del st.session_state['user_name']

                    else:
                        st.success(f'{flag_exists}', icon='✅')

    # =====================
    # User Management
    # =====================

    elif menu_id =='Add Classroom':
        st.title('Add Classroom ➕')
        st.write('---')
        st.write(' ')
        st.write(' ')
        e1,e2,e3 = st.columns(3)
        with e2:
            placeholder_3 = st.empty()
            add_classroom_form = placeholder_3.form('User', clear_on_submit=True)
            with add_classroom_form:

                add_classroom_form.subheader('Classroom Info 🗄')
                add_classroom_form.write(' ')

                classroom_id = add_classroom_form.text_input('Classroom Id')
                add_classroom_form.write(' ')


                classroom_sensor = add_classroom_form.text_input('Sensor')
                add_classroom_form.write(' ')

                broker_classroom = add_classroom_form.text_input('Broker')
                add_classroom_form.write(' ')

                capacity_classroom = add_classroom_form.text_input('Capacity')
                add_classroom_form.write(' ')

                classroom_date_registration = datetime.now().strftime('%d-%m-%Y')
                    
                create_new_classroom_button = add_classroom_form.form_submit_button('Add Classroom',type = 'primary')

                if create_new_classroom_button:
                        st.warning(f'TODO: Connect to Sensor API',  icon='📐')

    # =====================
    # About
    # =====================
    elif menu_id == 'About':
        st.title('About 👨‍💻')
        st.write('---')
        st.write('')
        st.write('')

        a1,a2,a3 = st.columns((1,1,2))
        with a1:
            st.image('img/ivan.jpeg',)
            st.markdown("<h5 style='text-align: center; color: #434242;'>Ivan Daniel Maestre Muza <br> Software Engineer <br> Universidad Industrial de Santander</h7>", unsafe_allow_html=True)
        with a2:
            st.image('img/eladio.jpeg',)
            st.markdown("<h5 style='text-align: center; color: #434242;'>Eladio Carrion Morales <br> Industrial Engineer <br> Universidad Industrial de Socorro</h7>", unsafe_allow_html=True)