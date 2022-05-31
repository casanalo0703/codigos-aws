"""
Modulo que conecta a Azure Blob Storage, crea un contenedor y sube un archivo
"""

import time
from logging import getLogger
import os

from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

logger = getLogger()
LLAVE_DE_CONEXION = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CLIENTE_BLOB = BlobServiceClient.from_connection_string(LLAVE_DE_CONEXION)


def crea_contenedor(nombre_contenedor: str) -> BlobServiceClient:
    """
    Crea un contenedor en Azure Blob Storage

    Args:
        nombre_contenedor - str: Nombre del contenedor a crear

    Returns:
        BlobServiceClient: Cliente de Azure Blob Storage con el contenedor creado
    """
    try:
        return CLIENTE_BLOB.create_container(nombre_contenedor)
    except ResourceExistsError:
        logger.warning(f"El contenedor {nombre_contenedor} ya existe")
        return CLIENTE_BLOB.get_container_client(nombre_contenedor)


def sube_archivo_a_blob(contenedor: str, nombre_blob: str, archivo: str) -> BlobServiceClient:
    """
    Crea un blob a partir de un contenedor, si ya esta creado lo devuelve, ademas, sube un archivo al blob

    Args:
        contenedor - BlobServiceClient: Cliente de Azure Blob Storage con el contenedor creado
        nombre_blob - str: Nombre del blob a crear
        archivo - str: Ruta del archivo a subir

    Returns:
        blob - BlobClient: Cliente de Azure Blob Storage con el blob creado
    """
    logger.info("\nSubiendo a Azure Storage como blob: %s \n\t", archivo)
    time.sleep(1)
    blob = CLIENTE_BLOB.get_blob_client(container=contenedor, blob=nombre_blob)

    with open(archivo, "rb") as archivo_blob:
        blob.upload_blob(archivo_blob, overwrite=True)
    logger.info(f"Archivo {archivo} subido a Azure Blob Storage")

    return blob


def descarga_archivo_blob(blob: BlobServiceClient) -> bytes:
    """
    Descarga el contenido de un blob

    Args:
        blob - BlobClient: Cliente de Azure Blob Storage con el blob creado

    Returns:
        bytes: Contenido del blob
    """
    return blob.download_blob().readall()


def main():
    """
    Funcion principal
    """
    contenedor_imagenes = crea_contenedor("contenedor-imagenes")
    contenedor_archivos = crea_contenedor("contenedor-archivos")
    blob_imagen = sube_archivo_a_blob(
        "contenedor-imagenes", "blob-imagen.png", "Azure/img/test.jpg"
    )
    blob_archivo = sube_archivo_a_blob(
        "contenedor-archivos", "blob-texto.txt", "Azure/docs/test.txt"
    )
    print(descarga_archivo_blob(blob_archivo))


if __name__ == "__main__":
    main()
