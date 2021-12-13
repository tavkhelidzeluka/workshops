from os import stat
from settings import BASE_DIR, DB_PATH
import json



class Cryptography:
    @staticmethod
    def hash(char: str) -> str:
        if char == 'Z' or char == 'z':
            return chr(ord(char) - 25) # a - A, 122 - 25 ->  97 , 90 - 25 -> 65
        return chr(ord(char) + 1) # a 97 + 1 -> 98

    @staticmethod
    def dehash(char: str) -> str:
        if char == 'a' or char == 'A':
            return chr(ord(char) + 25)
        return chr(ord(char) - 1)

    @staticmethod
    def make_hash(hashable: str) -> str:
        """
            A - Z ->  65 - 90
            a - z ->  91 - 122
        """
        if not isinstance(hashable, str):
            print('hashable must be a string!')
            return
        
        hashed_chars: list[str] = [] # a , v, v,b ,we

        for char in hashable:
            # ord აბრუნებს ASCII კოდს
            char_ascii = ord(char)
            if not (ord('a') <= char_ascii and char_ascii <= ord('z')) and not (ord('A') <= char_ascii and char_ascii <= ord('Z')):
                print('hashable must contain only letters [a-z and A-Z]')
                return

            hashed_chars.append(Cryptography.hash(char))
        return ''.join(hashed_chars) # ['a', 'b'] -> ab

    @staticmethod
    def read_hash(hashed: str) -> str:
        dehashed_chars: list[str] = []

        for char in hashed:
            dehashed_chars.append(Cryptography.dehash(char))
        
        return ''.join(dehashed_chars)

class User:
    def __init__(self, username: str) -> None:
        # constructor
        self.username = username
    
    @staticmethod
    def validate(username, password) -> 'User':
        users = json.load(open(DB_PATH))
        user_obj = {
            "username": username,
            "password": Cryptography.make_hash(password)
        }

        if user_obj not in users:
            raise Exception('User does not exists!')

        return User(username)

    @staticmethod
    def create(username, password) -> 'User':
        users = json.load(open(DB_PATH))
        hashed_password = Cryptography.make_hash(password)
        users.append({
            "username": username,
            "password": hashed_password
        })
        print(users)

        json.dump(users, open(DB_PATH, 'w+'), indent=4)

        return User(username, hashed_password)
    

    def __str__(self) -> str:
        return self.username
