from main import get_weatherdata, add, devide, UserManager, is_parameter
import pytest
import requests
import json

# API testing
def get_weather(incity):
    resp = requests.get(f"https://api.weather.com/v1/{incity}")
    if resp.status_code == 200:
        return resp.json()
    else:
        raise ValueError("Cannot get weather data for the selected city")

# API testing v2
# test_valid_post_register
#    call: https://reqres.in/api/registe
# test_valid_post_logging
#     call: https://reqres.in/api/login
# test_valid_get_users
#     call: https://reqres.in/api/users?page=2
# test_valid_get_user
#     call: https://reqres.in/api/users/2
def get_url():
    return "https://reqres.in"
def test_valid_post_register():
    lurl = get_url() + "/api/register"
    data = { 'email': 'eve.holt@reqres.in', 'password': 'pistol' }
    response = requests.post(lurl,data=data)
    lt = json.loads(response.text)
    assert response.status_code == 200
    assert lt["id"] == "4"
    assert lt["token"] == "QpwL5tke4Pnpja7X4"
def test_valid_post_logging():
    lurl = get_url() + "/api/login"
    data = { 'email': 'eve.holt@reqres.in', 'password': 'cityslicka' }
    response = requests.post(lurl,data=data)
    lt = json.loads(response.text)
    assert response.status_code == 200
    assert lt["token"] == "QpwL5tke4Pnpja7X4"
def test_valid_get_users():
    lurl = get_url() + "/api/users?page=2"
    response = requests.get(lurl)
    lt = json.loads(response.text)
    assert response.status_code == 200
    assert lt["per_page"] == 6
    assert lt["total"] == 12
def test_valid_get_user():
    lurl = get_url() + "/api/users/2"
    response = requests.get(lurl)
    lt = json.loads(response.text)
    assert response.status_code == 200
    assert lt["data"]["id"] == 2
    assert lt["data"]["email"] == "janet.weaver@reqres.in"
    assert lt["support"]["url"] == "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral"

@pytest.mark.parametrize("num, expected", [(1,False),(2,True),(3,True),(4,True),(17,True),(18,False),(19,True),(25,True),])
def test_is_parameter(num,expected):
    assert is_parameter(num) == expected

@pytest.fixture
def user_manager():
    # Craete an UserManager instance
    return UserManager()
def test_add_user(user_manager):
    assert user_manager.add_user("New_User", "newuser@mail.com") == True
    assert user_manager.get_user("New_User") == "newuser@mail.com"
def test_add_duplicate_user(user_manager):
    user_manager.add_user("New_User", "newuser@mail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("New_User", "newuser@mail.com")

def test_get_weatherdata():
    assert get_weatherdata(21) == "hot"
    assert get_weatherdata(35) == "hot"
    assert get_weatherdata(12) == "cold"

def test_add():
    assert add(2,3) == 5, "2 + 3 should be 5"
    assert add(-1,1) == 0, "-1 + 1 should be 0"
    assert add(0,0) == 0, "0 + 0 should be 0"

def test_devide():
    with pytest.raises(ValueError, match="Cannot devide by zero"):
        devide(10,0)


