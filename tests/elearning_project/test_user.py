import pytest
from rest_framework.test import APIClient

client=APIClient()
@pytest.mark.django_db
def test_register_user():
    
    payload=dict(
        
        username = "jaidhanush",
        password= "12Jai@345",
        password2= "12Jai@345",
        email= "jaidhanushdj@gmail.com",
        first_name= "jai",
        last_name= "kumar"
    )
    
    response=client.post('/api/user/register',payload)
    data=response.data
    assert data['status']==201
    assert data['message']=='User added successfully'