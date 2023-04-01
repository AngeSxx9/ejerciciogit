intentos = 0

def Login(usuario, contrasena):
    global intentos
    if usuario == "admin" and contrasena == "admin123*":
        intentos = 0
        return True
    else:
        intentos += 1
        return False

# Pedir al usuario que ingrese su nombre de usuario y contraseña
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Verificar las credenciales ingresadas
while not Login(usuario, contrasena):
    print("Nombre de usuario o contraseña incorrectos.")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    Login(usuario, contrasena) # Llamar a la función Login nuevamente para actualizar los intentos

# Si las credenciales son correctas, mostrar un mensaje de bienvenida
print("Bienvenido, ", usuario)

# Mostrar el número de intentos realizados
if intentos > 0:
    print("Número de intentos: ", intentos)
