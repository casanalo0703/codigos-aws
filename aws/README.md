# AWS
Los códigos de esta carpeta son para poder crear recursos de AWS.

## Lambda_ejemplo

Esta carpeta nos permite poder crear una lambda, empaquetarla como .zip y poder hacer deploy para que podamos tener nuestra lambda corriendo en la nube.

Para poder crear nuestra función en AWS:

1. Copia o descarga el código.
2. Instala todas las dependencias que se encuentran dentro de `requirements.txt` en la misma ruta que uses para tu carpeta, ejemplo:
```bash
pip install -r requirements.txt -t .
```
3. Empaqueta el código y las librerías en un solo `.zip`
4. Sube a tu cuenta de AWS y prueba el evento.