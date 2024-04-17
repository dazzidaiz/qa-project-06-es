# Pruebas de como la aplicacion "Urban Grocers" crea kits de productos

- Se han creado varias lisas de comprobacion, una de ellas es para capo name al crear un kit de productos
-Tu tarea es:
     --automatizar las pruebas desde la lista de comprobacion,
     --Cargar el codigo en GitHub,
     --Enviar el repositorio a revision

# Cofiguracion

     ..Paso 1: Conecta con tu GitHub
--El primer paso es enlazar tu cuenta de GitHub a TripleTen. 
--Para ello, haz clic en el botón "Enlazar la cuenta de GitHub" en el widget en la parte superior de  la pagina de TripleTen,
Esto te llevará a una nueva pestaña del navegador donde se te pedirá que confirmes que deseas enlazar tu cuenta de GitHub. 
Si aún no has iniciado sesión en GitHub, se te pedirá que introduzcas tu nombre de usuario y contraseña.
Al confirmarlo, tu perfil de TripleTen se conectará a tu perfil de GitHub a través de la API segura de GitHub.
 Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.
     
     ..Paso 2. Clona el repositorio en tu computadora
-Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-06.

-Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:
     cd ~               # asegúrate de estar en tu directorio de inicio
     mkdir projects     # crea una carpeta llamada projects
     cd projects        # cambia el directorio a la nueva carpeta de proyectos

-Clona el repositorio con SSH  
     git clone git@github.com:username/qa-project-06.git  

-Puedes utilizar PyCharm para trabajar en el proyecto localmente. 
--Simplemente abre PyCharm y selecciona Archivo → Abrir y luego selecciona la carpeta qa-project-06 que clonaste en tu computadora. 
--En la aplicacion Pycharm se crearon automaticamente los bancos:
     -configuration.py        # URL  rutas de la solicitud
     -data.py                 # Datos de la solicitud
     -seder_stand_request.py  # Envio de las solicitudes
     -post_new_client_kit     # Pruebas
     -ready.md                # Descripcion del proyecto
     -.gitignore              # Bancos innecesarios
      
# Inicia el servidor de "Urban Grocers" para obtener la URL de tu servidor
     URL (https://cnt-ea0cdf02-1895-47a4-87b9-c80e2499da7a.containerhub.tripleten-services.com)
          NOTA SOBRE URL: cada que se inicia el servidor la URL cambia 

--Abre la documentación para estudiar la API de la aplicación de Urban Grocers: <the url of the launched server>/docs/.
--Busca "Main.Kits" →" Crear un kit.”
--Antes de comenzar a trabajar tu proyecto, lee cuidadosamente esta lección. # Creación de un kit para el usuario o usuaria

# Creación de un kit para el usuario o usuaria
Vas a crear un kit dentro de un usuario o usuaria. Para ello, sigue estos pasos:
     --import configuration.py, data.py y la libreria requests de Pycharm con el comando import al banco sender_stand_request.py
     --import configuration
     --import requests
     --import data

..Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).CREATE_USER_PATH = "/api/v1/users/"

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)

..Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.KITS_PATH = "/api/v1/kits"

def auth_token():
    user = post_new_user(data.user_body)
    user_json = user.json()

    return user_json['authToken']

def post_new_client_kit(kit_body_key):
    token = auth_token()
    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {token}'

    kit_body = kit_body_key
    return requests.post(cofiguration.URL_SERVICE + configuration.KITS_PAHT,
                         json=kit_body,
                         headers=headers,
    )

response = post_new_client_kit(data.kit_bodies["one_character"])    

-Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, según el cuerpo de solicitud.
 Sin embargo, los pasos serán los mismos.

--Importa los bancos seder_stand_request.py y el banco data.py al banco post_new_client_kit.py
  -Puedes crear una función que cambiará el contenido del cuerpo de solicitud, nómbrala get_kit_body y agrega el parámetro name
  -Cada prueba debe estar en una función separada con el prefijo test, de lo contrario, Pytest las ignorará

def get_kit_body(name):
    reurn kit_bodies[name].copy()

--Hay dos tipos de pruebas en la lista de comprobación: positivas y negativas (código 400). 
Su lógica se puede expresar en funciones separadas: positive_assert(kit_body) y negative_assert_code_400(kit_body)

# Función de prueba positiva
def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name

# Función de prueba negativa para los casos en los que la solicitud devuelve un error
def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code

-La lista de comprobación completa debe estar en el banco create_kit_name_kit_test.py













