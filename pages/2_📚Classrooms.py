import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from utils import side_bar_colored,create_dummy_date
import time
from datetime import datetime
from streamlit_option_menu import option_menu
from db import get_user, authentication, change_password,create_new_user,fetch_all_users,delete_user,update_user
import plotly.express as px


side_bar_colored()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# =====================
# Session Manager
# =====================
# st.session_state['name'] = 'name'
# st.session_state['last_name'] = 'last_name'
# st.session_state['role'] = 'role'




# ===========================
# Authentication FAILED
if 'auth_' not in st.session_state or st.session_state['auth_'] == False:

    l1,l2,l3 = st.columns((1,0.5,1))
    col1_,col2_,col3_ = st.columns((1,2,1))

    with l2:
        st.image('./img/logo_1.png')
    with col2_:

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



# ===========================
# Authentication VALIDATED
# ===========================
elif st.session_state['auth_'] == True:
    # st.title('LOGO HERE')
    
    name = st.session_state['name']
    last_name = st.session_state['last_name']
    role = st.session_state['role']
    date_login = st.session_state['date_login']
    # =================================
    # NAME-LASTNAME | ROLE DISPLAY
    # =================================


    # ==================
    # NAVIGATION BAR
    # ==================

    # ------------------------
    # Administrator Role
    # ------------------------
    if role == 'Administrator':
        st.write(' ')
        st.write(' ')

        a1,a2,a3 = st.columns((1,10,1))
        with a2:
            l4,l5,l6 = st.columns((4,1,1))
            menu_selected = option_menu(menu_title= None, options=['Aulas','Gestion de Usuarios','Perfil','Monitoreo','Bases de Datos','Cerrar Sesion'], icons= ['bar-chart','people','person-circle','speedometer','box','door-closed'], orientation='horizontal',default_index=0)
            # with l1:
            #     st.success('CO2 Control')
                # st.image('./img/logo_1.png', width=140)
            with l4:
                st.info('CO2 Control')
            with l5:
                st.success(f'{name}', icon = '👤')
            with l6:
                st.warning(f'{role}', icon = '📍')
        

    # ------------------------
    # Other Role
    # ------------------------
    else:
        st.write(' ')
        st.write(' ')
        a1,a2,a3 = st.columns((1,10,1))
        with a2:
            l4,l5,l6 = st.columns((4,1,1))
            with l4:
                st.info('CO2 Control')
            with l5:
                st.success(f'{name}', icon = '👤')
            with l6:
                st.warning(f'{role}', icon = '📍')
            menu_selected = option_menu(menu_title= None, options=['Aulas','Perfil','Monitoreo','Cerrar Sesion'], icons= ['bar-chart','person-circle','speedometer','door-closed'], orientation='horizontal',default_index=0)



    # =====================
    # CLASSROOMS DISPLAY
    # =====================
    
    if menu_selected == 'Aulas':
        # st.title('Classrooms Realtime Information 📈')
        st.write('---')
        st.write('')
        st.write('')
        f1,f2,f3 = st.columns((1,10,1))
        df = create_dummy_date()
        with f2:
            
            aulas = df['aula'].unique()

            # =====================
            # Seleccionar edificio
            # =====================
            z1,z2,z3 = st.columns(3)
            with z1:
                edificio = st.selectbox(label='Seleccionar edificio:', options = df['edificio'].unique())
            with z2:
                piso = st.selectbox(label='Seleccionar piso:', options = df['piso'].unique())
            # for i in aulas:
            df_temp = df[(df['edificio'] == edificio) & (df['piso'] == piso)]
            df_temp.sort_values(by = ['datetime'], ascending = False, inplace =True)
            df_temp = df_temp.head()
            df_temp_dict = df_temp.to_dict(orient = 'records')
            options_list = []
            for i in df_temp_dict:

                aula = i['aula']
                medicion = i['medicion']
                datetime = i['datetime'].strftime('%d-%m-%Y')
                alerta = '🔴' 
                if medicion >=400 and medicion <= 799:
                    alerta = '🟢'
                elif medicion >=800 and medicion <=999:
                    alerta = '🟡'

                texto = f'{aula.title()} | Last Lecture: {datetime} | Co2 Levels: {medicion}ppm {alerta}'
                options_list.append(texto)

            class_selected = option_menu(menu_title= 'Informacion Aulas 📈', menu_icon = 'info-square-fill',options=options_list, orientation='vertical',default_index=0)

            st.caption('🔴 ppm: [1000,2000] ➖ 🟡 ppm: [800,999] ➖ 🟢 ppm: [400,799] ➖ ⚪ error de conexion')
            st.write('---')

            for i in options_list:
                if class_selected == i:
                    st.title('Dashboards 📊')
                    st.write('---')
                    aula_selected = i.split('|')[0].lower().strip()
                    df_temp_2 = df[(df['edificio'] == edificio) & (df['piso'] == piso) & (df['aula'] == f'{aula_selected}')]
                    # st.dataframe(df_temp_2, use_container_width=True)
                    fig = px.line(df_temp_2, x="datetime", y="medicion",  color='aula')
                    fig.update_layout(title_text=f'Line Plot CO2 Levels | {aula_selected.title()}', title_x=0.42,xaxis_title = 'Date',yaxis_title = 'Nivel de CO2',legend_title = 'Aula')
                    fig.add_hline(y=1000,line=dict(color="#EB4747"))
                    fig.add_hline(y=800,line=dict(color="#FFD966"))
                    st.plotly_chart(fig, use_container_width=True)
                    st.write('---')
                    k1,k2 = st.columns(2)
                    st.write('---')
                    with k1:
                        fig_2 = px.histogram(df_temp_2, x="medicion", nbins=20)
                        fig_2.update_layout(title_text=f'Histogram Plot CO2 Levels | {aula_selected.title()}', title_x=0.42,xaxis_title = 'Nivel de CO2',yaxis_title = 'Distribucion',legend_title = 'Aula')
                        st.plotly_chart(fig_2, use_container_width=True)
                    with k2:
                        fig_3 = px.bar(df_temp_2, x='datetime', y='medicion')
                        fig_3.update_layout(title_text=f'Bar Plot CO2 Levels | {aula_selected.title()}', title_x=0.42,xaxis_title = 'Date',yaxis_title = 'Nivel de CO2',legend_title = 'Aula')
                        fig_3.update_traces(marker_color='green')
                        st.plotly_chart(fig_3, use_container_width=True)
            
            st.markdown("<h3 style='text-align: center; color: #000000;'>Raw Data 📊</h3>", unsafe_allow_html=True)
            st.write(' ')
            st.dataframe(df_temp_2, use_container_width=True)
    # =====================
    #   # =====================
    elif menu_selected == 'Cerrar Sesion':
        st.title(' ')
        st.write('---')
        st.write(' ')
        st.write(' ')
        b1,b2,b3 = st.columns((1,4,1))
        # with a1:
        #     st.image('img/usuario.png')

        with b2:
            st.warning('Cerrando Sesion...')
            time.sleep(3)
        switch_page('authentication')
    

    # =====================
    # Perfil
    # =====================
    elif menu_selected == 'Perfil':
        st.write('---')
        st.write(' ')
        st.write(' ')
        a1,a2,a3 = st.columns((1,4,1))
        # with a1:
        #     st.image('img/usuario.png')

        with a2:
            name = st.session_state['name']
            last_name = st.session_state['last_name']
            role = st.session_state['role']
            with st.expander(f'Detalles Perfil', expanded=True):
                st.markdown("<h1 style='text-align: center; color: #000000;'>👤</h1>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center; color: #000000;'>{name} {last_name}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center; color: #000000;'>📍 {role}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center; color: #000000;'>🖌 User Since: {date_login}</h3>", unsafe_allow_html=True)
                st.write(' ')
            st.write('---')
                
            with st.expander('Cambiar Contraseña'):
                form_change_password = st.form('form change password')
                f1,f2,f3 = st.columns((1,2,1))
                with f2:
                
                    with form_change_password:
                        form_change_password.subheader('🔐')
                        form_change_password.write(' ')
                        user_input = form_change_password.radio( 'Nombre Usuario',[st.session_state['key']])
                        form_change_password.write(' ')
                        password_input = form_change_password.text_input('Contraseña actual',type='password', max_chars=15, key = 'password')
                        form_change_password.write(' ')
                        password_input_2 = form_change_password.text_input('Contraseña Nueva',type='password', max_chars=15, key = 'new_password')
                        form_change_password.write(' ')
                        submit = form_change_password.form_submit_button('Cambiar Contraseña',type = 'primary' )

                        if submit:
                            change_password_flag = change_password(user_name_input = user_input,password_input = password_input,new_password_input = password_input_2)

                            if change_password_flag == True:
                                st.success('La contraseña ha sido cambiada')
                            else:
                                st.error('No se ha cambiado la contraseña, verifica tus credenciales')

                            
    # =====================
    # Gestion de Usuarios
    # =====================
    elif menu_selected == 'Gestion de Usuarios':
        st.write('---')
        st.write('')
        st.write('')
        d1,d2,d3 = st.columns((1,3,1))
        with d2:

            with st.expander('👤 Agregar Usuario'):    
                placeholder_2 = st.empty()
                user_management_form = placeholder_2.form('User', clear_on_submit=True)
                with user_management_form:

                    user_management_form.subheader('👤')
                    user_management_form.write(' ')

                    user_nick_name = user_management_form.text_input('Nombre de Usuario')
                    user_management_form.write(' ')

                    user_name = user_management_form.text_input('Nombres')
                    user_management_form.write(' ')

                    user_last_name = user_management_form.text_input('Apellidos')
                    user_management_form.write(' ')

                    user_password = user_management_form.text_input('Contraseña',type='password', max_chars=15)
                    user_management_form.write(' ')

                    user_role = user_management_form.selectbox('Rol',('Administrator', 'Viewer'))

                        
                    user_date_registration = datetime.now().strftime('%d-%m-%Y')
                    create_new_user_button = user_management_form.form_submit_button('Agregar Usuario',type = 'primary')

                    if create_new_user_button:
                        flag_exists = create_new_user(user_name = user_nick_name,password = user_password,name = user_name,last_name = user_last_name,role = user_role)
                        if flag_exists == 'El usuario ya existe':
                            st.error(f'{flag_exists}',  icon='💀')

                        else:
                            st.success(f'{flag_exists}', icon='✅')

            with st.expander('❌ Borrar Usuario'):
                total_usuarios = fetch_all_users()
                df_total_usuarios = pd.DataFrame(total_usuarios)
                st.write(' ')
                st.subheader('Listado Total de Usuarios 👨‍💻')
                st.write(' ')
                st.dataframe(df_total_usuarios, use_container_width=True)
                listado_user_names = df_total_usuarios['key'].to_list()
                st.write('---')
                usuario_selected = st.selectbox('Selecciona el usuario a eliminar',options= listado_user_names)
                st.write(' ')
                st.write(' ')
                df_total_usuarios_filtred = df_total_usuarios[df_total_usuarios['key'] == usuario_selected]
                st.write('🧨 El siguiente usuario se eliminara: ')
                st.table(df_total_usuarios_filtred)
                st.write(' ')
                eliminar_button = st.button('Eliminar usuario', type='primary')
                if eliminar_button:
                    delete_flag = delete_user(usuario_selected)
                    if delete_flag:
                        st.success('El usuario ha sido eliminado')
                    else:
                        st.error('El usuario no se ha podido eliminar')

            with st.expander('🔄 Modificar Usuario'):
                total_usuarios = fetch_all_users()
                df_total_usuarios = pd.DataFrame(total_usuarios)
                st.write(' ')
                st.subheader('Listado Total de Usuarios 👨‍💻')
                st.write(' ')
                st.dataframe(df_total_usuarios, use_container_width=True)
                listado_user_names = df_total_usuarios['key'].to_list()
                st.write('---')
                usuario_selected = st.selectbox('Selecciona el usuario a modificar ',options= listado_user_names)
                st.write(' ')
                st.write(' ')
                st.write('✅ El siguiente usuario se modificara: ')
                st.write(' ')
                df_total_usuarios_filtred = df_total_usuarios[df_total_usuarios['key'] == usuario_selected]
                df_total_usuarios_filtred_dict = df_total_usuarios_filtred.to_dict(orient='records')
                form_cambiar_user_data = st.form('form change user')
                f1,f2,f3 = st.columns((1,2,1))
                with f2:
                
                    with form_cambiar_user_data:
                        usuario = df_total_usuarios_filtred_dict[0]['key']
                        usuario_name = df_total_usuarios_filtred_dict[0]['name']
                        usuario_last_name = df_total_usuarios_filtred_dict[0]['last_name']
                        usuario_password = df_total_usuarios_filtred_dict[0]['password']
                        usuario_role = df_total_usuarios_filtred_dict[0]['role']


                        form_cambiar_user_data.subheader('🔐')
                        form_cambiar_user_data.write(' ')
                        user_name_input = form_cambiar_user_data.text_input('Usuario',value = usuario)
                        form_cambiar_user_data.write(' ')
                        user_input_name = form_cambiar_user_data.text_input('Nombres', value = usuario_name)
                        form_cambiar_user_data.write(' ')
                        user_input_last_name = form_cambiar_user_data.text_input('Apellidos', value = usuario_last_name)
                        form_cambiar_user_data.write(' ')
                        password_input_cambiar = form_cambiar_user_data.text_input('Contraseña',type='password', max_chars=15,value=usuario_password)
                        form_cambiar_user_data.write(' ')
                        user_role_modificar = form_cambiar_user_data.selectbox('Roles',('Administrator', 'Viewer'), )
                        form_cambiar_user_data.write(' ')
                        submit_modificar = form_cambiar_user_data.form_submit_button('Modificar Usuario',type = 'primary' )

                        if submit_modificar:
                            flag_change = update_user(user_name = user_name_input,password = password_input_cambiar,name = user_input_name,last_name = user_input_last_name,role = user_role_modificar)
                        #     change_password_flag = change_password(user_name_input = user_input,password_input = password_input,new_password_input = password_input_2)

                            if flag_change == True:
                                st.success('Los datos del usuario han sido cambiados')
                            else:
                                st.error('No se han podido cambiar los datos del usuario')


                # if modificar_button:
                    # modify_flag = delete_user(usuario_selected)
                    # if modify_flag:
                    #     st.success('El usuario ha sido eliminado')
                    # else:
                    #     st.error('El usuario no se ha podido eliminar')

    # =====================
    # Monitoreo
    # =====================

    if menu_selected == 'Monitoreo':
        st.write('---')
        st.write(' ')
        st.write(' ')
        t1,t2,t3 = st.columns((1,4,1))

        with t2:
            st.title('Monitoreo 🧬')
    

    # =====================
    # Bases de datos
    # =====================

    if menu_selected == 'Bases de Datos':
        st.write('---')
        st.write(' ')
        st.write(' ')
        r1,r2,r3 = st.columns((1,4,1))

        with r2:
            items = fetch_all_users()
            df_users = pd.DataFrame(items)
            st.title('DB: Users 📋')
            st.write(' ')
            st.dataframe(df_users, use_container_width=True)
            st.write('---')
            st.title('DB: Aulas 📋')
            df_aulas = create_dummy_date()
            st.dataframe(df_aulas, use_container_width=True)
            st.write('---')
                     