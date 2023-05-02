from app import schemas
import pytest
from jose import jwt
from app.cofig import settings
# from .database import client,session



# def test_root(client):
#     res = client.get("/")
#     print( res.json().get('message'))
#     assert res.json().get('message') == 'Hello vamsi'
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/",json = {"email":"vamsi62@gmail.com", "password":"pass123"})
    print( res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "vamsi62@gmail.com"
    assert res.status_code == 201

def test_login_user(client,test_user):
    res = client.post("/login", data = {"username":test_user['email'], "password":test_user['password']})

    login_res = schemas.Token(**res.json())
    # print(login_res.json())
    payload = jwt.decode(login_res.access_token,settings.secret_key,algorithms=[settings.algorithm])
    # print(payload.get("user_email"))
    id : str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200   

@pytest.mark.parametrize("email , password , status_code",[('vamsi12@gmailcom','password123',403),('vamsi@gmailcom','password123',403),('vamsi@gmailcom','password23',403),( None,'password23',422),('vamsi@gmailcom',None,422)])

def test_incorrect_login(test_user,client,email,password,status_code):
    res = client.post("/login",data = {"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == 'invalid credentials'
