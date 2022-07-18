"""Modulo que hara una peticion y regresara su contenido"""
import json
import logging
from datetime import datetime
from typing import Tuple

import boto3
import requests
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
S3_CLIENT = boto3.client("s3")
BUCKET = "bucket-seminario"

log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


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
    logger.info("evento recibido", extra={"event": event})
    event = limpia_peticion(event)
    if not evento_valido(event):
        raise requests.RequestException("El evento es incorrecto")
    resultado = requests.get("https://randomuser.me/api")
    resultado = resultado.json()
    resultado["route"] = subir_a_s3(json.dumps(resultado), event)
    logger.info("Respuesta a mandar", extra={"resp": resultado})

    return resultado


def limpia_peticion(event):
    """
    Limpia la petición para las invocaciones de lambda, o las invocaiones HTTP

    Args:
        event - dict: El evento/petición que hizo que la lambda se activara

    Returns:
        dict: El evento json limpio
    """
    if "body" in event:
        body = event["body"]
        body = json.loads(body)
        return body

    return event


def evento_valido(event: dict) -> bool:
    """
    Revisa que el evento sea valido

    Args:
        event - dict: El evento que invoca a la lambda

    Returns:
        bool: Si el evento debe ser validado o no
    """
    return event.get("random_user", False)


def subir_a_s3(object: bytes, event: dict) -> Tuple[str, None]:
    """
    Sube a S3 la respuesta que se obtuvo de la API si el usuario asi lo necesita
    y regresa la llave (ruta) en donde se guarda el json

    Args:

    """
    fecha = datetime.now().strftime("%d%m%Y-%H-%M-%S")
    ruta = f"random_user/ejemplo/{fecha}.json"
    if event.get("upload_s3", False):
        logger.info("subiendo archivo a S3 con la ruta", extra={"ruta": ruta})
        S3_CLIENT.put_object(Bucket=BUCKET, Body=object, Key=ruta)
        return ruta

    logger.info("No e subira la informacion a S3")
    return None
