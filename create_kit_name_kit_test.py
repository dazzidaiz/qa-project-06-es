
import sender_stand_request
import data

def get_kit_body(name):
    reurn kit_bodies[name].copy()

# Función de prueba positiva
def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name

# Función de prueba negativa para los casos en los que la solicitud devuelve un error
def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code

# Prueba 1. El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_kit_1_1_letter_in_name_get_success_response():
    kit_body = data.kit_bodies["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

# Prueba 2. Usuario o usuaria creada con éxito. El parámetro firstName contiene 15 caracteres
def test_create_kit_2_maximum_characers_in_name_get_success_response():
    kit_body = data.kit_bodies["maximum_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

# Prueba 3. Error El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_kit_3_empty_string_in_name_get_negative_response():
    kit_body = data.kit_bodies["empty_string"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

# Prueba 4. Error El número de caracteres es mayor que la cantidad permitida (512):
def test_create_kit_4_maximum_plus_one_in_name_get_negaive_response():
    kit_body = data.kit_bodies["maximu_plus_one_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

# Prueba 5. Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_kit_t_special_characers_in_name_get_success_response():
    kit_body = data.kit_bodies["special_characters"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

# Prueba 6. Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_kit_6_spaces_in_name_get_success_response():
    kit_body = data.kit_bodies["spaces"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

# Prueba 7. Se permiten números: kit_body = { "name": "123" }
def test_create_kit_y_numbers_in_name_get_success_response():
    kit_body = data.kit_bodies["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

# Prueba 8. Error El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_kit_8_empty_name_in_name_get_negative_response():
    kit_body = data.kit_bodies["empty_name"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

# Prueba 9. Error Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_kit_9_different_in_name_get_negative_response():
    kit_body = data.kit_bodies["different_characers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)
