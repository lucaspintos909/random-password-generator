[![Run tests](https://github.com/lucaspintos909/random-password-generator/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/lucaspintos909/random-password-generator/actions/workflows/run-tests.yml)
# Random Password Generator
> Generador de contraseñas aleatorias

Genera una contraseña por default de 16 carácteres, 1 número y 1 simbolo, pudiendo además agregar parametros personalizados.

## Como usar
### Requerimientos
* Python 3
* Pipenv `pip install pipenv`
### Setup
```
pipenv install
```
### Ejecución básica
```
python run.py
```

### Parámetros
 - `--length` para indicar cantidad de carácteres
 - `--numbers` para indicar cantidad de números
 - `--symbols` para indicar cantidad de símbolos

Ejemplo: 
```
python run.py --length 25 --numbers 4 --symbols 4
```
![Resultado del ejemplo](./img/example.png)


## Development

#### Ejecutar tests
```
pipenv run test
```
