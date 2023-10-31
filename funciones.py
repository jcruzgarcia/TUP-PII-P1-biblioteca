from clases import Usuario, TipoDocumento
from datetime import *
import re

def validar_contrasenia(contrasenia):
    # Verifica que la contraseña tenga entre 8 y 10 caracteres y al menos un dígito
    return re.match(r"^(?=.*\d).{8,10}$", contrasenia)


def registrar_usuario():
    print("REGISTRAR USUARIO")
#-username
    email = str(input("Ingresa tu correo electrónico: "))
    while True:
        user_name_input =  str(input("Ingresa tu nombre de usuario: "))
        for u in Usuario.user_registry:
            if user_name_input in u.get_user_name():
                print("El usuario ya existe")
            else:
                print("Nombre de usuario disponible.")
                break
        break        
    fecha_alta= datetime.now()
    estado = True
    
    es_administrador = input("¿El usuario es administrador? \n 1. Sí 9\n 2. No")
    if es_administrador == 1:
        es_administrador = True
    elif es_administrador == 2:
        es_administrador = False

#-password
    while True:
        contrasenia = str(input("Ingrese una contraseña (debe ser entre 8 y 10 caracteres y tener al menos un caracter numérico): "))
        contrasenia_verification = str(input("Ingrese nuevamente su contraseña: "))
        if contrasenia != contrasenia_verification:
            print("Las contraseñas no coinciden, intente nuevamente)")
        else:
            if validar_contrasenia(contrasenia):
                print("Registro exitoso")
            else:
                print("La contraseña no cumple con los requisitos \n Debe tener entre 8 y 10 caracteres y al menos 1 caracter numérico")
        break
    
    usuario = Usuario(user_name_input,estado,es_administrador,email, contrasenia, None, None, fecha_alta,None)
    Usuario.user_registry.append(usuario)
#-resto de datos
    nombre_input = str(input("Ingresa tu nombre:"))
    usuario.set_nombre(nombre_input)
    
    apellido_input = str(input("Ingresa tu apellido:"))
    usuario.set_apellido(apellido_input)
    
    fecha_nacimiento_input = input("Ingresa tu fecha de nacimiento con el siguiente formato: YYYY-MM-DD: \n")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_input, "%Y-%m-%d")
    usuario.set_fecha_nacimiento(fecha_nacimiento)
    
    edad_input = int(input("Ingrese su edad: "))
    usuario.set_edad(edad_input)
    
    nro_documento_input = int(input(f"Ingrese el numero correspondiente a su {TipoDocumento.get_tipo_documento}:  "))
    usuario.set_nro_documento(nro_documento_input)
    