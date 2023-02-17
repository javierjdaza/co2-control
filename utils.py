
import pandas as pd
import streamlit as st
import time

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

    [data-testid="stSidebar"]{
        background-color:#486EDB;
        color: white;
    }
    .css-17lntkn{
        color: white;
    }

    section[data-testid="stSidebar"] > div {

        padding-top: 90px;



    }
    </style>
    """
    st.markdown(page_bg_img,unsafe_allow_html=True)

def button_customized():
    page_button = """
    <style>

    button[kind="secondary"]{

        padding: 2em 25em 2em 25em;
        background: #efefef;
        border: none;
        border-radius: .5rem;
        color: #444;
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: .1rem;
        text-align: center;
        outline: none;
        cursor: pointer;
        transition: .2s ease-in-out;
        box-shadow: -6px -6px 14px rgba(255, 255, 255, .7),
                    -6px -6px 10px rgba(255, 255, 255, .5),
                    6px 6px 8px rgba(255, 255, 255, .075),
                    6px 6px 10px rgba(0, 0, 0, .15);
    }
    button[kind="secondary"]:hover{

        box-shadow: -2px -2px 6px rgba(255, 255, 255, .6),
              -2px -2px 4px rgba(255, 255, 255, .4),
              2px 2px 2px rgba(255, 255, 255, .05),
              2px 2px 4px rgba(0, 0, 0, .1);
    }
    </style>
    """
    st.markdown(page_button,unsafe_allow_html=True)

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



