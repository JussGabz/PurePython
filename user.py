import bcrypt

class User:
    """
    Class for Creating Users
    """
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def hash_password(self):
        password = bytes(self.password, encoding='utf8')
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password, salt)

        print("Password: ", hash_password)
        return hash_password


    