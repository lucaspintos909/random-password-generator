import random
import string


def generate(length=15, num_len=1, sym_len=1):

    valid_params = params_validation(length, num_len, sym_len)

    if not valid_params["valid"]:
        return valid_params

    # Concateno las letras en minúscula y en mayúscula
    letters = string.ascii_lowercase + string.ascii_uppercase

    # Calculo la cantidad de letras en base a los numero y simbolos solicitados
    number_of_letters = length - (num_len + sym_len)

    # Obtengo una lista con la cantidad de letras aleatorias
    letters = random.sample(letters, number_of_letters)

    # Obtengo una lista con la cantidad de numeros aleatorios
    numbers = random.sample(string.digits, num_len)

    # Obtengo una lista con la cantidad de simbolos aleatorios
    symbols = random.sample(string.punctuation, sym_len)

    # Junto las tres listas
    password = letters + numbers + symbols

    # Mezclo la lista
    random.shuffle(password)

    # Uno todos los caracteres de la lista
    password = ''.join(password)

    return {"valid": True, "password": password}


def params_validation(length, num_len, sym_len):
    error = {"valid": False, "message": ''}
    if length > 52:
        error["message"] = "La contraseña no puede tener mas de 52 caracteres."
        return error

    if num_len > 10:
        error["message"] = "La contraseña no puede tener mas de 10 números."
        return error

    if sym_len > 20:
        error["message"] = "La contraseña no puede tener mas de 10 simbolos."
        return error

    if length < 0 or num_len < 0 or sym_len < 0:
        error["message"] = "Parametros negativos invalidos."
        return error

    return {"valid": True}
