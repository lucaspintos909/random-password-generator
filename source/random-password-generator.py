import random
import string

def generateRandomPassword(pass_len = 15, num_len = 1, sym_len = 1):

    # Concateno las letras en minúscula y en mayúscula
    letters = string.ascii_lowercase + string.ascii_uppercase

    # Calculo la cantidad de letras en base a los numero y simbolos solicitados
    number_of_letters = pass_len - (num_len + sym_len)

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

    return password