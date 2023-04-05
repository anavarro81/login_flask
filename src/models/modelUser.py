from models.entities.User import User

class ModelUser():
    
    # Se usa el decorador: "classmethod" para poder usarlo sin instanciar la clase. 
    @classmethod
    def login(self, db, user):

        try:
        # Crea un cursor para operar sobre la base de datos
            cursor = db.connection.cursor()
        
        # Comprobamos si existe en el usuario introducido en la BBDD. 
        # Sentencia SQL a ejecutar. Selecciona todo para el usuario introducido.           
            sql =   """ SELECT id, username, password, fullname FROM users WHERE username='{}' """.format(user.username)

        # Se ejecuta el curso con la sentencia Sql generada.
            cursor.execute(sql)
        
        # Se lee del cursor una fila (row).  
        # Devuelve una tupla donde cada campo de la tabla devuelto es una posición. 
            row = cursor.fetchone()        

        # Se compruba si se han devueto datos o no (retorno = None).
        
        # Si hay datos, se devuelve l usuario encontrado. 
        
        # Comprobar clave usuario
        #    Mediante el método de clase check_password se comprueba si la introducida [user.password]
        #    es igual a la de la base de datos row[2]. 
            if row !=  None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user 
            else:
                return None 

                    
        except Exception as ex:
            raise Exception(ex)
    