import pytest
from app.ECenter_Dashboard import app

"""
def test_valid_login():
   
    response = app.test_client().post('/login', data=dict(name='Zoya_74560021', password='Zoya0021'))
    assert response.status_code == 200
    #assert b"Thanks for logging in, patkennedy79@gmail.com!" in response.data
    #assert b"Welcome patkennedy79@gmail.com!" in response.data
    #assert b"Flask User Management" in response.data
    #assert b"Logout" in response.data
    #assert b"Login" not in response.data
    #assert b"Register" not in response.data
"""
"""   
def test_valid_logout():
    response = app.test_client().get('/')
    assert response.status_code == 200
    #assert b"Goodbye!" in response.data
    #assert b"Flask User Management" in response.data
    #assert b"Logout" not in response.data
    #assert b"Login" in response.data
    #assert b"Register" in response.data
"""
"""
def test_valid_register():
    response = app.test_client().post('/register', data=dict(name='Maya_74561021', password='Zoya0021'))
    #data=dict(name='Zoya_74560021', password='Zoya0021')
    assert response.status_code == 200
"""
def test_dashboard():
    response = app.test_client().get('/dashboard')
    assert response.status_code == 200

