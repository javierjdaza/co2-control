from deta import Deta
from datetime import datetime


DETA_KEY = 'e0jeqtjtszl_L996atb2Q4i8HKS36bU6drgU6tt1HYSq' 

# Initialize with a project key
deta = Deta(DETA_KEY)


# This is how to create/connect a database
db = deta.Base("users")


def create_new_user(user_name,password,name,last_name,role):
    # create new user
    user_fetched = get_user(user_name)
    if user_fetched is None:
        date_login = datetime.now().strftime('%d-%m-%Y')
        db.put({"key":user_name, "password":password, "name":name.title(), 
        "last_name": last_name.title(),"role": role.title(),"date_login":date_login})
        return 'El usuario ha sido creado con exito'
    else:
        return 'El usuario ya existe'

def fetch_all_users():
    """Returns a dict of all users"""
    res = db.fetch()
    return res.items


def get_user(user_name:str):
    return db.get(user_name)

def fetch_all_co2_data():
    db = deta.Base("data_co2")
    res = db.fetch()
    all_items = res.items

    while res.last:
        res = db.fetch(last=res.last)
        all_items += res.items
    return all_items

def authentication(user_name_input:str, password_input):
    user_fetched = get_user(user_name_input)
    password_fetched = user_fetched['password']
    if user_fetched is not None and password_fetched == password_input:

        password = user_fetched['password']
        name = user_fetched['name']
        last_name = user_fetched['last_name']
        role = user_fetched['role']
        date_login = user_fetched['date_login']
        user_name = user_fetched['key']
        auth_flag = True
        return auth_flag,password,name,last_name,role,date_login,user_name
    else:
        password = ''
        name = ''
        last_name = ''
        role = ''
        date_login = ''
        auth_flag = False
        user_name = ''
        return auth_flag,password,name,last_name,role,date_login,user_name


def change_password(user_name_input,password_input,new_password_input:str):
    user_fetched = get_user(user_name_input)
    if user_fetched is not None:
        user_dict = db.get(user_name_input)
        if user_dict['password'] == password_input:
            try:
                db.update({"password":new_password_input},key=user_name_input)
                return True
            except Exception as e:
                print(e)
                return False
    else:
        return False


def delete_user(user_name):
    try:
        db.delete(user_name)
        return True
    except Exception as e:
        print(e)
        return False



def update_user(user_name,password,name,last_name,role):
    try:
        db.update({"password":password, "name":name.title().strip(), "last_name": last_name.title().strip(),"role": role.title().strip()}, key = user_name)
        return True
    except Exception as e:
        print(e)
        return False