from werkzeug.security import check_password_hash
class User():
    
    # Constructor
    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
    

    # Comprueba si la password introducida para le usuario: password
    # es igual a la "haseada" (encriptada en la bbdd).

    # El decorador @classmethod permite usar un metod de clase, sin instanciarla. 
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

