import bcrypt
from user import User

new_user = User(
    first_name="Gabriel", last_name="Ifesanya", username="JussGabz", email="gabriel@hotmail.com", password="Gabriel123")

def test_get_first_name():
    assert new_user.get_first_name() == "Gabriel"

def test_get_last_name():
    assert new_user.get_last_name() == "Ifesanya"

def test_hash_password():
    hashed_password = new_user.hash_password()
    password = new_user.password.encode('utf-8')
    is_matched = bcrypt.checkpw(password, hashed_password)

    assert is_matched