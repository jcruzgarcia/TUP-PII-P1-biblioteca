from datetime import *
from abc import *
import random, re
x = date.today()

class Persona(ABC):
    def __init__(self, _nombre: str, _apellido: str, _fecha_nacimiento: date, _edad: int, _nro_documento: int) -> None:
        self._nombre = _nombre
        self._apellido = _apellido
        self._fecha_nacimiento = _fecha_nacimiento
        self._edad = _edad
        self._nro_documento = _nro_documento
    @property
    def get_nombre(self):
        return self._nombre
    @property
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre de debe ser una cadena de texto")
    
    @property
    def get_apellido(self):
        return self._apellido
    @property
    def set_apellido(self, nuevo_apellido):
        if isinstance(nuevo_apellido, str):
            self._apellido = nuevo_apellido
        else:
            raise ValueError("El apellido de debe ser una cadena de texto")
    
    @property
    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento
    @property
    def set_fecha_nacimiento(self, nuevo_fecha_nacimiento):
        if isinstance(nuevo_fecha_nacimiento, date):
            self._fecha_nacimiento = nuevo_fecha_nacimiento
        else:
            raise ValueError("La fecha de nacimiento debe ser del tipo date")
    
    @property
    def get_edad(self):
        return self._edad
    @property
    def set_edad(self, nuevo_edad):
        if isinstance(nuevo_edad, int):
            self._edad = nuevo_edad
        else:
            raise ValueError("La edad debe ser del tipo entero")
    
    @property
    def get_nro_documento(self):
        return self._nro_documento
    @property
    def set_nro_documento(self, nuevo_nro_documento):
        if isinstance(nuevo_nro_documento, int):
            self._nro_documento = nuevo_nro_documento
        else:
            raise ValueError("El numero de documento debe ser del tipo entero")
    
class Usuario(Persona):
    user_registry = []
    
    def __init__(self, __user_name: str, __estado: bool,__adminitrador: bool, __email: str, __password: str, _nombre: str, _apellido: str, __fecha_alta: date, __fecha_baja: date) -> None:
        super().__init__(_nombre, _apellido)
        self.__user_name = __user_name #----------------------hacer {unique}
        self.__estado = True
        self.__administrador = False
        self.__email = __email
        self.__password = __password
        self.__fecha_alta = datetime.now()
        self.__fecha_baja = __fecha_baja
        
        
    @property #read-only
    def get_user_name(self):
        return self.__user_name
    
    @property
    def get_estado(self):
        return self.__estado
    @property
    def set_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, bool):
            self.__estado = nuevo_estado
        else:
            raise ValueError("El nombre de debe ser un valor booleano (true/false)")
    
    @property
    def get_administrador(self):
        return self.__administrador
    @property
    def set_administrador(self, nuevo_administrador):
        if isinstance(nuevo_administrador, bool):
            self.__administrador = nuevo_administrador
        else:
            raise ValueError("El estado del administrador debe ser un booleano")
        
    @property
    def get_email(self):
        return self.__email
    @property
    def set_email(self, nuevo_email):
        if isinstance(nuevo_email, str):
            self.__email = nuevo_email
        else:
            raise ValueError("El email de debe ser una cadena de texto")
    
    @property
    def get_password(self):
        return self.__password
    @property
    def set_password(self, nuevo_password):
        if isinstance(nuevo_password, str):
            self.__password = nuevo_password
        else:
            raise ValueError("El nombre de debe ser una cadena de texto")
        
    @property
    def get_fecha_alta(self): #read-only
        return self.__fecha_alta
    
    @property
    def get_fecha_baja(self):
        return self.__fecha_baja
    @property
    def set_fecha_baja(self, nuevo_fecha_baja):
        if isinstance(nuevo_fecha_baja, date):
            self.__fecha_baja = nuevo_fecha_baja
        else:
            raise ValueError("La fecha de baja debe ser de tipo date")
        
    def __str__(self) -> str:
        
        return f"""
                    Usuario: {self.__user_name}\n
                    Estado: {self.__estado}\n
                    Email: {self.__email}\n
                    Contraseña: {self.__password}\n
                    Nombre {self._nombre}\n
                    Apellido: {self._apellido}\n
                    Fecha de alta: {self.__fecha_alta}\n
                    Fecha de baja: {self.__fecha_baja}\n"""
    #--------------METHODS--------------#
                    
    def validar_credenciales(self) -> bool:
        if user_name_input == self.__user_name:
            print("El usuario coincide")
            if contrasenia == self.__password:
                print("La contraseña coincide")
                return True
            else:
                print("la contraseña NO coincide")
                return False
        else:
            print("usuario NO COINCIDE")
            return False
            
    def baja_usuario(self) -> None:
        self.__estado = False
        self.__fecha_baja = datetime.now()
    
    def leyo_libro(self) -> bool:
        pass
    def agregar_libro(self) -> None:
        pass
    def quitar_libro(self) -> None:
        pass
    
    
class TipoDocumento():
    def __init__(self, __tipo_documento: str) -> None:
        self.__tipo_documento = __tipo_documento
    
    @property
    def get_tipo_documento(self): #read-only
        

        return self.__tipo_documento

class Libro():
    isbn_registry = []
    
    def __init__(self, __nombre: str, __autor: str, __fecha_lanzamiento: date, __isbn: str) -> None:
        self.__nombre = __nombre
        self.__autor = __autor
        self.__fecha_lanzamiento = __fecha_lanzamiento

        if __isbn is not None: #---------------------------------------------------------------aplicar lo mismo para user_name en clase Usuario?
            if __isbn in Libro.isbn_registry:
                raise ValueError("El ISBN ingresado ya está en uso.")
            self.__isbn = __isbn
            Libro.isbn_registry.add(__isbn)
        else:
            self.__isbn = self.generar_ISBN()
        
    @property
    def get_nombre(self):
        return self.__nombre
    @property
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre de debe ser una cadena de texto")
    
    @property
    def get_autor(self):
        return self.__autor
    @property
    def set_autor(self, nuevo_autor):
        if isinstance(nuevo_autor, str):
            self._autor = nuevo_autor
        else:
            raise ValueError("El autor de debe ser una cadena de texto")
    
    @property
    def get_fecha_lanzamiento(self):
        return self.__fecha_lanzamiento
    @property
    def set_fecha_lanzamiento(self, nuevo_fecha_lanzamiento):
        if isinstance(nuevo_fecha_lanzamiento, str):
            self.__fecha_lanzamiento = nuevo_fecha_lanzamiento
        else:
            raise ValueError("La fecha de lanzamiento debe ser del tipo date")
    
    @property
    def get_isbn(self):
        return self.__isbn
    @property
    def set_isbn(self, nuevo_isbn):
        if isinstance(nuevo_isbn, str):
            self.__isbn = nuevo_isbn
        else:
            raise ValueError("El nombre de debe ser una cadena de texto")
            
    def generar_IBSN(self) -> str:
        isbn = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        while isbn in Libro.isbn_registry:
            isbn =  isbn = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        Libro.isbn_registry.add(isbn)
        return isbn
    
