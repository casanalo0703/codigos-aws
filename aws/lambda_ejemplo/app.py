"""Modulo que hara una peticion y regresara su contenido"""

import requests


def lambda_handler(event: dict, context: dict) -> dict:
    """
    Punto de entrada de las lambdas en AWS

    Args:
        event - dict: El evento/petición que hizo que la lambda se activara
        context - dict: El contexto que AWS nos ofrece, como el ID de la invocacion, el tiempo
            que le queda  la lambda para estar activa, su limite de memoria, etc.
            Ver más: https://docs.aws.amazon.com/es_es/lambda/latest/dg/python-context.html

    Returns:
        dict: El diccionario de la peticion a la pagina establecida
    """
    if not evento_valido(event):
        raise requests.RequestException("El evento es incorrecto")
    resultado = requests.get("https://randomuser.me/api")

    return resultado.json()


def evento_valido(event: dict) -> bool:
    """
    Revisa que el evento sea valido

    Args:
        event - dict: El evento que invoca a la lambda

    Returns:
        bool: Si el evento debe ser validado o no
    """
    return event.get("random_user", False)


print(lambda_handler({"random_user": True}, None))
