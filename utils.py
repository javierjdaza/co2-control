
import pandas as pd
import streamlit as st
import time
import random
from datetime import datetime, timedelta



@st.cache_data
def authentication(user:str, password:str):
    response = False

    
    name = ''
    last_name = ''
    role = ''
    date_login = ''
    df = pd.read_json('auth.json', lines=True)
    df_dict = df.to_dict(orient='records')

    for dictionary in df_dict:

        if dictionary['user'] == user and dictionary['password'] == password:
            response = True
            name = dictionary['name'].title()
            last_name = dictionary['last_name'].title()
            role = dictionary['role'].title()
            date_login = dictionary['date_login'].title()

    return response, name,last_name,role,date_login
            
def side_bar_colored():
    page_bg_img = """
    <style>
    section[data-testid="stSidebar"] > div {

        padding-top: 90px;
    }
    </style>
    """
    st.markdown(page_bg_img,unsafe_allow_html=True)

@st.cache_data()
def create_dummy_date():

    aulas = ['aula 1','aula 2','aula 3','aula 4','aula 5','aula 6','aula 7','aula 8','aula 9']
    edificios = ['CAMILO TORRES', 'CAPRUIS Y FAVUIS','CENTIC','DANIEL CASAS','CENIVAM']


    dict_dummy = []
    start_date = datetime.strptime('31/12/2022', '%d/%m/%Y')
    for i in aulas:
        piso = 0
        n_aula = int(i.split(' ')[1] ) 
        if n_aula <=3:
            piso = 1
        elif n_aula >3 and n_aula <=6:
            piso = 2
        elif n_aula > 6 :
            piso = 3
        
        for dia in range(1,91):
            edificio = random.choice(edificios)
            dict_ = {
                'aula':i,
                'medicion': random.randint(400,1200),
                'datetime': start_date + timedelta(dia),
                'sensor' : f'{i}_sensor',
                'edificio' : edificio,
                'piso' : piso,
            }
            dict_dummy.append(dict_)
        df = pd.DataFrame(dict_dummy)
    return df
    # start_date = datetime.strptime('01/06/2022', '%d/%m/%Y')
    # end_date = datetime.strptime('20/02/2023', '%d/%m/%Y')
    # end_date - start_date


def progress_bar(title:str):
    progress_text = "Loading the information...Please Wait"
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(4):
        time.sleep(0.5)
        my_bar.progress(percent_complete + 25, text=progress_text)




def new_user(user,password,name,last_name,role,date_login):
    new_user_data = {
        'user' : user.lower(),
        'password' : password.title(),
        'name' : name.title(),
        'last_name' : last_name.title(),
        'role' : role.title(),
        'date_login' : date_login,
    }

    df_temp = pd.DataFrame([new_user_data])
    df = pd.read_json('auth.json', lines=True)
    if len(df[df['user'] == user]) == 0:
        df = pd.concat([df,df_temp])

        with open('auth.json', 'w') as f:
            f.write(df.to_json( orient='records', lines = True))
        return 'User created succesfully'
    else:
        return 'The user already exists'



