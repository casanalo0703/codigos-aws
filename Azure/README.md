# Codigos azure

Los códigos están divididos en las carpetas correspondientes dependiendo el tema que se haya visto, en caso de que se requieran instrucciones extra se pondrán en este documento

## Blob storage
Para blob storage se recomienda un ambiente virtual de python (venv) e instalar el `requeriments.txt`

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Además de exportar la key que nos ofrece blob storage:

Bash:
```bash
export AZURE_STORAGE_CONNECTION_STRING="<clave>"
```
PowerShell:
```powershell
setx AZURE_STORAGE_CONNECTION_STRING "<clave>"
```

## Cosmos db
para cosmosd db se necesita tener una cuenta de cosmos db, además de tener una base de datos dentro de un contenedor, y cambiar los nombres a los de su contenedor y base específicos.

Se debe de instalar `requirements.txt`, y, además de exportar las variables de `endpoint` y `key`.

Bash:
```bash
export ENDPOINT="<clave>"
export KEY="<clave>"
```
PowerShell:
```powershell
setx ENDPOINT "<clave>"
setx KEY "<clave>"
```