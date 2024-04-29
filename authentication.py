from flask import session
from dotenv import load_dotenv, dotenv_values
import os

class Authentication:
    def __init__(self) -> None:
        load_dotenv()
        self.email = os.getenv("EMAIL") 
        self.password = os.getenv("PASSWORD")

    def login(self, credentials):
        if self.email == credentials['email'] and \
            self.password == credentials['password']:
            
            session['email'] = credentials['email']
            
            return True
        return False

    @property
    def is_loggedin(self):
        return session.get('email') is not None
    

    def logout(self):
        session.pop("email")