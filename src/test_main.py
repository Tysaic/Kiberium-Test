from fastapi.testclient import TestClient
from main import app


client = TestClient(app)
#EXISTING HOME
def test_existing_id():
    response = client.get('/v1/api/patent/id/12')
    assert response.status_code == 200
    assert response.json() == {"patent": "AAAA011"}

def test_positive_id():
    response = client.get('/v1/api/patent/id/-32423')
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "ensure this value is greater than 0"

def test_doesnt_exists_id():
    response = client.get('/v1/api/patent/id/9999999999')
    assert response.status_code == 422
    assert response.json()["detail"]["alert"] == "ID doesn't exists"

def test_string_as_id():

    response = client.get('/v1/api/patent/id/sjadaws')
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"

def test_float_as_id():

    response = client.get('/v1/api/patent/id/7.0')
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"

def test_existing_patent():

    response = client.get('/v1/api/patent/number/AAAA099')
    assert response.status_code == 200
    assert response.json() == {"id": 100}

def test_greater_len_patent():

    response = client.get('/v1/api/patent/number/001aaZZ')
    assert response.status_code == 422
    assert response.json()["detail"]["error"] == "The patent number must be type as: AAAA000 4 letters and 3 digits"

def test_doesnt_exists_patent():

    response = client.get('/v1/api/patent/number/ZZZZ999')
    assert response.status_code == 422
    assert response.json()["detail"]["alert"] == "The patent doesn't exists"

def test_regex_patent():

    response = client.get('/v1/api/patent/number/AAA0001')
    assert response.status_code == 422
    assert response.json()["detail"]["error"] == "The patent number must be type as: AAAA000 4 letters and 3 digits"
