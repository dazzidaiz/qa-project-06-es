
import data
# Función de prueba positiva
def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name
# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code
# Prueba 1. El número permitido de caracteres (1): kit_body = { "name": "a"}
def kit_creation_test_1():
    kit_body = data.kit_bodies["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 201, kit_body ['name'])

# Prueba 2. Usuario o usuaria creada con éxito. El parámetro firstName contiene 15 caracteres
def test_creation_test_2():
    kit_body = data.kit_bodies["maximus_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 201, kit_body['name'])

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_creation_test_3():
    kit_body = data.kit_bodies["empty_string"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 400)

# Prueba 4. El número de caracteres es mayor que la cantidad permitida (512):
def test_creation_test_4():
    kit_body = data.kit_bodies["maximu_plus_one_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 400)

# Prueba 5. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_creation_test_5():
    kit_body = data.kit_bodies["special_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 201, kit_body['name'])

# Prueba 6. Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_creation_test_6():
    kit_body = data.kit_bodies["spaces"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 201, kit_body['name'])

# Prueba 7. Se permiten números: kit_body = { "name": "123" }
def test_creation_test_7():
    kit_body = data.kit_bodies["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 201, kit_body['name'])

# Prueba 8. El parámetro no se pasa en la solicitud: kit_body = { }
def test_creation_test_8():
    kit_body = data.kit_bodies["empty_name"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 400)

# Prueba 9. Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_creation_test_9():
    kit_body = data.kit_bodies["differet_characers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert(kit_response, expected_status_code: 400)
