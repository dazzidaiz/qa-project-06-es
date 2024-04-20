# Pruebas de como la aplicación "Urban Grocers" crea kits de productos

- Mi tarea es automatizar las pruebas de la lista de comprobación
- Una de ellas es para el campo name al crear un kit de productos
- Estudiar las API de la aplicación "Urban Grocers", "Main.Kits" - "Crear un kit.”
- Las pruebas se pueden realizar en la aplicación PyCharm:

     -Paso 1. Conecta con tu GitHub  
     -Paso 2. Clona el repositorio en tu computadora
     -Paso 3. Se creará un repositorio automáticamente. El nombre del repositorio será qa-project-06

--En la aplicacion Pycharm se crearon automaticamente los bancos que utilizare en todas las pruebas
     -configuration.py        # URL  rutas de la solicitud
     -data.py                 # Datos de la solicitud
     -seder_stand_request.py  # Envio de las solicitudes
     -post_new_client_kit     # Pruebas
     -ready.md                # Descripcion del proyecto
     -.gitignore              # Bancos innecesarios
      
# Para inciar con las pruebas
- inicio el servidor de "Urban Grocers" para obtener la URL 
      NOTA SOBRE URL: cada que se inicia el servidor la URL cambia. 

--Importo URL del servidor, los datos de la solicitud y la libreria request, al banco sender_stand_request.py con el comando import
- Para crear un kit necesito crear primero un usuario para obtener los headers que en este caso es Autorization y Bearer Token

--Envio una solicitud para crear un nuevo usuario CREATE_USER_PATH = "/api/v1/users/"
- Esta solicitud me dara como resultado un authToken que es una clave de identificación del usuario,
utilizamos la funcion def le ponemos un nombre post_new_user_body, hacemos un return el request y el nombre de la solicitud post
los datos requeridos los estamos adquiriendo  de data.py los datos del usuario, la URL de configuration.py y la libreria requests 

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)

..Ahora envio una solicitud para crear un kit personal para este usuario. KITS_PATH = "/api/v1/kits"
En esta seccion se crearon dos funciones una para def auth_token y def post_new_client_kit
para que los headers sean los mismos para cada prueba de la lista 
..Envio la solicitud request.post para crear el usuario con diferentes parametros pero mismos headers
 
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

- Ahora los resultados de las prueba serán diferentes cada vez, según el cuerpo de solicitud.
 Sin embargo, los pasos serán los mismos.

--Importo los bancos seder_stand_request.py y el banco data.py al banco post_new_client_kit.py
  -Creo una función que cambia el contenido del cuerpo de solicitud, get_kit_body y agrego el parámetro name
  -Cada prueba debe estar en una función separada con el prefijo test, de lo contrario, Pytest las ignorará

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













